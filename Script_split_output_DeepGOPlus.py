import os
import csv

deepgoplus_output = "C:/Users/uerjl/OneDrive/Área de Trabalho/Hanna/LITV/DeepGOPlus/Sequências_Tcruzi/Y_C6/Hanna_190225_DeepGOPlus_NaoHipoteticasSemGO_YC6.tsv"
output_file = "C:/Users/uerjl/OneDrive/Área de Trabalho/Hanna/LITV/DeepGOPlus/Sequências_Tcruzi/Y_C6/Atualizado_Hanna_200225_DeepGOPlus_Naoipoteticas_YC6_sem_GO.tsv"

# Verifica se o arquivo de entrada existe
if os.path.exists(deepgoplus_output):
    print(f"O arquivo {deepgoplus_output} foi encontrado.")
else:
    print(f"Erro: O arquivo {deepgoplus_output} não foi encontrado.")

# Abrir o arquivo para leitura
dicionario = {}

try:
    with open(deepgoplus_output, 'r', encoding='utf-8') as file:
        for line in file:
            # Dividir a linha em colunas usando espaço ou outro delimitador
            partes = line.strip().split()

            # O item da primeira coluna é a chave do dicionário. Os itens das demais colunas são os valores.
            if partes:
                dicionario[partes[0]] = partes[1:]

    count = 0
    # Abrir o arquivo de saída para escrita
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter='\t')
            for protein, gos_scores in dicionario.items():
                for go_score in gos_scores:
                    if "|" in go_score:
                        go_id, score = go_score.split("|", 1)
                        writer.writerow([protein, score, go_id])
                        count += 1
        print("Número de linhas", count)
        print(f"Resultados escritos no arquivo {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")

except FileNotFoundError:
    print(f"Erro: O arquivo {deepgoplus_output} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
