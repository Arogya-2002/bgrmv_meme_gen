from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse, StreamingResponse

import shutil
import os
import io

import base64
import sys

from src.pipeline.bg_prediction_pipeline import process_remove_bg, process_add_bg, process_inpaint
from src.pipeline.run_meme_generator_pipeline import run_pipeline, fetch_image_templates
from src.exceptions import CustomException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev or frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static and template directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    try:
        temp_input_path = f"temp_{file.filename}"
        with open(temp_input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        output_path = process_remove_bg(temp_input_path)

        with open(output_path, "rb") as image_file:
            image_bytes = image_file.read()

        os.remove(temp_input_path)
        return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")

    except CustomException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


@app.post("/add-background/")
async def add_background(
    foreground: UploadFile = File(...),
    background: UploadFile = File(...)
):
    try:
        temp_foreground_path = f"temp_foreground_{foreground.filename}"
        with open(temp_foreground_path, "wb") as buffer:
            shutil.copyfileobj(foreground.file, buffer)

        temp_background_path = f"temp_background_{background.filename}"
        with open(temp_background_path, "wb") as buffer:
            shutil.copyfileobj(background.file, buffer)

        output_path = process_add_bg(temp_foreground_path, temp_background_path)

        with open(output_path, "rb") as image_file:
            image_bytes = image_file.read()

        os.remove(temp_foreground_path)
        os.remove(temp_background_path)

        return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")

    except CustomException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


@app.post("/inpaint/")
async def inpaint_image(
    input_image: UploadFile = File(...),
    mask_image: UploadFile = File(...)
):
    try:
        temp_input_path = f"temp_input_{input_image.filename}"
        with open(temp_input_path, "wb") as buffer:
            shutil.copyfileobj(input_image.file, buffer)

        temp_mask_path = f"temp_mask_{mask_image.filename}"
        with open(temp_mask_path, "wb") as buffer:
            shutil.copyfileobj(mask_image.file, buffer)

        output_path = process_inpaint(mask_img_path=temp_mask_path, input_img_path=temp_input_path)

        with open(output_path, "rb") as image_file:
            image_bytes = image_file.read()

        os.remove(temp_input_path)
        os.remove(temp_mask_path)

        return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")

    except CustomException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}



# Input model
class TopicInput(BaseModel):
    topic_name: str

# --- Routes ---

@app.post("/generate-meme", summary="Generate meme and return PNG")
def generate_meme_api(input: TopicInput):
    try:
        result = run_pipeline(input.topic_name)
        image_bytes = result["image_bytes"]
        emotion = result["emotion"]

        image_bytes.seek(0)

        return StreamingResponse(
            image_bytes,
            media_type="image/png",
            headers={"X-Emotion": emotion}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-meme-base64", summary="Generate meme and return as base64")
def generate_meme_base64_api(input: TopicInput):
    try:
        result = run_pipeline(input.topic_name)
        image_bytes = result["image_bytes"]
        emotion = result["emotion"]

        image_bytes.seek(0)
        base64_str = base64.b64encode(image_bytes.read()).decode()

        return {
            "status": "success",
            "emotion": emotion,
            "image_base64": f"data:image/png;base64,{base64_str}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/fetch-templates", summary="Fetch image templates from Supabase")
def fetch_templates_api():
    try:
        result = fetch_image_templates()
        return JSONResponse(content={"status": "success", "templates": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
