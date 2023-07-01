from rest_framework import serializers


class PDFParseSerializer(serializers.Serializer):
    pdf_file = serializers.FileField()
