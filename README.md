# lambda_pdf2text


Lambda PDF Text Extractor
This Lambda function extracts text from a PDF file encoded in base64 format. It's useful for scenarios where you need to extract text data from PDF files within an AWS Lambda environment.

Usage
Input: Provide the PDF data as a base64-encoded string in a JSON object with the key "pdf_data". The function expects this input in the event body.


```json
{
    "pdf_data": "<base64_encoded_pdf_data>"
}
```

Output: The function returns the extracted text as a response with a 200 status code.

```json
{
    "statusCode": 200,
    "body": "<extracted_text>"
}
```

Dependencies
PyPDF2: Python library for reading PDF files.
base64: Python module for base64 encoding and decoding.
io: Python module for handling I/O operations.
json: Python module for JSON manipulation.
Installation
Clone or download the code from this repository.

Ensure you have Python installed on your local machine.

Install the required dependencies using pip:

```
pip install PyPDF2
```

Copy and paste the provided Lambda function code into a Python file (e.g., lambda_function.py).

Deployment
To deploy this function to AWS Lambda:

Zip the Python file along with the installed dependencies.

python
```
zip -r lambda_function.zip lambda_function.py /path/to/installed/dependencies
```

Upload the ZIP file to your Lambda function through the AWS Management Console or using the AWS CLI.

Configure the trigger and set up the necessary permissions.

Notes
Ensure that the Lambda function has sufficient permissions to access other AWS services if required.
This function currently extracts text from all pages of the PDF. You can modify it to suit your specific requirements, such as extracting text from specific pages or implementing additional processing logic.
