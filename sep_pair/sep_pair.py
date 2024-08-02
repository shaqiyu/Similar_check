import csv
from itertools import combinations

def parse_and_process(input_file_path, output_file_path):
    result = []
    
    with open(input_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  
        
        keep_columns_idx = [
            headers.index('题目全局首次领取日期'),
            headers.index('v2版本标签(rm人题分发)'),
            #headers.index('新标签(rm人题分发)'),
            headers.index('题目id'),
            headers.index('题目浏览链接'),
            headers.index('题目最终状态'),
            headers.index('废弃原因'),
            headers.index('prompt'),
            headers.index('第一个response内容'),
            headers.index('第二个response内容'),
            headers.index('第三个response内容'),
            headers.index('第四个response内容'),
            headers.index('题目最新交付答案')
        ]
        
        for row in reader:
            keep_columns_data = [row[i] for i in keep_columns_idx[:7]]
            responses = row[keep_columns_idx[7]:keep_columns_idx[11] + 1]
            answer_mapping = row[keep_columns_idx[11]]
            discard_reason = row[keep_columns_idx[5]]

            if discard_reason in ["response均好"]:
                answer_mapping = "1=2=3=4"

            answer_mapping = answer_mapping.replace('5', '')

            # Split the answer_mapping into pairs
            pairs = set()
            answer_parts = answer_mapping.split('=')
            num_responses = len(answer_parts)
            for i in range(num_responses):
                for j in range(i + 1, num_responses):
                    pairs.add(f"{i+1}={j+1}")
                    pairs.add(f"{j+1}={i+1}")

            pairs = set()
            for part in answer_mapping.split(','):
                answer_parts = part.split('=')
                for combo in combinations(answer_parts, 2):
                    pairs.add(f"{combo[0]}={combo[1]}")
                    pairs.add(f"{combo[1]}={combo[0]}")

            seen_pairs = set()
            for i in range(len(responses)):
                for j in range(i + 1, len(responses)):
                    pair_str = f"{i+1}={j+1}"
                    if pair_str not in seen_pairs:
                        if answer_mapping == "(null)":
                            is_equal_pair = '无意义'
                        else:
                            is_equal_pair = '是' if pair_str in pairs else '否'
                        if j+1 != 5:  #Delete "5"
                            result.append(keep_columns_data + [is_equal_pair, responses[i], responses[j], i+1, j+1])
                            seen_pairs.add(pair_str)

    with open(output_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            headers[:7] + ['是否等号pair', 'rsp1', 'rsp2', 'response1序号', 'response2序号']
        )
        writer.writerows(result)

input_file_path = '16_22_pair.csv'
output_file_path = '16_22_mathdata.csv'
parse_and_process(input_file_path, output_file_path)
print(f"{output_file_path} Done")