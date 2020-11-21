from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from entrar_registrar import views

class TestRegistrar(TestCase):
    def setUp(self) -> None:
        self.username = 'user'
        self.password = 'plataforma123'

    def test_registrar_form(self):
        response = self.client.post(reverse(views.registrar), data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


#python3 manage.py test catalog.tests.test_models.YourTestClass.test_one_plus_one_equals_two