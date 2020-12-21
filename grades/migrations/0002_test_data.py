from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from django.contrib.auth.models import User
        from grades.models import Grade, Course

        user1 = User.objects.create_user(username="ido", password="123456")
        course1 = Course.objects.create(course_name="course1", credinitials="3")
        course2 = Course.objects.create(course_name="course2", credinitials="2")
        test_data = [
            (user1, course1, 85, 'A', 2021),
            (user1, course2, 60, 'B', 2020),
            (user1, course1, 20, 'C', 2020),
        ]

        with transaction.atomic():
            for user, course, grade, semester, year in test_data:
                Grade(user=user, course=course, grade=grade, semester=semester, year=year).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
