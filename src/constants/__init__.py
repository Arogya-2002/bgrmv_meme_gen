import os

# Root artifact directory
ARTIFACTS_DIR = "artifacts"

# Subdirectories
REMOVED_BG_DIR = os.path.join(ARTIFACTS_DIR, "removed_bg_images")
CHANGED_BG_DIR = os.path.join(ARTIFACTS_DIR, "changed_bg_images")
UPLOADED_BG_DIR = os.path.join(ARTIFACTS_DIR, "user_uploaded_bg_images")

# Image filenames
RMBG_IMG_NAME = "removed_bg.png"
BG_IMG_NAME = "background.png"
CH_BG_IMG_NAME = "changed_bg.png"

# Default path folder (can be anything general)
IMG_PATH_FOLDER = ARTIFACTS_DIR

"""constants for image inpainting"""
MASK_IMG_NAME = "mask.png"
INPUT_IMG_NAME = "input_image.png"
INPAINT_OUTPUT_DIR = os.path.join(ARTIFACTS_DIR, "inpainted_images")
INPAINT_OUTPUT_IMG_NAME = "output_image.png"





# Meme generation constants
import os
from dotenv import load_dotenv

load_dotenv()
# Directory paths
TEMPLATE_DIR = "meme_templates"
FONT_PATH = "fonts/Noto_Sans_Telugu/NotoSansTelugu-Regular.ttf"

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")


# Emotion templates
EMOTION_TEMPLATES =['happy', 'sad', 'angry', 'surprise', 'neutral', 'sarcastic']


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET_PATH= os.getenv("BUCKET_PATH") 


EMOTIONS_CSV_PATH = "emotions_rows.csv"  
# Emotion templates mapping

TOPIC_NAME = None

OUTPUT_DIR = "artifacts"
TEMPLATES_DIR = "template_dir"
JSON_FILE = "emotion_image_urls.json"
MEMES = "memes"