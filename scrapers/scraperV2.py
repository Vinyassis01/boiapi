from bs4 import BeautifulSoup
import datetime
import requests

class Scraper ():
	date = datetime.date.today()
	abertura = '{'
    fechamento = '}'

	def __init__ (self,link,header):
		self.link = link
		self.header = header
		
	def get_page(self,object):
		response = requests.get(url,headers)
    	page_content = response.content
    	soap = BeautifulSoup(page_content,'html.parser')
    	return soap

    def get_data(self,soap):
    	try:
    		femea_nelorada = soap.find_all('tr',class_="conteudo")[28:41]
    		macho_anelorado = soap.find_all('tr',class_="conteudo")[:13]
    		with open (f'valores animais {datetime.date.today()}.json','w') as json:
    	except Exception as e:
    		print("erro ao acessar o conteudo da pagina :{e}")
    	try:
    		for boi_magro in macho_anelorado:
            	estado = boi_magro.get_text()[1:4]
            	valor  = int(boi_magro.get_text()[5:11])
            	arroba = valor/12.5
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")
        except:
        	pass

        try:
        	for garrote in macho_anelorado:
            	estado = garrote.get_text()[1:4]
            	valor =  garrote.get_text()[32:37]
            	try:
            	    arroba = int(valor)/10
            	except:
            	    arroba =  garrote.get_text()[32:35]
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")

        try:
        	for bezerro in macho_anelorado:
            	estado = bezerro.get_text()[1:4]
            	valor = bezerro.get_text()[59:63]
            	try:
                	arroba = int(valor)/10
            	except:
                	arroba =  bezerro.get_text()[59:62]
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")

        except:
        	pass

        try:
        	for bezerro_desmamado in macho_anelorado:
                estado = bezerro_desmamado.get_text()[1:4]
            	try: 
            	    valor = int(bezerro_desmamado.get_text()[82:89])
            	    arroba = valor/6.5
            	except:
            	    valor = bezerro_desmamado.get_text()[82:87]
            	    valor_animal = valor+'0'
            	    if len(valor_animal) >= 4:
            	        valores = float(valor.replace(',','.'))
            	        arroba = int(valores)/60.5
            	    else:
            	        arroba = int(valor_animal)/6.5
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")
        except Exception as e:
        	print(f"erro :{e}")
       
       try:
       		for vaca_boiadeira in femea_nelorada:
            	estado = vaca_boiadeira.get_text()[1:4]
            	valor = int(vaca_boiadeira.get_text()[6:11])
            	arroba = valor/11
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")
       except:
       		pass

       	try:
       		for novilha in femea_nelorada:
            	estado = novilha.get_text()[1:4]
            	valor = novilha.get_text()[31:37]
            	valores = float(valor.replace(',','.'))
            	arroba = valores/9
            	json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")

       	except:
       		pass

       	try:
       		for bezerra in femea_nelorada:
            estado = bezerra.get_text()[1:4]
            valor = bezerra.get_text()[55:63]
            valores = float(valor.replace(',','.'))
            arroba = valores/7
            json.write(f"""{abertura}"date":"{date}","animal":"boi magro nelorado","arroba":"{arroba}","estado":"{estado}","regiao":"{estado}"{fechamento},""")

        except:
        	pass

scrapy=Scraper(link='https://www.scotconsultoria.com.br/cotacoes/reposicao/',headers='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0')
