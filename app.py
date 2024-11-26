from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from pdf2image import convert_from_path
import os
import uuid
from typing import Optional

app = FastAPI()

# Directory for saving temporary images
TEMP_FOLDER = "temp_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)

@app.post("/pdf2image/")
async def pdf_to_image_api(
    pdf_file: UploadFile = File(...),
    page_number: Optional[int] = Form(None),
    output_format: str = Form("png"),
    dpi: int = Form(300)
):
    """
    Endpoint to convert a PDF to images.
    
    Parameters:
        pdf_file (UploadFile): The uploaded PDF file.
        page_number (int, optional): The specific page number to convert. Converts all pages if not provided.
        output_format (str): The desired image format (png, jpeg, jpg). Default is "png".
        dpi (int): Resolution of the output image. Default is 300.
        
    Returns:
        JSONResponse or FileResponse: JSON with paths to images or the specific image.
    """
    try:
        # Save the uploaded file temporarily
        file_id = str(uuid.uuid4())
        temp_pdf_path = os.path.join(TEMP_FOLDER, f"{file_id}.pdf")
        with open(temp_pdf_path, "wb") as temp_pdf:
            temp_pdf.write(await pdf_file.read())
        
        # Convert PDF to image(s)
        if page_number:
            pages = convert_from_path(temp_pdf_path, dpi=dpi, first_page=page_number, last_page=page_number)
        else:
            pages = convert_from_path(temp_pdf_path, dpi=dpi)

        image_paths = []
        for i, page in enumerate(pages):
            image_path = os.path.join(TEMP_FOLDER, f"{file_id}_page_{i + 1}.{output_format}")
            page.save(image_path, output_format.upper())
            image_paths.append(image_path)
        
        # If only one page, return the file directly
        if len(image_paths) == 1:
            return FileResponse(image_paths[0], media_type=f"image/{output_format}")

        # Otherwise, return paths to all images
        return JSONResponse({"images": image_paths})
    
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
    
    finally:
        # Cleanup temporary PDF
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)

# Run the app using: uvicorn app:app --reload

