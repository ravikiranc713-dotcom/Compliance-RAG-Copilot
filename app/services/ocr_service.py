import pytesseract
from PIL import Image


class OCRService:

    def extract_text(self, image: Image.Image) -> str:
        """
        Extract text from image using Tesseract OCR
        """

        text = pytesseract.image_to_string(image)

        return text.strip()


ocr_service = OCRService()