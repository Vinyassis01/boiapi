from bs4 import BeautifulSoup
import requests
url = 'https://www.scotconsultoria.com.br/cotacoes/reposicao/'
headers ='Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'
response = requests.get(url,headers)
page_content = response.content
soap = BeautifulSoup(page_content,'html.parser')
# valores = soap.find_all('table'[2],'tbody'[1],'tr','td')
valores = soap.find_all('tr',class_="conteudo")[:5]
for item in valores:
    print (item.get_text()[:15])