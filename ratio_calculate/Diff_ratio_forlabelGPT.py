import csv
import time 
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + 2*(c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def ratio(s1, s2):
    distance = levenshtein_distance(s1, s2)
    max_len = max(len(s1), len(s2))
    sum_len = len(s1) + len(s2)
    if max_len == 0:
        return 1.0
    return (sum_len - distance) / sum_len

def calculate_similarity_ratio_for_row(values):
    columns = list(values.keys())
    similarity_results = {col: {} for col in columns}
    
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                similarity_results[col1][col2] = ratio(values[col1], values[col2])
            else:
                similarity_results[col1][col2] = 1.0
    
    return similarity_results

def process_csv(input_file, output_file, columns):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
            header = ['Row', '1-2']
            writer.writerow(header)
            
            for row_number, row in enumerate(reader, start=1):
                values = {col: row[col] for col in columns}
                
                similarity_results = calculate_similarity_ratio_for_row(values)
                
                output_row = [
                    row_number,
                    similarity_results['response1']['response2']
                ]
                
                writer.writerow(output_row)

def main():
    start_time = time.time()
    input_file = './rsp_717_dataset.csv'
    output_file = './rsp_717_dataset_result_2.csv'
    columns = ['response1', 'response2']

    process_csv(input_file, output_file, columns)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Similarity results have been written to {output_file}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()