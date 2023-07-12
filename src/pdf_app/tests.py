from django.test import TestCase, Client
from django.urls import reverse


class TestPDFParsingEndpoint(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('parse-pdf')

    def test_pdf_parsing_endpoint(self):
        # Create a PDF file object
        pdf_file = open('media/file.pdf', 'rb')
        # Make a POST request to the endpoint with the PDF file
        response = self.client.post(self.url, {'pdf_file': pdf_file})
        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the expected data
        expected_data = {'parsed_data': 'expected data'}
        self.assertEqual(response.json(), expected_data)
