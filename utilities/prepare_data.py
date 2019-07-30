import json
import pandas as pd

df = pd.read_csv('data_base.csv', encoding='gbk')
df = df.fillna('')


def find_loc(product, text):
    """
    function to find the place for the product entity
    :param product:
    :param text:
    :return:
    """
    loc = None
    text = str(text)
    text_end = len(text)
    if product:
        while loc is None or len(loc) > len(product.replace(" ", "")) + 2:
            start = text.find(product[0])
            end = text.rfind(product[-1], 0,text_end) + 1
            loc = text[start:end].replace(" ", "")
            text_end = end - 1
    else:
        start = -1
        end = -1
    return start, end, text[start:end]


for i, row in df.iterrows():
    product = row['product']
    text = row['question']
    start, end, loc = find_loc(product, text)
    df.loc[i, 'start'] = int(start)
    df.loc[i, 'end'] = int(end)
    df.loc[i, 'product_entity'] = loc

"""
1. NLU data
"""

train_data = dict(rasa_nlu_data={})
train_data['rasa_nlu_data']['common_examples'] = []
train_data['rasa_nlu_data']['regex_features'] = []
train_data['rasa_nlu_data']['lookup_tables'] = []
train_data['rasa_nlu_data']['entity_synonyms'] = []

for _, row in df.iterrows():
    if row['start'] != -1 and row['end'] != -1:
        entities = [dict(start=int(row['start']), end=int(row['end']), value=row['product_entity'], entity='product')]
    else:
        entities = []
    row_data = dict(text=row['question'], intent=row['intent'], entities=entities)
    train_data['rasa_nlu_data']['common_examples'].append(row_data)

names = set(df[df['product'] != 'general']['product'].unique())
for name in names:
    synonyms = list(set(df.loc[df['product'] == name, 'product_entity'].unique().tolist()).difference(set([name])))
    if synonyms:
        train_data['rasa_nlu_data']['entity_synonyms'].append(dict(value=name, synonyms=synonyms))

with open('../data/customer_service.json', 'w') as f_handle:
    json.dump(train_data, f_handle)

"""
2. Jieba User Dict
"""

entities = df.product_entity.unique().tolist()
with open("../jieba_userdict/jieba_userdict.txt", 'w') as f_handle:
    lines = [e + "\n" for e in entities if e]
    f_handle.writelines(lines)