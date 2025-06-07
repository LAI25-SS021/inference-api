from PIL import Image
from io import BytesIO

import tensorflow as tf
import numpy as np

from utils.format_output import format_image_pred

model = None
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANNELS = 3
CLASSES = ["Berminyak", "Kering", "Normal"]


def load_model():
    path = "mobilenetv2.keras"
    model = tf.keras.models.load_model(path)
    return model


def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()
    image = np.asarray(image.resize((IMAGE_WIDTH, IMAGE_HEIGHT)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 255.0
    np.set_printoptions(suppress=True)
    prediction = model.predict(image)
    result = format_image_pred(prediction, CLASSES)
    return result
