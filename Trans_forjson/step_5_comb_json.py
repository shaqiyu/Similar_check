import json

# 文件路径
input_file_path_1 = '0730a_equal_v0.json'
input_file_path_2 = '0730a_noequal_v0.json'
output_file_path = 'merged_output.json'

# 读取JSON文件
def read_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)

# 写入JSON文件
def write_json(data, file_path):
    with open(file_path, mode='w', encoding='utf-8') as file:
        for item in data:
            json_string = json.dumps(item, separators=(',', ':'), ensure_ascii=False)
            file.write(json_string + '\n')
        #json.dumps(data, file, ensure_ascii=False)
        #json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    # 读取两个JSON文件
    json_data1 = read_json(input_file_path_1)
    json_data2 = read_json(input_file_path_2)
    
    # 合并两个JSON数据
    merged_data = json_data1 + json_data2
    
    # 将合并后的数据写入新的文件
    write_json(merged_data, output_file_path)
    
    print(f'两个JSON文件已合并，保存到 {output_file_path}')

if __name__ == '__main__':
    main()
