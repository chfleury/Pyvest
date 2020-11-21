from django.test import Client, TestCase
from django.urls import reverse
from usuario_investimentos import views
from django.contrib.auth import login
from django.contrib.auth.models import User
import os
from carrinho.models import Investimento
class TestInvestimento(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.clientLogado = Client()
       
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        logged_in = self.clientLogado.login(username='testuser', password='12345')
        
        self.investimento = Investimento.objects.create(
            symbol = "ABEV3",
            name = "Ambev S.A.",
            region = "Brazil/Sao Paolo",
            currency = "BRL",
            timeOpen = "10:00",
            timeClose = "17:30",
            timeZone = "-3",
            marketCap = 241055.0,
            price = 15.16,
            changePercent =-1.3,
            data = "2020-11-17 11:08:03",
            userId = user.id,
        )

    def test_GET(self):
        response = self.client.get('/busca', follow= True) 
        self.assertRedirects(response, '/entrar')

    def test_GET_logado(self):        
        response = self.clientLogado.get('/meus_investimentos/')

        self.assertEquals(response.status_code, 200)
        path = os.path.join('investimentos_do_usuario.html')

        self.assertTemplateUsed(response, path) 

    def test_POST_clicar(self):
        response = self.clientLogado.post(
            '/meus_investimentos/', 
            data={'symbol': 'ABEV3', 'name': 'Ambev S.A.'}, 
            format='json',
            follow= True)

        path = os.path.join('base_chart.html')

        self.assertTemplateUsed(response, path) 
        
    def test_POST_excluir(self):
        response = self.clientLogado.post(
            '/meus_investimentos/', 
            data={'id': self.investimento.id}, 
            format='json',
            follow= True)

        self.assertEquals(response.status_code, 200)
        path = os.path.join('investimentos_do_usuario.html')

        self.assertTemplateUsed(response, path) 
               