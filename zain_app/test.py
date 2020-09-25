from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Users
from django.urls import reverse

class UsersTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='yazan',
            email='yazan@gmail.com',
            password='password'
        )

        self.users = Users.objects.create(
            title='banana',
            author='aaaaa',
            body='ccccc'
        )

    def test_users_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        response = self.client.get(reverse('users_create'))
        self.assertEqual(response.status_code, 200)

    def test_snack_list_view(self):
        response = self.client.get(reverse('users_details',args='1'))
        self.assertEqual(response.status_code, 200)


    def test_delete_view(self):
        response = self.client.get(reverse('user_delete',args='1'))
        self.assertEqual(response.status_code, 200)


    def test_edit_view(self):
        response = self.client.get(reverse('users_edit',args='1'))
        self.assertEqual(response.status_code, 200)



