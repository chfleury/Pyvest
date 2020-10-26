from django.shortcuts import render

# criar uma linked list pros investimentos
# criar um botão para cada investimento com o código e o nome de cada um
# usar a API pra pegar o dado do dia daquele investimento

investimentos_do_usuario = []

def requisicao(symbol, key, nome_do_campo):

    url = f'https://api.hgbrasil.com/finance/stock_price?&key={key}&symbol={symbol}&fields={nome_do_campo}'

    dados = requests.get(url)

    resposta_geral = dados.json()
    somente_resultados = resposta_geral["results"]
    valor_do_campo_desejado = somente_resultados["PETR4"]

    return valor_do_campo_desejado



def meus_investimentos(request):

    






    return render(request, 'investimentos_do_usuario.html', {})