from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.object.create(title='Mazvu', text='text of news')

    def test_text_content(self):
        post = Post.object.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'text of news')


class HomePagesView(TestCase):
    def setUp(self):
        Post.object.create(title='Mazvu 2', text='text of news')

    def test_views_urls_exsist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_views_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_views_(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp, 'home.html')