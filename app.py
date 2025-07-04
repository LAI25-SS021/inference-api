from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from services import predict, read_image

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"message": "API Running"}


@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"

    # Read the image
    image = read_image(await file.read())

    # Predict and format
    prediction = predict(image)

    response = {}
    response["status"] = "success"
    response["message"] = "Predict success"
    response["data"] = prediction
    return response


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
