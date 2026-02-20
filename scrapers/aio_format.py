import datetime
import asyncio

inicio = '{'
fim = '}'
async def format_macho_nelore(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
            # boi magro
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"boi magro","valor_animal":"{itens[1]}","valor_kg":"{itens[2]}","relacao_troca":"{itens[3]}","data":"{datetime.date.today()}"{fim}\n''')
            # garrote
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"garrote","valor_animal":"{itens[4]}","valor_kg":"{itens[5]}","relacao_troca":"{itens[6]}","data":"{datetime.date.today()}"{fim}\n''')
            # bezerro
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"bezerro","valor_animal":"{itens[7]}","valor_kg":"{itens[8]}","relacao_troca":"{itens[9]}","data":"{datetime.date.today()}"{fim}\n''')
            # bezerro desmamado
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"bezerro desmamado","valor_animal":"{itens[10]}","valor_kg":"{itens[11]}","relacao_troca":"{itens[12]}","data":"{datetime.date.today()}"{fim}\n''')


async def format_boi_gordo(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
            if len(itens) == 10:
                output.write(f'''{inicio}"estado":"{itens[0]}","animal":"boi gordo","regiao":"{itens[1]}{itens[2]}","arroba_a_vista":"{itens[3]}","arroba_a_prazo":"{itens[4]}","variacao":"{itens[5]}","data":"{datetime.date.today()}"{fim}\n''')    
            elif len(itens) == 9:
                output.write(f'''{inicio}"estado":"{itens[0]}","animal":"boi gordo","regiao":"{itens[1]}","arroba_a_vista":"{itens[2]}","arroba_a_prazo":"{itens[3]}","variacao":"{itens[4]}","data":"{datetime.date.today()}"{fim}\n''')
            elif len(itens) == 8:
                output.write(f'''{inicio}"estado":"{itens[0]}","regiao":"","animal":"boi gordo","arroba_a_vista":"{itens[1]}","arroba_a_prazo":"{itens[2]}","variacao":"{itens[3]}","data":"{datetime.date.today()}"{fim}\n''')
     

async def format_femea_nelore(arquivo_entrada,arquivo_saida):
    with open(arquivo_entrada,'r+') as file, \
        open(arquivo_saida,'a') as output :
        # loop para percorrer cada linha
        for linha in file:
            # transforma cada linha em lista 
            itens = list(linha.split())
             # vaca magra
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"vaca magra","valor_animal":"{itens[1]}","valor_kg":"{itens[2]}","relacao_troca":"{itens[3]}","data":"{datetime.date.today()}"{fim}\n''')
            # novilha
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"novilha (9@)","valor_animal":"{itens[4]}","valor_kg":"{itens[5]}","relacao_troca":"{itens[6]}","data":"{datetime.date.today()}"{fim}\n''')
            # bezerra 9@
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"bezerra (7@)","valor_animal":"{itens[7]}","valor_kg":"{itens[8]}","relacao_troca":"{itens[9]}","data":"{datetime.date.today()}"{fim}\n''')
            # bezerra 6@
            output.write(f'''{inicio}"estado":"{itens[0]}","animal":"bezerra (7@)","valor_animal":"{itens[10]}","valor_kg":"{itens[11]}","relacao_troca":"{itens[12]}","data":"{datetime.date.today()}"{fim}\n''')

async def main():
    await asyncio.gather(
        format_boi_gordo(arquivo_entrada='boi gordo.json',arquivo_saida=f'valores_gerais_boi_gordo_{datetime.date.today()}.json'),  
        format_femea_nelore(arquivo_entrada='femea nelore.json',arquivo_saida=f'valores_gerais_reposicao_{datetime.date.today()}.json'),
        format_macho_nelore(arquivo_entrada='macho nelore.json',arquivo_saida=f'valores_gerais_reposicao_{datetime.date.today()}.json'),  
        )

if __name__ == "__main__":
    asyncio.run(main())
