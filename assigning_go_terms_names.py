import os
import csv

# File paths
tsv_file_1 = "/path/to/input/file1.tsv"
tsv_file_2 = "/path/to/input/file2.tsv"
obo_file = "/path/to/gene/ontology/file.obo"
output_file_1 = "/path/to/output/file1.tsv"
output_file_2 = "/path/to/output/file2.tsv"

# Function to read the .obo file and create a dictionary of GO terms
def parse_obo_file(obo_file):
    go_terms = {}
    with open(obo_file, 'r', encoding='utf-8') as obo:
        current_id = None
        current_name = None
        current_namespace = None
        for line in obo:
            if line.startswith("id: "):
                current_id = line.strip().split(": ")[1]
            elif line.startswith("name: "):
                current_name = line.strip().split(": ")[1]
            elif line.startswith("namespace: "):
                current_namespace = line.strip().split(": ")[1]
            elif line.strip() == "[Term]":
                if current_id and current_name and current_namespace:
                    go_terms[current_id] = (current_name, current_namespace)
                current_id = None
                current_name = None
                current_namespace = None
        # Adds the last term if necessary
        if current_id and current_name and current_namespace:
            go_terms[current_id] = (current_name, current_namespace)
    return go_terms

# Function to process a .tsv file
def process_tsv_file(tsv_file, go_terms, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        with open(tsv_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter='\t')
            for row in reader:
                if len(row) == 3:
                    protein, score, go_id = row
                    if go_id in go_terms:
                        name, namespace = go_terms[go_id]
                        writer.writerow([protein, score, go_id, name, namespace])

# Reads the .obo file and creates the GO terms dictionary
go_terms = parse_obo_file(obo_file)

# Processes the two .tsv files and writes the results to separate output files
process_tsv_file(tsv_file_1, go_terms, output_file_1)
process_tsv_file(tsv_file_2, go_terms, output_file_2)

print(f"Results from file 1 written to {output_file_1}")
print(f"Results from file 2 written to {output_file_2}")
