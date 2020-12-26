from django.db import models
from django.conf import settings
# Each user can add, modify or remove course from is list
# Each course contains coures id(default by Django), name, credinitials and grade


class Course (models.Model):
    course_name = models.CharField(max_length=50)
    credinitials = models.IntegerField(default=2)

    def __str__(self):
        return self.course_name

    @classmethod
    def addCourse(cls, course_name, credinitials):
        newCourse = Course()
        newCourse.course_name = course_name
        newCourse.credinitials = credinitials
        newCourse.save()
        return newCourse

    @classmethod
    def removeCourse(cls, courseID):
        Course.objects.filter(id=courseID).delete()
        pass


class Semester(models.TextChoices):
    Winter = 'A',
    Spring = 'B',
    Summer = 'C'


class Grade(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    grade = models.IntegerField(default=0)
    semester = models.CharField(max_length=1, choices=Semester.choices)
    year = models.IntegerField(default=0)

    @classmethod
    def addGradeUserCourse(cls, user, courseID, grade, semester, year):
        newGrade = Grade()
        newGrade.user = user
        newGrade.course = courseID
        newGrade.grade = grade
        newGrade.semester = semester
        newGrade.year = year
        newGrade.save()
        return newGrade

    @classmethod
    def removeGrade(cls, gradeID):
        Grade.objects.filter(id=gradeID).delete()
        pass
