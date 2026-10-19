from django.test import TestCase
from django.urls import reverse

from .models import ContactEnquiry, Product, Project


class ProvisionApiTests(TestCase):
    def test_products_endpoint_returns_json(self):
        Product.objects.create(
            name='Sliding Window',
            category='Sliding Windows',
            description='Modern aluminium sliding window.',
        )

        response = self.client.get(reverse('products-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['name'], 'Sliding Window')

    def test_projects_endpoint_returns_json(self):
        Project.objects.create(
            title='Harbor Residence',
            location='Dubai',
            category='Residential',
            description='A premium glass façade project.',
        )

        response = self.client.get(reverse('projects-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['title'], 'Harbor Residence')

    def test_contact_endpoint_creates_enquiry(self):
        response = self.client.post(
            reverse('contact-create'),
            {
                'name': 'Client Name',
                'email': 'client@example.com',
                'phone': '+971500000000',
                'subject': 'Quote request',
                'message': 'We would like a consultation.',
            },
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactEnquiry.objects.count(), 1)
