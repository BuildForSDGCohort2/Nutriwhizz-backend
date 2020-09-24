from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
from .models import Category, Profile


class ModelTestCase(TestCase):
    """This class defines the test suite for Category model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.category_name = "Movie"
        self.category = Category(name=self.category_name)

    def test_model_can_create_a_categories_list(self):
        """Test the category model can create a category."""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

class PropfileTest(TestCase):
    """ Test module for Profile model """

    def setUp(self):
        Profile.objects.create(
            name='Patrick', email= 'Patrick@gmail.com', alias='Big Boss', category = 'Movie' , super_power= 'Fire', rating = 5)
        

    def test_profile_email(self):
        profile_patrick = Puppy.objects.get(name='Patrick')
        self.assertEqual(
            puppy_casper.get_email(), "Patrick emails is Patrick@gmail.com")
        


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Movie'}
        self.response = self.client.post(
            reverse('create'),
            self.category_data,
            format="json")

    def test_api_can_create_a_category(self):
        """Test the api has category creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)