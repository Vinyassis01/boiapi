import requests
import time 
import subprocess

def inserir_valores_animais_reposicao(arquivo,url):
	print("iniciando o processo para inserir os dadoos no DB")
	headers = {'Content-Type': 'application/json'}
	inicio = "{"
	fim = "}"
	with open(arquivo,'r') as file :
		print(f"abrindo o arquivo : {arquivo}")
		for linha in file :
			time.sleep(2)
			data = linha
			comando = [
    'curl', '-X', 'POST', url,
    '-H', 'Content-Type: application/json',
    '-d', data
    ]
			try:
			    subprocess.run(comando)
			#    requests.post(url=url, headers=headers, data=data)
			#    print(f"ok")
			except Exception as e:
				print(f"houve um erro {e}")

inserir_valores_animais_reposicao(arquivo='valores_gerais_boi_gordo.json',url='http://127.0.0.1:8000/boi_gordo/inserir/')