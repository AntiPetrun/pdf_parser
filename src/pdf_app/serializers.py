from rest_framework import serializers


class PDFParseSerializer(serializers.Serializer):
    file = serializers.FileField()
