import base64
import io
import PyPDF2
import json


def lambda_handler(event, context):

    pdf_data = json.loads(event["body"])["pdf_data"]
    decoded_data = base64.b64decode(pdf_data)

    pdf_reader = PyPDF2.PdfReader(io.BytesIO(decoded_data))

    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return {"statusCode": 200, "body": text}
