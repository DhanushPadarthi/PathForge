import PyPDF2
import pdfplumber
from docx import Document
import logging
from typing import Optional
import io

logger = logging.getLogger(__name__)

class ResumeParser:
    
    @staticmethod
    async def parse_pdf(file_content: bytes) -> str:
        """
        Parse PDF file and extract text content
        """
        try:
            # Try with pdfplumber first (better text extraction)
            text = ""
            with pdfplumber.open(io.BytesIO(file_content)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            if text.strip():
                logger.info(f"Extracted {len(text)} characters using pdfplumber")
                return text.strip()
            
            # Fallback to PyPDF2
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            logger.info(f"Extracted {len(text)} characters using PyPDF2")
            return text.strip()
            
        except Exception as e:
            logger.error(f"Error parsing PDF: {e}")
            raise ValueError(f"Failed to parse PDF: {str(e)}")
    
    @staticmethod
    async def parse_docx(file_content: bytes) -> str:
        """
        Parse DOCX file and extract text content
        """
        try:
            doc = Document(io.BytesIO(file_content))
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            
            logger.info(f"Extracted {len(text)} characters from DOCX")
            return text.strip()
            
        except Exception as e:
            logger.error(f"Error parsing DOCX: {e}")
            raise ValueError(f"Failed to parse DOCX: {str(e)}")
    
    @staticmethod
    async def parse_resume(file_content: bytes, filename: str) -> str:
        """
        Parse resume file based on extension
        """
        file_ext = filename.lower().split('.')[-1]
        
        if file_ext == 'pdf':
            return await ResumeParser.parse_pdf(file_content)
        elif file_ext in ['docx', 'doc']:
            return await ResumeParser.parse_docx(file_content)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")

# Global parser instance
resume_parser = ResumeParser()
