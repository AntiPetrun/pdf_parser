from django.urls import path
from .views import view_txt_files, view_pdf_file, view_locally_upload_file


urlpatterns = [
    path('view_txt_files/', view_txt_files, name='view_txt_files'),
    path('view_pdf_file/', view_pdf_file, name='view_pdf_file'),
    path('view_locally_upload_file/', view_locally_upload_file, name='view_locally_upload_file'),
]
