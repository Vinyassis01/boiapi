import requests
import time 
import subprocess
import asyncio
import datetime

async def inserir_valores_animais(arquivo,url):
	print("iniciando o processo para inserir os dadoos no DB")
	headers = {'Content-Type': 'application/json'}
	inicio = "{"
	fim = "}"
	with open(arquivo,'r') as file :
		print(f"abrindo o arquivo : {arquivo}")
		for linha in file :
			time.sleep(1)
			data = linha
			comando = [
    'curl', '-X', 'POST', url,
    '-H', 'Content-Type: application/json',
    '-d', data
    ]
			try:
			    subprocess.run(comando)

			except Exception as e:
				print(f"houve um erro {e}")

# inserir_valores_animais(arquivo='valores_gerais.json',url='http://127.0.0.1:8000/reposicao/inserir/')

async def main():
    url_reposicao = 'http://127.0.0.1:8000/reposicao/inserir/'
    url_boi_gordo = 'http://127.0.0.1:8000/boi_gordo/inserir/'
    
    # Executa ambas as funções ao mesmo tempo
    await asyncio.gather(
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-02-27.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-02-28.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-03-01.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-03-02.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-03-03.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-03-04.json',url=url_boi_gordo),
        inserir_valores_animais(arquivo='valores_gerais_boi_gordo_2026-03-05.json',url=url_boi_gordo),

        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-02-27.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-02-28.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-03-01.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-03-02.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-03-03.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-03-04.json',url=url_reposicao),
        inserir_valores_animais(arquivo='valores_gerais_reposicao_2026-03-05.json',url=url_reposicao),
    )

if __name__ == "__main__":
    asyncio.run(main())

