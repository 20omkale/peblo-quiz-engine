import fitz  # PyMuPDF


def ingest_pdf(file_path: str):
    """
    Extract text from PDF and split into chunks
    """

    doc = fitz.open(file_path)

    full_text = ""

    for page in doc:
        full_text += page.get_text()

    doc.close()

    # basic chunking
    chunk_size = 500
    chunks = []

    for i in range(0, len(full_text), chunk_size):
        chunk = full_text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks