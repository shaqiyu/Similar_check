import csv
import Levenshtein

def calculate_similarity_ratio_for_row(values):
    columns = list(values.keys())
    similarity_results = {col: {} for col in columns}
    
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                similarity_results[col1][col2] = Levenshtein.ratio(values[col1], values[col2])
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
    input_file = './transformer/check1.csv'
    output_file = './check2.csv'
    columns = ['response1', 'response2']

    process_csv(input_file, output_file, columns)
    print(f"Similarity results have been written to {output_file}")

if __name__ == "__main__":
    main()