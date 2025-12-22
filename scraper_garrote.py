from bs4 import BeautifulSoup
import requests
import datetime

url = 'https://www.scotconsultoria.com.br/cotacoes/reposicao/'
headers ='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'
response = requests.get(url,headers)
page_content = response.content
soap = BeautifulSoup(page_content,'html.parser')

def macho_nelore(soap):
    # ok
    macho_anelorado = soap.find_all('tr',class_="conteudo")[:13]
    date = datetime.date.today()
    abertura = '{'
    fechamento = '}'
    with open (f'boi magro nelorado @ {datetime.date.today()}.json','w') as json:
        for boi_magro in macho_anelorado:
            estado = boi_magro.get_text()[1:4]
            valor  = int(boi_magro.get_text()[5:11])
            arroba = valor/12.5
            json.write(f"""{abertura}
"date":"{date}",
"animal":"boi magro nelorado",
"arroba":"{arroba}",
"estado":"{estado}",
"regiao":"{estado}"
{fechamento}
,""")
    json.close()
   # ok
    with open (f'garrote nelorado @ {datetime.date.today()}.json','w') as json:
        for garrote in macho_anelorado:
            estado = garrote.get_text()[1:4]
            valor =  garrote.get_text()[32:37]
            try:
                arroba = int(valor)/10
            except:
                arroba =  garrote.get_text()[32:35]
            json.write(f"""{abertura}
"date":"{date}",
"animal":"garrote nelorado",
"arroba":"{arroba}",
"estado":"{estado}",
"regiao":"{estado}"
{fechamento}
,
""")
    json.close()

    # ok
    with open (f'bezerro nelorado @ {datetime.date.today()}.json','w') as json:
        for bezerro in macho_anelorado:
            estado = bezerro.get_text()[1:4]
            valor = bezerro.get_text()[59:63]
            try:
                arroba = int(valor)/10
            except:
                arroba =  bezerro.get_text()[59:62]
            json.write(f"""{abertura}
"date":"{date}",
"animal":"garrote nelorado",
"arroba":"{arroba}",
"estado":"{estado}",
"regiao":"{estado}"
{fechamento}
,
""")
    json.close()

    # ok
    with open (f'bezerro desmamado nelorado @ {datetime.date.today()}.json','w') as json:
        for bezerro_desmamado in macho_anelorado:
            estado = bezerro_desmamado.get_text()[1:4]
            try: 
                valor = int(bezerro_desmamado.get_text()[82:89])
                arroba = valor/6.5
            except:
                valor = bezerro_desmamado.get_text()[82:87]
                valor_animal = valor+'0'
                if len(valor_animal) >= 4:
                    arroba = int(valor_animal)/60.5
                else:
                    arroba = int(valor_animal)/6.5
            json.write(f"""{abertura}
"date":"{date}",
"animal":"bezerro desmamado",
"arroba":"{arroba:.2f}",
"estado":"{estado}",
"regiao":"{estado}"
{fechamento}
,
""")
    json.close()

macho_nelore(soap=soap)