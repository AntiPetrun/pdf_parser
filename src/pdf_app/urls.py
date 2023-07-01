from django.urls import path
from .views import PDFParseView


urlpatterns = [
    path('parse-pdf/', PDFParseView.as_view(), name='parse_pdf'),
]
