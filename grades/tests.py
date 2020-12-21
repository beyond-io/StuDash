import pytest
from grades.models import Grade, Course
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestGrade:
    def test_addGradeUserCourse(cls):
        user3 = User.objects.create_user(username="idan", password="123456")
        c = Course.addCourse(course_name="NLP", credinitials="3")
        Grade.addGradeUserCourse(user3, c, 90, 'A', 2021)
        out = Grade.objects.filter(semester='A')
        assert list(out.values_list('user', 'course', 'grade', 'semester', 'year')) == [
            (1, 1, 85, 'A', 2021),
            (2, 3, 90, 'A', 2021)
        ]

    def test_removeGrade(cls):
        user3 = User.objects.create_user(username="idan", password="123456")
        c = Course.addCourse(course_name="NLP", credinitials="3")
        Grade.addGradeUserCourse(user3, c, 50, 'B', 2020)
        Grade.removeGrade(2)
        out = Grade.objects.all()
        assert list(out.values_list('user', 'course', 'grade', 'semester', 'year')) == [
            (1, 1, 85, 'A', 2021),
            (1, 1, 20, 'C', 2020),
            (2, 3, 50, 'B', 2020),
        ]


@pytest.mark.django_db
class TestCourse:
    def test_addCourse(cls):
        Course.addCourse(course_name="java", credinitials="3")
        out = Course.objects.filter(credinitials='3')
        assert list(out.values_list('course_name', 'credinitials')) == [
            ('course1', 3),
            ('java', 3),
        ]

    def test_removeCourse(cls):
        Course.addCourse(course_name="java", credinitials="3")
        Course.removeCourse(3)
        out = Course.objects.all()
        assert list(out.values_list('course_name', 'credinitials')) == [
            ('course1', 3),
            ('course2', 2),
        ]
