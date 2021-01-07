import pytest
from forumMessages.models import Message, Category
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone

user = User(username='johndoe', password='secret')
testMessage1 = Message.addMessage(user=user, text="Lorem ipsum dolor sit amet", categories=None)
# Created a global variable testMessage1 - in order to add it in 1 func and delete it in another func


@pytest.mark.django_db
class TestMessages:


    def test_addCategory(cls):
        Category.addCategory("TestCat")
        testCat = Category.objects.get(name="TestCat")
        assert testCat.name == "TestCat"
        # testCat will be deleted after the final test is performed


    def test_getCategories(cls):
        allCat = Category.getCategories()
        assert isinstance(allCat, QuerySet)  # Check if the list of categories is OK after adding a test category
        assert all(isinstance(cat, Category) for cat in Category)  # Are all instances in Category table are Category


    def test_addMessage(cls):
        testMessage1 = Message.addMessage(user=user, text="Lorem ipsum dolor sit amet", categories=None)
        assert list(testMessage1.values_list('user', 'text', 'categories', 'date')) == [
            user, "Lorem ipsum dolor sit amet", None, timezone.now]


    def test_editMessage(cls):
        testMessage1.editMessage("Some different text")
        assert testMessage1.text == "Some different text"


    def test_deleteMessage(cls):
        testMessage1_ID = testMessage1.id
        Message.deleteMessage(testMessage1_ID)  # Delete the test Message after all tests passed
        # Make sure the instance deleted does not exist anymore
        assert not(isinstance(Message.objects.get(id=testMessage1_ID), Message))
        # No method for category deletion exists (no scenario for deleting a category, by design),
        # so this is done manually in the next line
        Category.objects.get(name="TestCat").delete()  # Delete the test Category after all tests passed
