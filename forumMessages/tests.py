import pytest
from django.test import TestCase
from forumMessages.models import Message, Category
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from grades.models import Course

@pytest.mark.django_db
class TestMessages:

    def test_addCategory(cls):
        Category.addCategory("TestCat")
        testCat = Category.objects.get(name="TestCat")
        assert testCat.name == "TestCat"

    def test_getCategories(cls):
        allCat = Category.getCategories()
        assert isinstance(allCat, QuerySet) # Check if the list of categories is OK after adding a test category
        assert all(isinstance(cat, Category) for cat in Category) # Check if all the instances in Category table are of type Category
        Message.objects.get(name="TestCat").delete() # Delete the test Category after all tests passed
        # No method for category deletion exists (no scenario for deleting a category, by design), so this is done manually in the above line
