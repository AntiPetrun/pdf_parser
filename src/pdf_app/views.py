from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .pdf_parser import parse_pdf


@csrf_exempt
def view_txt_files(request):
    """
    Send a request with txt file in body to the server to retrieve the content of the file
    :param request: POST request
    :body: txt file
    :return: JSON serialization ->'str'
    """
    if request.method == 'POST':
        file = request.FILES['file']  # Text File.txt <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        content = file.read().decode('utf-8')  # human readable content
        serialized_content = json.dumps(content)  # JSON serialization ->'str'
        return HttpResponse(serialized_content)
    else:
        return HttpResponse('Invalid request method')


@csrf_exempt
def view_pdf_file(request):
    """
    Send a request with pdf file in body to the server to retrieve the pdf file as it is
    :param request: POST request
    :body: pdf file
    :return: PDF file
    """
    if request.method == 'POST':
        file = request.FILES['file']
        content = file.read()
        response = HttpResponse(content, content_type='application/pdf')
        print(response)
        response['Content-Disposition'] = 'attachment; filename="file.pdf"'
        print(response.items())
        return response
    else:
        return HttpResponse('Invalid request method')


@csrf_exempt
def view_locally_upload_file(request, *args, **kwargs):
    """
    Send a request to the server to retrieve the content of a pdf file
    :param request: POST request
    :body: none
    :return: content of a pdf file
    """
    if request.method == 'POST':  # <- sent your path to the file here below
        file_path = '/path/to/file.pdf'
        text = parse_pdf(file_path)
        response = HttpResponse(text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="file.txt"'
        return response
