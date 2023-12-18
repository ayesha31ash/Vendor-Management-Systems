# vendor_management/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor
from .serializers import VendorSerializer

class VendorAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vendor_url = reverse('vendor-list')

        # Create sample vendor data for testing
        self.vendor_data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact info',
            'address': 'Vendor Address',
            'vendor_code': 'ABC123',
        }
        Vendor.objects.create(**self.vendor_data)

    def test_list_vendors(self):
        response = self.client.get(self.vendor_url)
        vendors = Vendor.objects.all()
        serializer_data = VendorSerializer(vendors, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'vendors': serializer_data})
