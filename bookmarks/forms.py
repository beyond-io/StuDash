from django import forms
from bookmarks.models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('course', 'url', 'urlname')
        labels = {
            'course': 'Choose Course',
            'url': 'Website Address',
            'urlname': 'Website Name',
        }
