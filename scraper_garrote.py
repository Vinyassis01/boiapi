from bs4 import BeautifulSoup
import requests
import datetime
url = 'https://www.scotconsultoria.com.br/cotacoes/reposicao/'
headers ='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'
def page (url,headers):
    response = requests.get(url,headers)
    page_content = response.content
    soap = BeautifulSoup(page_content,'html.parser')
    return soap

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

def femea_nelore (soap):
    femea_nelorada = soap.find_all('tr',class_="conteudo")[28:41]
    date = datetime.date.today()
    abertura = '{'
    fechamento = '}'
#    with open(f'vaca boiadeira @ {datetime.date.today()}','w')as json:
#        for vaca_boiadeira in femea_nelorada:
#            estado = vaca_boiadeira.get_text()[1:4]
#            valor = int(vaca_boiadeira.get_text()[6:11])
#            arroba = valor/11
#            json.write(f"""{abertura}
#"date":"{date}",
#"animal":"vaca boideira",
#"arroba":"{arroba:.2f}",
#"estado":"{estado}",
#"regiao":"{estado}"
#{fechamento}
#,""")
#    json.close()

#    with open(f'novilha @ {datetime.date.today()}','w')as json:
#        for novilha in femea_nelorada:
#            estado = novilha.get_text()[1:4]
#            valor = novilha.get_text()[31:37]
#            valores = float(valor.replace(',','.'))
#            arroba = valores/9
#            json.write(f"""{abertura}
#"date":"{date}",
#"animal":"novilha",
#"arroba":"{arroba:.2f}",
#"estado":"{estado}",
#"regiao":"{estado}"
#{fechamento}
#,""")
#    json.close()

    with open(f'bezerra 7@ {datetime.date.today()}','w')as json:
        for bezerra in femea_nelorada:
            estado = bezerra.get_text()[1:4]
            valor = bezerra.get_text()[55:63]
            valores = float(valor.replace(',','.'))
            arroba = valores/7
            json.write(f"""{abertura}
"date":"{date}",
"animal":"novilha",
"arroba":"{arroba:.2f}",
"estado":"{estado}",
"regiao":"{estado}"
{fechamento}
,""")
    json.close()

#pagina = page(url,headers) 
femea_nelore(soap=page(url,headers))
macho_nelore(soap=page(url,headers))
