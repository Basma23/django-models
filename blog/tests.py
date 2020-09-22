from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class BlogTest(TestCase):
    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected, actual)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

    def test_post_detail_page_status_code(self):
        expected = 200
        url = reverse('post_detail')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected, actual)

    def test_post_detail_page_template(self):
        url = reverse('post_detail')
        response = self.client.get(url)
        actual = 'post_detailt.html'
        self.assertTemplateUsed(response, actual)

    def test_postes_page_status_code(self):
        expected = 200
        url = reverse('postes')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected, actual)

    def test_postes_page_template(self):
        url = reverse('postes')
        response = self.client.get(url)
        actual = 'postes.html'
        self.assertTemplateUsed(response, actual)