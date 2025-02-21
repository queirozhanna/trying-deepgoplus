import os
import csv

deepgoplus_output = "/path/to/deepgoplus/file.tsv"
output_file = "/path/to/new/file.tsv"

# Check if the input file exists
if os.path.exists(deepgoplus_output):
    print(f"The file {deepgoplus_output} was found.")
else:
    print(f"Error: The file {deepgoplus_output} was not found.")

# Open the file for reading
dictionary = {}

try:
    with open(deepgoplus_output, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into columns using space or other delimiters
            parts = line.strip().split()

            # The item in the first column is the key of the dictionary. The items in the other columns are the values.
            if parts:
                dictionary[parts[0]] = parts[1:]

    count = 0
    # Open the output file for writing
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter='\t')
            for protein, gos_scores in dictionary.items():
                for go_score in gos_scores:
                    if "|" in go_score:
                        go_id, score = go_score.split("|", 1)
                        writer.writerow([protein, score, go_id])
                        count += 1
        print("Number of rows", count)
        print(f"Results written to the file {output_file}")

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

except FileNotFoundError:
    print(f"Error: The file {deepgoplus_output} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
