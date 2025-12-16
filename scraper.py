from bs4 import BeautifulSoup
import requests
from bs4 import AttributeResemblesVariableWarning
import warnings
import re
import datetime
warnings.filterwarnings("ignore", category=AttributeResemblesVariableWarning)

url  ='https://www.scotconsultoria.com.br/cotacoes/boi-gordo/'
headers ='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'

def get_page(url,headers):
    page = requests.get(url,headers)
    page_content = page.content
    soap = BeautifulSoup(page_content,'html.parser')
    table = soap.find_all('tr','td',class_="conteudo")[12:]
    return table

dados = get_page(url=url,headers=headers)
with open(f'valores @ {datetime.date.today()}.json','w') as json:
    for item in dados :
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
