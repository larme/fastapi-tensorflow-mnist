import json

from fastapi import FastAPI, File, UploadFile
import numpy as np
import tensorflow as tf
import PIL

app = FastAPI()

model = tf.saved_model.load("mnist_model")


@app.post("/predict_image/")
def predict_image(file: UploadFile = File(...)):
    img = PIL.Image.open(file.file)
    arr = np.array(img) / 255.0
    assert arr.shape == (28, 28)
    arr = np.expand_dims(arr, axis=2).astype("float32")
    arr = np.expand_dims(arr, axis=0)
    pred = model(arr).numpy()
    return json.dumps(pred.tolist())
    return item
