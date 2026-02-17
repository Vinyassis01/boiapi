import datetime

def format_macho_nelore(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
            # boi magro
            output.write(f'''"estado":"{itens[0]}","animal":"boi magro","valor_animal":"{itens[1]}","relacao_troca()":"{itens[2]}","relacao_troca()":"{itens[3]}","data":"{datetime.date.today()}"\n''')
            # garrote
            output.write(f'''"estado":"{itens[0]}","animal":"garrote","valor_animal":"{itens[4]}","relacao_troca()":"{itens[5]}","relacao_troca()":"{itens[6]}","data":"{datetime.date.today()}"\n''')
            # bezerro
            output.write(f'''"estado":"{itens[0]}","animal":"bezerro","valor_animal":"{itens[7]}","relacao_troca()":"{itens[8]}","relacao_troca()":"{itens[9]}","data":"{datetime.date.today()}"\n''')
            # bezerro desmamado
            output.write(f'''"estado":"{itens[0]}","animal":"bezerro desmamado","valor_animal":"{itens[10]}","relacao_troca()":"{itens[11]}","relacao_troca()":"{itens[12]}","data":"{datetime.date.today()}"\n''')


def format_boi_gordo(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
            if len(itens) == 10:
                output.write(f'''"estado":"{itens[0]}","animal":"boi gordo","regiao":"{itens[1]}{itens[2]}","arroba(a vista)":"{itens[3]}","arroba(30 dias)":"{itens[4]}","variacao":"{itens[5]}","data":"{datetime.date.today()}"\n''')    
            elif len(itens) == 9:
                output.write(f'''"estado":"{itens[0]}","animal":"boi gordo","regiao":"{itens[1]}","arroba(a vista)":"{itens[2]}","arroba(30 dias)":"{itens[3]}","variacao":"{itens[4]}","data":"{datetime.date.today()}"\n''')
            elif len(itens) == 8:
                output.write(f'''"estado":"{itens[0]}","regiao":"","animal":"boi gordo","arroba(a vista)":"{itens[1]}","arroba(30 dias)":"{itens[2]}","variacao":"{itens[3]}","data":"{datetime.date.today()}"\n''')
     

def format_femea_nelore(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
             # vaca magra
            output.write(f'''"estado":"{itens[0]}","animal":"vaca magra","valor_animal":"{itens[1]}","relacao_troca()":"{itens[2]}","relacao_troca()":"{itens[3]}","data":"{datetime.date.today()}"\n''')
            # novilha
            output.write(f'''"estado":"{itens[0]}","animal":"novilha (9@)","valor_animal":"{itens[4]}","relacao_troca()":"{itens[5]}","relacao_troca()":"{itens[6]}","data":"{datetime.date.today()}"\n''')
            # bezerra 9@
            output.write(f'''"estado":"{itens[0]}","animal":"bezerra (7@)","valor_animal":"{itens[7]}","relacao_troca()":"{itens[8]}","relacao_troca()":"{itens[9]}","data":"{datetime.date.today()}"\n''')
            # bezerra 6@
            output.write(f'''"estado":"{itens[0]}","animal":"bezerra (7@)","valor_animal":"{itens[10]}","relacao_troca()":"{itens[11]}","relacao_troca()":"{itens[12]}","data":"{datetime.date.today()}"\n''')


format_boi_gordo(arquivo_entrada='boi gordo @ 2026-02-17.json',arquivo_saida='valores_gerais_boi_gordo.json')  
format_femea_nelore(arquivo_entrada='femea nelore @ 2026-02-17.json',arquivo_saida='valores_gerais.json')
format_macho_nelore(arquivo_entrada='macho nelore @ 2026-02-17.json',arquivo_saida='valores_gerais.json')  
