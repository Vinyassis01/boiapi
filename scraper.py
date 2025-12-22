from bs4 import BeautifulSoup
import requests
from bs4 import AttributeResemblesVariableWarning
import warnings
import re
import datetime
warnings.filterwarnings("ignore", category=AttributeResemblesVariableWarning)

headers ='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'

# boi gordo
url_boi  ='https://www.scotconsultoria.com.br/cotacoes/boi-gordo/'

# garrote /reposicao
url_garrote = 'https://www.scotconsultoria.com.br/cotacoes/reposicao/'

# bezerro
url_bezerro = 'https://www.noticiasagricolas.com.br/cotacoes/boi-gordo/macho-nelore-bezerro-12-meses'

# vaca gorda
url_vaca_gorda = 'https://www.scotconsultoria.com.br/cotacoes/vaca-gorda/%3Fref%3Dfoo'

def get_page_boi(url,headers):
    page = requests.get(url,headers)
    page_content = page.content
    soap = BeautifulSoup(page_content,'html.parser')
    table = soap.find_all('tr','td',class_="conteudo")[12:]
    return table

dados_boi = get_page_boi(url=url_boi,headers=headers)
with open(f'valores @ {datetime.date.today()}.json','w') as json:
    for item in dados_boi :
        valor = item.get_text()
        padrao = r"\s(\S+)\s"
        dados = re.findall(padrao,valor)
#        valores_arroba = "".join(dados)
        abertura = '{'
        fechamento = '}'
        if len(dados) == 7 :
            json.write(f"""
{abertura}
"date":"{datetime.date.today()}",
"animal":"boi",
"arroba":"{dados[2]}",
"estado":"{dados[0]}",
"regiao":"{dados[1]}"
{fechamento},
""")
        elif len(dados) == 6 :
            json.write(f"""
{abertura}
"date":"{datetime.date.today()}",
"animal":"boi",
"arroba":"{dados[1]}",
"estado":"{dados[0]}",
"regiao":""
{fechamento},
""")
    json.close()

# garrote
def get_page_garrote(url,headers):
    page = requests.get(url,headers)
    page_content = page.content
    soap = BeautifulSoup(page_content,'html.parser')
# implementar o parser da pagina
    pass

dados_garrote = get_page_garrote(url=url_garrote,headers=headers)
with open (f'valores @ garrote {datetime.date.today()}') as json:
    for item in dados_garrote :
        abertura = '{'
        fechamento = '}'
        json.write(f"""
{abertura}
"date":"{datetime.date.today()}",
"animal":"boi",
"arroba":"{dados[2]}",
"estado":"{dados[0]}",
"regiao":"{dados[1]}"
{fechamento},
""")
        json.close()

# bezerro
def get_page_bezerro(url,headers):
    page = requests.get(url,headers)
    page_content = page.content
    soap = BeautifulSoup(page_content,'html.parser')
# implementar o parser da pagina
    pass

dados_bezerro = get_page_bezerro(url=url_bezerro,headers=headers)
with open (f'valores @ bezerro {datetime.date.today()}') as json :
    for item in dados_bezerro :
        abertura = '{'
        fechamento = '}'
        json.write(f"""
{abertura}
"date":"{datetime.date.today()}",
"animal":"boi",
"arroba":"{dados[2]}",
"estado":"{dados[0]}",
"regiao":"{dados[1]}"
{fechamento},
""")
        json.close()      

# garrote
def get_page_vaca_gorda(url,headers):
    page = requests.get(url,headers)
    page_content = page.content
    soap = BeautifulSoup(page_content,'html.parser')
# implementar o parser da pagina
    pass

dados_vacas_gorda = get_page_vaca_gorda(url=url_vaca_gorda,headers=headers)
with open (f'valores @ vaca gorda {datetime.date.today()}') as json :
    for item in dados_vacas_gorda :
        abertura = '{'
        fechamento = '}'
        json.write(f"""
{abertura}
"date":"{datetime.date.today()}",
"animal":"boi",
"arroba":"{dados[2]}",
"estado":"{dados[0]}",
"regiao":"{dados[1]}"
{fechamento},
""")
        json.close()
        