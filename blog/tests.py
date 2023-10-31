from django.test import TestCase
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.utils import timezone
from django.contrib.auth.models import User


# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        self.user, _ = User.objects.get_or_create(username='uzytkownik1')
        # Tworzenie posta przypisanego do autora
        self.post = Post.objects.create(title='Test Post', content='This is a test post.',
                                        author=self.user,
                                        created_at=timezone.now())

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_add_comment_view(self):
        form_data = {'content': 'This is a test comment.'}
        self.client.force_login(self.user)
        response = self.client.post(reverse('add_comment', args=[self.post.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Oczekujemy przekierowania po dodaniu komentarza

    def test_comment_form(self):
        self.client.force_login(self.user)
        form = CommentForm(data={'content': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_comment_model(self):
        self.client.force_login(self.user)
        comment = Comment.objects.create(post=self.post, content='This is a test comment.', author=self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, 'This is a test comment.')

