from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

class ListCarrinhoView(TestCase):
    #foi retornado uma reposta http
    # o primeiro endereço é onde está o user, o segundo é pra onde é redirecionado
    def test_not_Signin(self):
        response = self.client.get('/carrinho', follow= True) 
        """ self.assertEqual(response.status_code, 302) #302 temporary redirect  """
        self.assertRedirects(response, '/entrar')
    
"""
class registrado(TestCase):

    def from_sign_up_to_sign_in(self):
        response = self.client.get('\registrar', follow= True)
        self.assertRedirects(response, '\entrar')




"""





    
""" class logado(TestCase):
    
    @login_required(login_url='/entrar')
    def secure(self, request):
        user = request.user
        return render(request, '/entrar', {'username': user.username})

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('user', 'plataforma 123')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(username='user', password='plataforma 123')
        response = self.client.get('/entrar', follow=True)
        user = User.objects.get(username='user')
        self.assertEqual(response.context['username'], 'user')

    
    def test_session_is_empty(self):
        self.client.get('/carrinho')
        session = self.client.session
        self.assertEqual(session["acao"], "")
"""

