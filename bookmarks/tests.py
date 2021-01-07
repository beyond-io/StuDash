import pytest
from django.db.models.query import QuerySet
from bookmarks.models import Bookmark
from django.contrib.auth.models import User
from grades.models import Course
from django.urls import reverse
from django.test import TestCase, Client


@pytest.mark.django_db
class TestBookmark:
    def test_course_feed(cls):
        '''
        this function tests the bookmarks displayed on the course page
        '''
        out = Bookmark.course_feed()
        assert isinstance(out, QuerySet)
        assert all(isinstance(b, Bookmark) for b in out)
        assert list(out.values_list('course', 'url', 'urlname')) == [
            (2, 'https://www.facebook.com', 'Facebook'),
            (2, 'https://www.facebook.com', 'Facebook'),
            (1, 'https://www.ynet.co.il', 'Ynet'),
            (1, 'https://www.google.com', 'Google'),
        ]

    def test_add_bookmark(cls):
        user = User(username='john', password='johnpassword')
        user.save()
        course = Course(user=user, course_name="intro 101", credinitials="3")
        course.save()
        Bookmark.add_bookmark(course, 'https://www.youtube.com', 'Youtube')
        new = Bookmark.objects.filter(urlname='Youtube')
        assert list(new.values_list('course', 'url', 'urlname')) == [
            (3, 'https://www.youtube.com', 'Youtube'),
        ]

    def test_remove_bookmark(cls):
        bm = Bookmark.objects.get(pk=1)
        Bookmark.remove_bookmark(bm)
        new = Bookmark.objects.all()
        assert list(new.values_list('course', 'url', 'urlname')) == [
            (1, 'https://www.ynet.co.il', 'Ynet'),
            (2, 'https://www.facebook.com', 'Facebook'),
            (2, 'https://www.facebook.com', 'Facebook')
        ]


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('bookmarks:create')

    def test_bookmarks_list_for_user(self):
        '''test if bookmarks list belongs to current user'''
        user_login = self.client.login(username='Ido', password='123456')
        response = self.client.get(self.create_url)
        assert (b'https://www.ynet.co.il') in response.content
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'bookmarks/bookmarks.html')
