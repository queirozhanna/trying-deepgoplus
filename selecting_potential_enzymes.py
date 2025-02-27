import csv

# Abrir o arquivo TSV de entrada
with open('/path/to/input/file.tsv', 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter='\t')
    
    # Abrir um arquivo TSV de saída
    with open('/path/to/output/file.tsv', 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        
        # Iterar sobre cada linha do arquivo de entrada
        for row in reader:
            # Verificar se a penúltima coluna contém 'activity' e não é 'catalytic activity'
            if 'activity' in row[-2] and row[-2].strip() != 'catalytic activity':
                writer.writerow(row)
