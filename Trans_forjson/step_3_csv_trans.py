import csv
import json

# 文件路径
csv_file_path = '731_combine_1000.csv'
json_file_path = 'math_gen_0730a_h1000.json'
output_file_path = 'output.json'

def read_csv(csv_file_path):
    sort_answers = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sort_answers.append(row['sort_answer'])
    return sort_answers

# 读取JSON文件
def read_json(json_file_path):
    with open(json_file_path, mode='r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)

# 写入JSON文件
def write_json(data, output_file_path):
    with open(output_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

def main():
    sort_answers = read_csv(csv_file_path)
    json_data = read_json(json_file_path)
    
    # 确保 CSV 文件的行数与 JSON 文件的行数匹配
    if len(sort_answers) != len(json_data):
        print("错误：CSV 文件的行数与 JSON 文件的行数不匹配")
        return
    
    # 将 sort_answer 添加到 JSON 数据中,注意数据格式对齐（如果不对齐可以加一个prompt_id相等判定）
    for item, answer in zip(json_data, sort_answers):
        item['sort_answer'] = answer
    
    write_json(json_data, output_file_path)

if __name__ == '__main__':
    main()