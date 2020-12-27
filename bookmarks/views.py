from django.shortcuts import render
from django.contrib import messages
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm
from grades.models import Course
from django.contrib.auth.models import User

# @login_required
def AddBookmarks(request):
    bookmarks = Bookmark.objects.all().order_by('-last_view_date')
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            new_bookmark = Bookmark()
            new_bookmark.course = Course.objects.get(id=1)
            new_bookmark.user = User.objects.get(id=1)
            new_bookmark.save()
            messages.success(request, "Bookmark saved successfully")
            return render(request, 'bookmarks/bookmarks.html',
                          {'bookmarks_list': bookmarks})
        '''
        Function for testing,
        will be added once the testing PR will be merged
        bookmarks = Bookmark.course_feed()
        '''
    else:
        return render(request, 'bookmarks/bookmarks.html',  {'bookmarks_list': bookmarks})
