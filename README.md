# 🚀 boi API

> A boi api tem a finalidade de disponibilizar dados referentes aos precos dos animais
> mais relevantes para a pecuaria e o produtor , a boi API coleta, limpa e trata dados e os
> disponibiliza de forma clara ,acessivel e com filtros avancados para valores e refencias a datas
> e animais em todos os estados do pais

---

## 💻 Sobre o Projeto
A boiAPI tem a finalidade de fornecer dados para decisoes de negocio de forma clara e que 
possa ser integrada aos programas e softwares ja usados pelo produtor , em um unico lugar
e com opcoes avancadas e dados gerais 

## 🛠 Tecnologias
As ferramentas utilizadas :
* Django
* Django-rest-framework
* Beautiful Soup
* Python
* Asyncio

## 🚀 Como Executar
Siga os passos abaixo para rodar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com

2. Instale as dependencias
  ```bash
  pip install django-rest-framework
```
```bash
  pip install django-fillter
```
```bash
  pip install django-rest-framework-simple-jwt
```
3. Rode as migrations do banco de dados
```bash
  python3 manage.py make migrations
```
```bash
  python3 manage.py migrate
```
4. Rode a acesse o servidor
```bash
  python3 manage.py runserver
```
```bash
  http://localhost:8000/
```
5. Gere um token de acesso
```bash
  http://localhost:8000/token
```
6. Navegue pela home e encontre  os endpoints
  > vc pode encontrar todos os endpoints e os exemplos de como acessa-los
