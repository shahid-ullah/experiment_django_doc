from django.test import Client, TestCase

from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="vim", content="vim")
        Post.objects.create(title="python", content="python programming")
        self.client = Client()

    def test_post_title(self):
        vim = Post.objects.get(title="vim")
        python = Post.objects.get(title="python")
        self.assertEqual(vim.title, 'vim')
        self.assertEqual(vim.content, 'vim')
        self.assertEqual(python.title, 'python')
        self.assertEqual(python.content, 'python programming')

        self.assertIsInstance('abc', str)

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
