import fitz
from pdf2image import convert_from_path

from app.services.ocr_service import ocr_service
from app.services.text_cleaner import text_cleaner


class PDFProcessor:

    def extract_text(self, pdf_path: str) -> str:

        extracted_text = ""

        try:

            doc = fitz.open(pdf_path)

            for page in doc:
                extracted_text += page.get_text()

            doc.close()

        except Exception as e:
            raise Exception(
                f"PDF extraction failed: {str(e)}"
            )

        cleaned_text = text_cleaner.clean(
            extracted_text
        )

        # If text exists, return directly
        if len(cleaned_text) > 100:
            return cleaned_text

        # Otherwise run OCR
        return self.extract_text_using_ocr(
            pdf_path
        )

    def extract_text_using_ocr(
        self,
        pdf_path: str
    ) -> str:

        all_text = ""

        images = convert_from_path(
            pdf_path,
            dpi=300
        )

        for image in images:

            page_text = ocr_service.extract_text(
                image
            )

            all_text += page_text + "\n"

        return text_cleaner.clean(all_text)


pdf_processor = PDFProcessor()