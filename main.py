import pandas as pd
import requests

datas = []




url = 'https://api.api-futebol.com.br/v1/campeonatos/2/tabela'
API_KEY = '$$$$' # chave api particular

headers = {
    'Authorization' : f'Bearer {API_KEY}',
    "Content-Type": "application/json"
}

response = requests.get(url=url , headers=headers)


if response.status_code == 200:
    dicionario = response.json()
    for times in dicionario:

        data = {
            'Posição': None,
            'Time': None,
            'Vitorias': None,
            'Derrotas': None, 
            'Empates': None,
            'Aproveitamento': None
        }

        data['Posição'] = times['posicao']
        data['Time'] = times['time']['nome_popular']
        data['Vitorias'] = times['vitorias']
        data['Derrotas'] = times['derrotas']
        data['Empates'] = times['empates']
        data['Aproveitamento'] = times['aproveitamento']

        datas.append(data)
        # print(dicionario)
        
else:
    
    print(f"Erro: {response.status_code}")
    print(response.text)



# print(datas)

df = pd.DataFrame(datas)

try:
    arquivo_excel = df.to_excel('tabela_brasileiro_2021.xlsx' , 'planilha1' , index=False)

    print(arquivo_excel)
except BaseException as e:
    print(e)
