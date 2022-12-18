"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core.models import Recipe


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email(self):
        """Test creating a user with an email is successful."""
        email = 'jasim'
        password = 'admin321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized for new users."""
        """
            Normalization is organizing your data in database
            i want to convert the first one of the following in to their respective second ones
        """
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises an Error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','admin321')

    def test_create_super_user(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'jasimfarrukh61@gmail.com',
            'admin321'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test create a recipe is successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description.',
        )
        self.assertEqual(str(recipe), recipe.title)     # checking String representation of recipe title

