import requests
import cv2
import numpy as np
from io import BytesIO

def swap_faces_from_urls(source_url: str, target_url: str):
    source_img = _download_image(source_url)
    target_img = _download_image(target_url)

    # --- Simple Placeholder Swap (flip source) ---
    swapped_img = cv2.addWeighted(source_img, 0.5, target_img, 0.5, 0)

    _, buffer = cv2.imencode(".jpg", swapped_img)
    img_bytes = BytesIO(buffer.tobytes())
    img_bytes.seek(0)
    return img_bytes

def _download_image(url: str):
    response = requests.get(url)
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_COLOR)
