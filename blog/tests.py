from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class AppTest(TestCase):
    def test_home_status_code(self):
        expected = 200
        url = reverse('blog_home')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_list_blog_status_code(self):
        expected = 200
        url = reverse('blog_list')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_post_detail_status_code(self):
        expected = 404
        url = reverse("blog_detail",args=(1,))
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected , actual)

    def test_home_page_template(self):
        url = reverse('blog_home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response , actual)

    def test_list_blog_page_template(self):
        url = reverse('blog_list')
        response = self.client.get(url)
        actual = 'list_blog.html'
        self.assertTemplateUsed(response , actual)


