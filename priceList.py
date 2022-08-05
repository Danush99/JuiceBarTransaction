import csv

def make_json(csvFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        #csvReader = csv.DictReader(csvf)
        reader=csv.reader(csvf, delimiter = '\t')
        for row in reader:
          if(len(row)>0):
            key = row[0]
            data[key]=row[1]
    return data

juice_regular = "price_lists/juice_regular.csv"
juice_vegi = "price_lists/juice_vegi.csv"
milkshake = "price_lists/milkshake.csv"
smoothies = "price_lists/smoothies.csv"
other_items = "price_lists/other_items.csv"

juice_regular_json=make_json(juice_regular)
juice_vegi_json=make_json(juice_vegi)
milkshake_json=make_json(milkshake)
smoothies_json=make_json(smoothies)
other_items_json=make_json(other_items)
