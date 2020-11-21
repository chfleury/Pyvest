from django.test import TestCase
from carrinho.models import Investimento

# Create your tests here.
class InvestimentoTestCase(TestCase):
    def setUp(self):
        Investimento.objects.create(
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
            userId = 0,
        )
    def test_return_str(self):
        Inv1 = Investimento.objects.get(name = "Ambev S.A.")
        self.assertEqual(Inv1.__str__(), ["Ambev S.A.","ABEV3"])

""" [{'symbol': 'ABEV3', 'name': 'Ambev S.A.', 'region': 'Brazil/Sao Paolo', 'currency': 'BRL', 'time_open': '10:00', 'time_close': '17:30', 'timezone': '-3', 'market_cap': '241055.0', 'price': '15.16', 'change_percent': '-1.3', 'updated_at': '2020-11-17 11:08:03'}]
[17/Nov/2020 14:44:38] "POST /busca HTTP/1.1" 200 7982 """