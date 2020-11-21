from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.contrib.auth import login
from django.contrib.auth.models import User
import os

class ListCarrinhoView(TestCase):
    #foi retornado uma reposta http
    # o primeiro endereço é onde está o user, o segundo é pra onde é redirecionado
    def test_not_Signin(self):
        response = self.client.get('/carrinho', follow= True) 
        self.assertRedirects(response, '/entrar')

class Logado(TestCase):   
               
    def setUp(self) -> None:
        self.client = Client()
       
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        logged_in = self.client.login(username='testuser', password='12345')

        self.path = os.path.join('index_carrinho.html')

        response = self.client.post('/busca', data={
                                'adicionar': True,
                                'symbol': 'CIEL3',
                                'name': 'Cielo',
                                'region': 'Br',
                                'currency': 'brl',
                                'open': '3:00',
                                'close': '4:00',
                                'timezone': -3,
                                'market_cap': 3921.2,
                                'price': 32.1,
                                'change_percent': 12.1,
                                'updated_at': '12/01/2020'}, format='json')
    

    def test_GET_logado(self):
        response = self.client.get('/carrinho')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, self.path) 

    def test_POST_investir(self):
        response = self.client.post('/carrinho', data={'investir': 'investir'}, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.path) 

    def test_POST_excluir(self):
        response = self.client.post('/carrinho', data={'excluir': 'excluir'}, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.path) 
