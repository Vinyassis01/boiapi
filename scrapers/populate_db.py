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

			except Exception as e:
				print(f"houve um erro {e}")

inserir_valores_animais_reposicao(arquivo='valores_gerais.json',url='http://127.0.0.1:8000/reposicao/inserir/')