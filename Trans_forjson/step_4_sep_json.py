import json
import random

input_file_path = 'output.json'
output_file_path_1 = 'output_part1.json'
output_file_path_2 = 'output_part2.json'
output_file_path_1_updated = 'output_part1_updated.json'
output_file_path_2_updated = 'output_part2_updated.json'

def read_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)

def write_json(data, file_path):
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    json_data = read_json(input_file_path)
    
    # 随机打乱数据
    random.shuffle(json_data)
    
    # 平分数据
    mid_point = len(json_data) // 2
    data_part1 = json_data[:mid_point]
    data_part2 = json_data[mid_point:]
    
    write_json(data_part1, output_file_path_1)
    write_json(data_part2, output_file_path_2)
    
    # 将 part1 的 "sort_answer" 字段更新为空字符串
    for item in data_part1:
        if 'sort_answer' in item:
            item['sort_answer'] = ""

    write_json(data_part1, output_file_path_1_updated)

    for item in data_part2:
        if 'sort_answer' in item and item['sort_answer'] == "":
            item['sort_answer'] = "1,2,3,4"
    
    write_json(data_part2, output_file_path_2_updated)
    

if __name__ == '__main__':
    main()
