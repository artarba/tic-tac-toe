from typing import List

import cv2
import pytesseract
import numpy as np


def recognize_tic_tac_toe(cropped_image: np.ndarray) -> List[int]:
    # Преобразование обрезанного изображения в байты
    _, image_encoded = cv2.imencode('.png', cropped_image)
    image_bytes = image_encoded.tobytes()

    # Преобразование байтов изображения в массив NumPy
    np_array = np.frombuffer(image_bytes, np.uint8)

    # Декодирование изображения из массива NumPy
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Преобразование в оттенки серого для лучшего распознавания текста
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

    result = (pytesseract.image_to_string(gray_image, config='--psm 6')
              .replace("|", '')
              .replace(' ', '')
              .replace('\n', '').lower())

    board = []
    for char in result:
        if char == 'x':
            board.append(1)
        elif char == 'o':
            board.append(0)

    # Проверка и заполнение массива, если распознанный текст был неполным
    if len(board) < 9:
        board.extend([-1] * (9 - len(board)))

    return board[:9]
