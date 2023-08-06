import numpy as np
import cv2
from typing import Union, Optional


def crop(image_bytes: Union[bytes, np.ndarray]) -> Optional[np.ndarray]:
    np_array = np.fromstring(image_bytes, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Преобразование в оттенки серого для лучшего распознавания текста
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Инвертирование текста в белый цвет
    gray = 255 * (gray < 128).astype(np.uint8)
    coords = cv2.findNonZero(gray)

    x, y, w, h = cv2.boundingRect(coords)
    cropped_image = image[y:y + h, x:x + w]

    return cropped_image
