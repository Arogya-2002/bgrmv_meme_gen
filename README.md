# 🎨 AI-Powered Image Processing & Meme Generation Suite

A comprehensive image processing service that combines intelligent background manipulation with creative meme generation. This powerful suite offers background removal, replacement, inpainting capabilities, and an innovative Tenglish meme generator - all through clean web interfaces and REST APIs.

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)  
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)  
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Features

### 🖼️ Image Processing Suite
- **🎯 Smart Background Removal**: Leverage the powerful U2NET model via `rembg` library for precise background removal  
- **🖼️ Background Replacement**: Seamlessly add custom backgrounds to transparent images  
- **🪄 Inpainting**: Fill masked areas in images using stable diffusion inpainting models  

### 🔥 Meme Generation Engine
- **🧠 AI-Powered Meme Creation**: Generate contextual memes based on user-provided topics
- **🎭 Emotion Detection**: Analyze emotional tone to select suitable meme templates
- **🖋️ Tenglish Support**: Custom font rendering for Telugu-English text combinations
- **☁️ Dynamic Templates**: Supabase integration for template management

### 🚀 Common Infrastructure
- **🌐 REST API**: FastAPI-powered endpoints for programmatic access  
- **🖥️ Web Interface**: Clean, responsive HTML interfaces for easy interaction  
- **📁 Modular Architecture**: Well-organized codebase with reusable components  
- **🛡️ Robust Error Handling**: Comprehensive logging and exception management  
- **🗂️ Smart File Management**: Automatic temporary file cleanup and organized storage  

---

## 📁 Unified Project Structure

```
image-processing-suite/
├── app.py                          # Main FastAPI application
├── meme_app.py                     # Meme generator FastAPI app (optional separate deployment)
├── static/                         # Static assets
│   └── style.css                   # Styling for web interfaces
├── templates/                      # Jinja2 HTML templates
│   ├── index.html                  # Image processing interface
│   └── meme.html                   # Meme generation interface
├── src/
│   ├── components/
│   │   ├── add_bg.py              # Background addition logic
│   │   ├── remove_bg.py           # Background removal logic
│   │   ├── inpaint.py             # Inpainting logic using Stable Diffusion
│   │   ├── emotion_detection.py   # Emotion analysis for memes
│   │   ├── meme_generation.py     # Meme creation logic
│   │   └── topic_ingestion.py     # Topic processing for memes
│   ├── entity/
│   │   ├── artifact.py            # Data classes and artifacts
│   │   ├── config.py              # Configuration management
│   │   └── meme_entities.py       # Meme-specific data structures
│   ├── exceptions.py              # Custom exception definitions
│   ├── logger.py                  # Logging configuration
│   ├── pipeline/
│   │   ├── bg_prediction_pipeline.py  # Image processing pipeline
│   │   └── meme_pipeline.py           # Meme generation pipeline
│   └── utils/
│       ├── common.py              # Shared utility functions
│       └── template_selection.py # Meme template utilities
├── artifacts/                     # Data and output folders
│   ├── memes/                     # Generated memes storage
│   ├── processed_images/          # Background processed images
│   └── emotion_image_urls.json    # Template mappings from Supabase
├── fonts/
│   └── NotoSansTelugu-Regular.ttf # Font for Tenglish rendering
├── template_dir/                  # Meme template storage
├── logs/                          # Application logs
├── README.md                      # This documentation
└── requirements.txt               # Python dependencies
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher  
- Git  
- Supabase account (for meme generation)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/image-processing-suite.git
   cd image-processing-suite
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   # Using conda
   conda create -p venv python==3.10 -y
   conda activate venv/
   
   # Or using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: Additional system dependencies may be required:
   > - **Ubuntu/Debian**: `sudo apt-get install libglib2.0-0`
   > - **macOS**: Usually works out of the box
   > - **Windows**: May require Visual C++ Build Tools

4. **Environment Configuration**
   ```bash
   # Create .env file with your configurations
   cp .env.example .env
   # Add your Supabase credentials and other API keys
   ```

### Deployment Options

#### Option 1: Single Unified Service
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

#### Option 2: Microservices Architecture
```bash
# Terminal 1 - Image Processing Service
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Meme Generation Service  
uvicorn meme_app:app --reload --host 0.0.0.0 --port 8001
```

#### Option 3: Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build
```

#### Option 4: Cloud Deployment
```bash
# Deploy to cloud platforms
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

---

## 📖 Usage

### Web Interfaces

#### Image Processing Interface
Navigate to `http://127.0.0.1:8000` for:
- **Remove Background**: Upload an image and click "Remove Background"  
- **Add Background**: Upload foreground and background images  
- **Inpaint Image**: Upload input image and mask for region filling  

#### Meme Generation Interface  
Navigate to `http://127.0.0.1:8000/memes` for:
- **Generate Meme**: Enter a topic and get AI-generated Tenglish memes
- **Browse Templates**: View available meme templates by emotion

### API Endpoints

#### 🖼️ Image Processing APIs

##### `POST /remove-background/`
Remove background from an uploaded image.
- **Parameters**: `file` (multipart/form-data)
- **Response**: PNG image with transparent background

##### `POST /add-background/`
Add a new background to a foreground image.
- **Parameters**: `foreground`, `background` (image files)
- **Response**: Composite image with new background

##### `POST /inpaint/`
Inpaint masked regions of an image.
- **Parameters**: `input_image`, `mask_image` (image files)
- **Response**: Inpainted image

#### 🔥 Meme Generation APIs

##### `POST /generate-meme`
Generate a meme and return as PNG stream.
```json
{
  "topic_name": "job interviews"
}
```
**Response**: Streaming PNG with `X-Emotion` header

##### `POST /generate-meme-base64`
Generate meme and return as base64.
```json
{
  "topic_name": "first salary"
}
```
**Response**:
```json
{
  "status": "success",
  "emotion": "happy",
  "image_base64": "data:image/png;base64,..."
}
```

##### `GET /fetch-templates`
Retrieve available meme templates.
**Response**:
```json
{
  "status": "success",
  "templates": {
    "happy": ["template1.png"],
    "sad": ["template2.png"]
  }
}
```

---

## ⚙️ Configuration

### Image Processing Configuration
Configure in `src/entity/config.py`:
- **File paths**: Processed image storage locations
- **Model settings**: Background removal and inpainting parameters
- **Processing options**: Image quality, format settings

### Meme Generation Configuration
Configure in `src/entity/meme_entities.py`:
- **Supabase credentials**: Database connection settings
- **Font settings**: Tenglish rendering options
- **Template management**: Emotion-template mappings
- **AI model settings**: Text generation parameters

---

## 🔧 Technical Architecture

### Core Technologies
- **Image Processing**: U2NET via `rembg`, Stable Diffusion inpainting
- **Meme Generation**: Google Gemini for dialogue, Supabase for templates
- **Web Framework**: FastAPI with Jinja2 templating
- **Image Manipulation**: Pillow (PIL) with custom font rendering
- **Database**: Supabase for template and metadata storage

### Processing Pipelines
- **Background Pipeline**: Remove → Process → Replace/Inpaint
- **Meme Pipeline**: Topic Analysis → Emotion Detection → Template Selection → Text Overlay

---

## 🧪 Sample Usage

### Image Processing
```bash
# Remove background
curl -X POST http://127.0.0.1:8000/remove-background/ \
     -F "file=@image.jpg" \
     --output transparent.png

# Add background
curl -X POST http://127.0.0.1:8000/add-background/ \
     -F "foreground=@person.png" \
     -F "background=@sunset.jpg" \
     --output composite.jpg
```

### Meme Generation
```bash
# Generate meme as PNG
curl -X POST http://127.0.0.1:8000/generate-meme \
     -H "Content-Type: application/json" \
     -d '{"topic_name": "monday mornings"}' \
     --output meme.png

# Generate meme as base64
curl -X POST http://127.0.0.1:8000/generate-meme-base64 \
     -H "Content-Type: application/json" \
     -d '{"topic_name": "exam results"}'
```

---

## 🚀 Deployment Strategies

### 1. **Monolithic Deployment**
Single service handling all functionality - ideal for small to medium scale.

### 2. **Microservices Architecture**
Separate services for image processing and meme generation - better for scaling and maintenance.

### 3. **Containerized Deployment**
Docker containers with orchestration - production-ready with load balancing.

### 4. **Serverless Deployment**
Function-based deployment on AWS Lambda, Google Cloud Functions, or similar platforms.

### 5. **Hybrid Cloud**
Combine local processing with cloud storage and CDN distribution.

---

## 🛠️ Development & Contributing

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Code formatting
black src/
isort src/

# Type checking
mypy src/
```

### Adding New Features

#### For Image Processing:
1. Implement logic in `src/components/`
2. Add configuration in `src/entity/config.py`
3. Create pipeline in `src/pipeline/`
4. Add API endpoint in `app.py`

#### For Meme Generation:
1. Extend emotion detection in `src/components/emotion_detection.py`
2. Add template logic in `src/utils/template_selection.py`
3. Update pipeline in `src/pipeline/meme_pipeline.py`
4. Add endpoints in `meme_app.py`

---

## 🚀 Future Roadmap

### Image Processing Enhancements
- [ ] **Advanced Models**: SAM, Deeplab integration
- [ ] **Batch Processing**: Multiple image handling
- [ ] **Real-time Processing**: WebSocket support
- [ ] **Extended Formats**: WebP, HEIC, AVIF support

### Meme Generation Features
- [ ] **Multi-language Support**: Beyond Tenglish
- [ ] **Custom Template Upload**: User-generated templates
- [ ] **Animated Memes**: GIF generation support
- [ ] **Social Integration**: Direct sharing capabilities

### Infrastructure Improvements
- [ ] **User Authentication**: Account management
- [ ] **Cloud Storage**: AWS S3, Google Cloud integration
- [ ] **CDN Integration**: Fast global content delivery
- [ ] **Analytics Dashboard**: Usage metrics and insights
- [ ] **API Rate Limiting**: Usage quotas and throttling
- [ ] **Enhanced UI**: Modern React/Vue.js frontends

---

## 🤝 Contributing

Contributions welcome! Please read our contributing guidelines:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📞 Contact & Support

**Primary Maintainer**: Arogya Vamshi  
- Email: [arogyavamshi2002@gmail.com](mailto:arogyavamshi2002@gmail.com)  
- GitHub: [@Arogya-2002](https://github.com/Arogya-2002)  

**Community Support**:
- 📋 Issues: [GitHub Issues](https://github.com/your-username/image-processing-suite/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-username/image-processing-suite/discussions)
- 📖 Wiki: [Project Wiki](https://github.com/your-username/image-processing-suite/wiki)

---

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - Excellent background removal library
- [Stable Diffusion](https://huggingface.co/stabilityai/stable-diffusion-2-inpainting) - AI inpainting capabilities
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [U2NET](https://github.com/xuebinqin/U-2-Net) - Underlying segmentation model
- [Supabase](https://supabase.com/) - Backend-as-a-service platform
- [Google Gemini](https://ai.google.dev/) - AI text generation

---

⭐ **Star this repository if you found it helpful!**

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/your-username/image-processing-suite)
![GitHub forks](https://img.shields.io/github/forks/your-username/image-processing-suite)
![GitHub issues](https://img.shields.io/github/issues/your-username/image-processing-suite)
![GitHub license](https://img.shields.io/github/license/your-username/image-processing-suite)