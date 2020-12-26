from django.shortcuts import render, redirect
from django.contrib import messages
from grades.models import Grade, Course
from grades.forms import GradeForm


def Create_grade(request):
    grades = Grade.objects.filter(user=request.user)
    courses = Course.objects.all()
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.course = form.cleaned_data['course']
            obj.grade = form.cleaned_data['grade']
            obj.semester = form.cleaned_data['semester']
            obj.year = form.cleaned_data['year']
            obj.save()
            messages.success(request, "Grade saved successfully")
            return redirect('grades')
    else:
        form = GradeForm()
        GPA = calculateGPA(grades, courses)
    return render(request, 'grades/grades.html', {
        'grades': grades,
        'form': form,
        'GPA': GPA,
    })


def calculateGPA(grades, courses):
    sum = 0
    count = 0
    for grade in grades:
        for course in courses:
            cred = grade.course.credinitials
        sum += grade.grade * cred
        count += cred
    return(sum/count)
