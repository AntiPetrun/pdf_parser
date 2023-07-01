from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PDFParseSerializer
from .pdf_parser import parse_pdf


class PDFParseView(APIView):
    def post(self, request):
        serializer = PDFParseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pdf_file = serializer.validated_data['pdf_file']

        # Assuming you have a 'media' directory in your Django project's root
        file_path = pdf_file.path

        parsed_text = parse_pdf(file_path)

        return Response({'parsed_text': parsed_text})
