import pandas as pd
from collections import defaultdict

df = pd.read_csv('1000_output.csv')

df['sort_answer'] = df.apply(
    lambda row: f"{row['response1序号']}={row['response2序号']}" if row['输出'] == '是！' and row['ratio1-2'] > 0.7 
    else f"{row['response1序号']},{row['response2序号']}", 
    axis=1
)

grouped = df.groupby('prompt')

def combine_group(group):
    num = group['序号'].iloc[0]
    prompt = group['prompt'].iloc[0]
    response1 = group.loc[group['response1序号'] == 1, 'response1'].values[0] if not group.loc[group['response1序号'] == 1, 'response1'].empty else None
    response2 = group.loc[group['response1序号'] == 2, 'response1'].values[0] if not group.loc[group['response1序号'] == 2, 'response1'].empty else None
    response3 = group.loc[group['response1序号'] == 3, 'response1'].values[0] if not group.loc[group['response1序号'] == 3, 'response1'].empty else None
    response4 = group.loc[group['response2序号'] == 4, 'response2'].values[0] if not group.loc[group['response2序号'] == 4, 'response2'].empty else None

    graph = defaultdict(set)
    for answer in group['sort_answer']:
        pairs = answer.split(';')
        for pair in pairs:
            if '=' in pair:
                left, right = pair.split('=')
                graph[left].add(right)
                graph[right].add(left)
    
    def get_connected_component(start, visited):
        component = set()
        stack = [start]
        while stack:
            #弹出一个节点赋值给node
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                #node进入联通集合中
                component.add(node)
                #将node相邻节点压入栈
                stack.extend(graph[node])
        return component

    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = get_connected_component(node, visited)
            components.append(component)
    
    merged_sort_answers = []
    for component in components:
        sorted_component = sorted(component, key=int)
        merged_sort_answers.append("=" .join(sorted_component))

    final_sort_answer = ';'.join(merged_sort_answers)
    
    return pd.Series({
        '序号': num,
        'prompt': prompt,
        'response1': response1,
        'response2': response2,
        'response3': response3,
        'response4': response4,
        'sort_answer': final_sort_answer
    })

combined_df = grouped.apply(combine_group).reset_index(drop=True)

combined_df.to_csv('731_combine_1000.csv', index=False)
