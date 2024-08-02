import pandas as pd
import numpy as np

df = pd.read_csv('./check.csv', delimiter=',', encoding='utf-8')

# 随机抽取500组数据
#np.random.seed(10)  # 为了确保每次运行结果相同
#sample_df = df.sample(n=1000, random_state=1)
sample_df = df
new_rows = []

for index, row in sample_df.iterrows():
    prompt = row['prompt']
    responses = [row['response1'], row['response2'], row['response3'], row['response4']]
    
    # 两两组合响应
    for i in range(len(responses)):
        for j in range(i + 1, len(responses)):
            new_row = [
                i + 1,      
                j + 1,       
                prompt,     
                responses[i],
                responses[j]
            ]
            new_rows.append(new_row)

new_df = pd.DataFrame(new_rows, columns=[
    #'序号', 
    'response1序号', 
    'response2序号', 
    'prompt', 
    'response1', 
    'response2'
])

new_df.to_csv('check1.csv', index=False, encoding='utf-8-sig')

