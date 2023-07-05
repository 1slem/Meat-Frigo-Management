import self as self
from PIL import Image
import pytesseract
import cv2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow requests with any HTTP method
    allow_headers=["*"],
)

@app.get("/")
async def root():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    video_files = [
        'C:/Users/Islamovic/Downloads/Video/v2.mp4',
        "C:/Users/Islamovic/Downloads/Video/v2.mp4",
        "C:/Users/Islamovic/Downloads/Video/v3.mp4"
    ]
    results = []
    for video_file in video_files:
        cap = cv2.VideoCapture(video_file)
        video_text = ""

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            video_text += text
            if video_text != "":
                break

        cap.release()
        results.append(video_text)
    return {"item": results}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
