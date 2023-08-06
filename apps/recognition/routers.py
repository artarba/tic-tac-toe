from fastapi import APIRouter, UploadFile, File, HTTPException

from apps.recognition.constants import ALLOWED_EXTENSIONS
from apps.recognition.schemas import RecognitionListResponse
from apps.recognition.utils.resize_image import crop
from apps.recognition.utils.recognition_image import recognize_tic_tac_toe

recognition_router = APIRouter(tags=["recognition"])


@recognition_router.post("/recognition_image/")
async def upload_image(image: UploadFile = File(...)) -> RecognitionListResponse:
    """
        Распознавание результата игры "Крестики-нолики" по загруженному изображению.

        Эта конечная точка принимает загруженное изображение, выполняет обработку изображения для распознавания доски
        "Крестики-нолики".

        Замечен местами некорректный результат для некоторых шрифтов.
        Тестирование проводилось с шрифтом: **Comic Sans MS**

        Параметры:
        - **image**: Загруженный файл изображения в формате PNG или JPEG.

        Возвращает:
        - **status_code**: Код состояния ответа (200 в случае успеха).
        - **result**: Список, представляющий доску Tic-Tac-Toe, где:
            - 1 обозначает "X" (крестики).
            - 0 обозначает "O" (нули).
            - -1 если числа нет или его не удалось распознать
            (Добавляется в конец результата. **Не показывает фактического местоположения**)
        """
    # Читаем содержимое файла
    image_content = await image.read()

    file_extension = image.filename.split('.')[-1].lower()
    if '.' + file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Неверный формат файла. Допускаются только файлы PNG или JPEG.")

    # Кропаем изображение
    cropped_image = crop(image_content)

    recognition_result = recognize_tic_tac_toe(cropped_image)
    if len(set(recognition_result)) == 1:
        raise HTTPException(status_code=400, detail="Символы не обнаружены")

    return RecognitionListResponse(items=recognition_result)
