from bs4 import BeautifulSoup
import aiohttp
import datetime
import asyncio

async def macho_nelore(url,headers):
  async with aiohttp.ClientSession() as session:
    async with session.get(url,headers=headers) as response:
      html = await response.text()
      soup = BeautifulSoup(html,'html.parser')
      macho_anelorado = soup.find_all('tr',class_="conteudo")[:13]
      with open (f'macho nelore @ {datetime.date.today()}.json','w') as json:
        for macho in macho_anelorado:
          dados_brutos = macho.get_text()
          dados_limpos = " ".join(dados_brutos.split())
          json.write(dados_limpos +'\n')
        json.close()


async def femea_nelore(url,headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            html = await response.text()
            soup = BeautifulSoup(html,'html.parser')
            femea_nelorada = soup.find_all('tr',class_="conteudo")[28:41]
            with open (f'femea nelore @ {datetime.date.today()}.json','w') as json:
                for femea in femea_nelorada:
                    dados_brutos = femea.get_text()
                    dados_limpos = " ".join(dados_brutos.split())
                    json.write(dados_limpos +'\n')
                json.close()

async def boi_gordo(url,headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            html = await response.text()
            soup = BeautifulSoup(html,'html.parser')
            boi_gordo = soup.find_all('tr','td',class_="conteudo")[12:]
            with open (f'boi gordo @ {datetime.date.today()}.json','w') as json:
                for boi in boi_gordo:
                    dados_brutos = boi.get_text()
                    dados_limpos = " ".join(dados_brutos.split())
                    json.write(dados_limpos +'\n')
                json.close()

async def main():
    url_reposicao = "https://www.scotconsultoria.com.br/cotacoes/reposicao/"
    url_boi_gordo = "https://www.scotconsultoria.com.br/cotacoes/boi-gordo/"
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0"}
    # Executa ambas as funções ao mesmo tempo
    await asyncio.gather(
        macho_nelore(url=url_reposicao,headers=headers),
        femea_nelore(url=url_reposicao,headers=headers),
        boi_gordo(url=url_boi_gordo,headers=headers)
    )

if __name__ == "__main__":
    asyncio.run(main())
