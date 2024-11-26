# Pdf2Image

A simple, fast, and efficient API for converting PDF files into high-quality images. Built with **FastAPI** and powered by the **pdf2image** library, this API provides flexible options to convert individual pages or entire PDFs into images of various formats (PNG, JPEG, etc.).

---

## 🚀 Features

- Convert PDFs to images with ease.
- Support for multiple image formats: PNG, JPEG, JPG.
- Convert a specific page or the entire document.
- Adjustable image quality through DPI (Dots Per Inch) settings.
- Returns either the converted image file or a JSON list of image paths.

---

## 🛠️ Installation

### Prerequisites

- **Python**: Version 3.8 or later.
- **Poppler**: A PDF rendering library required by `pdf2image`.

Install Poppler:

```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils

# macOS (using Homebrew)
brew install poppler
```

### Steps to Install Locally

1. **Clone the Repository**

   ```bash
   git clone git@github.com:Sambatra-Andriamihaja/pdf-to-image.git
   cd pdf-to-image-api
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server**
   ```bash
   uvicorn app:app --reload
   ```

The API will now be available at `http://127.0.0.1:8000`.

---

## 📖 Use

### Endpoint: `/pdf-to-image/`

#### **Request Parameters**

| Parameter       | Type     | Required | Default | Description                                                                 |
| --------------- | -------- | -------- | ------- | --------------------------------------------------------------------------- |
| `pdf_file`      | `file`   | Yes      | -       | The PDF file to be converted.                                               |
| `page_number`   | `int`    | No       | All     | The specific page number to convert (1-based index). Converts all if unset. |
| `output_format` | `string` | No       | `png`   | The desired image format (`png`, `jpeg`, `jpg`).                            |
| `dpi`           | `int`    | No       | 300     | The resolution of the output image (higher DPI results in better quality).  |

---

### Example Usage

#### With `curl`

```bash
curl -X POST "http://127.0.0.1:8000/pdf-to-image/" \
-F "pdf_file=@sample.pdf" \
-F "page_number=2" \
-F "output_format=jpeg" \
-F "dpi=200"
```

#### With Postman

1. Set method to `POST`.
2. Use the URL: `http://127.0.0.1:8000/pdf-to-image/`.
3. Add the following **Form Data**:
   - **Key**: `pdf_file` | **Value**: Upload a PDF file.
   - **Key**: `page_number` (Optional) | **Value**: Specify the page number.
   - **Key**: `output_format` (Optional) | **Value**: Desired image format.
   - **Key**: `dpi` (Optional) | **Value**: Set the image resolution.

#### Example Response

1. For a single-page conversion, you receive the image file directly:
   - Media Type: `image/jpeg` (or based on `output_format`).
2. For multiple pages, you receive a JSON response:
   ```json
   {
     "images": ["temp_images/1234_page_1.png", "temp_images/1234_page_2.png"]
   }
   ```

---

## 🧹 Maintenance

Temporary files (uploaded PDFs and generated images) are saved in the `temp_images` directory. To free up space, clean this folder regularly:

```bash
rm -rf temp_images/*
```

---

## 📦 Deployment

For production:

1. Set up a reverse proxy with **Nginx** or **Apache**.
2. Use HTTPS for secure communication.
3. Limit the file upload size in the API to prevent abuse.

---

## 👨‍💻 Contributing

Contributions are welcome! Follow these steps:

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add feature-name'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 💬 Support

If you encounter any issues or have suggestions, feel free to open an issue or contact me at [sambatra.andriamihaja@outlook.com](mailto:sambatra.andriamihaja@outlook.com).
