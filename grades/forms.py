from django import forms
from grades.models import Grade, Course


# Create the form class
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('course', 'grade', 'semester', 'year')
        course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None)
