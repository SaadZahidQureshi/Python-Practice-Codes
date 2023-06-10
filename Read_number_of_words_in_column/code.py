import pandas as pd

data  = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding='latin1')

# print(data.head())

data['Number of words'] = data['Article'].apply(lambda x: len(x.split()))
print(data.head())
                                               