import os
import json

def tratar_dados(diretorio):
    arquivos_json = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.json')]

    for arquivo in arquivos_json:
        arquivo_path = os.path.join(diretorio, arquivo)
    
        with open(arquivo_path, 'r') as f:
            dados = json.load(f)

            for bloco in dados:
                dados[bloco] = classificar_sinal(dados[bloco])

            file_name, file_extension = os.path.splitext(arquivo)
            salvar_arquivos_tratados(dados, output_file=f'{file_name}_tratado{file_extension}')


# cria uma para salvar os arquivos depois de tratados
def salvar_arquivos_tratados(json_tratado, output_file, output_folder='dados_tratados'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, output_file)

    with open(output_file_path, 'w') as f:
        json.dump(json_tratado, f, indent=2)


# Itera sobre todos os andares e pontos de acesso e classifica o sinal(dBm) de 
# cada um em "Bom", "Médio" ou "Ruim".
def classificar_sinal(bloco, bom=-60, medio=-79):
    b = bloco
    for andar in b:
        # pa => Ponto de acesso
        for pa in b[andar]:
            if int(pa['Sinal']) >= bom:
                pa['Qualidade'] = 'Bom'
            elif int(pa['Sinal']) >= medio and int(pa['Sinal']) < bom:
                pa['Qualidade'] = 'Medio'
            else:
                pa['Qualidade'] = 'Ruim'
    
    return b

if __name__ == '__main__':
    tratar_dados('dados/')