import io
import json
import logging

import numpy as np
import onnxruntime
import requests
from PIL import Image

logging.basicConfig(level=logging.INFO)
model_path = "model.onnx"
classes_path = "classes.json"

model = onnxruntime.InferenceSession(model_path)
with open(classes_path) as f:
    classes = json.load(f)


def get_images(limit=5):
    response = requests.get(f"https://picsum.photos/v2/list?limit={limit}").json()
    image_urls = [_["download_url"] for _ in response]

    images = []
    for image_url in image_urls:
        image_response = requests.get(image_url)
        img = Image.open(io.BytesIO(image_response.content)).convert("RGB")
        images.append(img)

    return images


def predict(images):
    def image_to_tensor(im):
        im = im.resize((224, 224))
        return np.asarray(im, dtype=np.float32)

    full_results = []
    for image in images:
        ims_tensor = np.asarray(list(map(image_to_tensor, [image])), dtype=np.float32)

        ims_tensor = np.moveaxis(ims_tensor, 3, 1)

        model_input = model.get_inputs()[0].name
        model_output = model.get_outputs()[0].name

        logging.debug(model_input)
        logging.debug(model_output)
        results = model.run(None, {model_input: ims_tensor})
        results = np.array(results).flatten()
        logging.debug(results)
        ans = str(np.argmax(results))
        logging.debug(ans)

        logging.info(classes[ans])

        full_results.append(classes[ans])

    return full_results


def main():
    for _ in range(30):
        images = get_images(limit=30)
        predict(images)
        logging.info(_)


if __name__ == "__main__":
    logging.info("Starting...")
    main()
    logging.info("Done")
