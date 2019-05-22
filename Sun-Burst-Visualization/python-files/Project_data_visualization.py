import json
import re

import pandas as pd

# from google.colab import files
# uploaded = files.upload()
# NotebookApp.iopub_data_rate_limit=10000000

path = "../resources/"
file = path+'categories_taxonomy.tsv'
df = pd.read_csv(file, delimiter='\t', encoding='utf-8', low_memory=False)
pd.set_option('display.max_columns', len(df.columns))
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 10000)
df = df[df.parent == 'wines'].children

wine_country = []
alcohol = {}
wine_name = {}
prod_ids = {}
result = {}

category_taxonomy = pd.read_csv(path+'categories_taxonomy.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

product_category = pd.read_csv(path+'products_categories_full.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

products = pd.read_csv(path+'products.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

wines = category_taxonomy[category_taxonomy.parent == 'wines'].children

for country in wines:
    if re.findall(r'wines-from-*', country):
        wine_country.append(country)
    result[country] = wine_country


for wines in wine_country:
    wine_name[wines] = category_taxonomy[category_taxonomy.parent == wines].children

for keys, val in wine_name.items():
    #   print(keys + '->' + val)
    for item in val:
        prod_ids[item] = product_category[product_category.category == item].code

for key, codes in prod_ids.items():
    # print(key + '->' + codes)
    for cod in codes:
        #     tp = products['alcohol_100g'].mean()
        alcohol[cod] = products[products.code == cod].alcohol_100g.mean()

category_taxonomy = pd.read_csv(path+'categories_taxonomy.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

product_category = pd.read_csv(path+'products_categories_full.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

products = pd.read_csv(path+'products.tsv', delimiter='\t', encoding='utf-8', low_memory=False)

alcohols = category_taxonomy[category_taxonomy.parent == 'alcoholic-beverages'].children


def get_child(name, dic2):
    if category_taxonomy[category_taxonomy.parent == name].children.empty:
        # print ("here")
        dic3 = {"name": str(name), "size": len(str(name))}
        return dic3
    else:
        temp3 = {}

        l1 = category_taxonomy[category_taxonomy.parent == name].children
        childs = []
        for items in l1:
            dic2 = {}
            childs.append(get_child(items, dic2))

        temp3["name"] = str(name)
        temp3["children"] = childs

        return temp3


root_name = "alcoholic-beverages"
root = {}
for alcohol in alcohols:
    root["name"] = str(root_name)

    temp = {}
    second_root = get_child(alcohol, temp)
    try:
        root["children"].append(second_root)
    except:
        root["children"] = [second_root]
print("Dumping the data into json file %s", )
print(root)

with open('../json-dump-files/alcoholic-beverages.json', 'w') as fp:
    json.dump(root, fp)
