# Tests for models pages
from django.test import TestCase
from django.contrib.auth import get_user_model

from decimal import Decimal

from core import models



def create_user(email='user@example.com', password='testpass123'):
    """Create and Return a new user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'test1234'
        # username = 'test'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            # username=username,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['test3@ExAMplE.COM', 'test3@example.com'],
            ['TEST4@EXAMPLE.COM', 'TEST4@example.com'],
            ['test5@example.COM', 'test5@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test1234')

    def test_create_superuser(self):
        """Test Creating Superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test1234',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='TestTag1')

        self.assertEqual(str(tag), tag.name)
