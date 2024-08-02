import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            
            # 写入CSV文件的头部
            csv_writer.writerow(['prompt', 'ability', 'response1', 'response2', 'response3', 'response4'])
            
            for entry in data:
                # 确保每个条目是字典
                if not isinstance(entry, dict):
                    print("Error: An entry in the list is not a dictionary.")
                    continue
                
                prompt = entry.get('prompt', '')
                ability = entry.get('ability', '')
                responses = entry.get('response', [])

                if not isinstance(responses, list):
                    print("Error: 'response' is not a list.")
                    continue

                # 取出4个response内容
                response_contents = [response.get('content', '') if isinstance(response, dict) else '' for response in responses[:4]]
                
                while len(response_contents) < 4:
                    response_contents.append('')
                
                # 写入一行数据到CSV
                csv_writer.writerow([prompt, ability] + response_contents)
                
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    except Exception as e:
        print(f"Error: {e}")

json_file = 'math_gen_0730a_h1000.json'  
csv_file = 'output_731.csv'  

json_to_csv(json_file, csv_file)
