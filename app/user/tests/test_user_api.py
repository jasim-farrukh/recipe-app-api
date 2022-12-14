"""
Tests for the user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        # Now posting the data to the URL
        res = self.client.post(CREATE_USER_URL, payload)
        # Now adding assertions for what we expect to happen
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)  # check if endpoint returns HTTP 201
        user = get_user_model().objects.get(email=payload['email'])  # check if email matches
        self.assertTrue(user.check_password(payload['password']))  # check if password matches
        # Now making sure password is not returned in response
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        create_user(**payload)
        # Now making the post request
        res = self.client.post(CREATE_USER_URL, payload)  # POST the payload to the endpoint that is being passed
        """Bad Request if the user is trying to create account with existing email"""
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 chars."""
        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # we also check if the user doesn't exist, so it doesn't create the user
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
