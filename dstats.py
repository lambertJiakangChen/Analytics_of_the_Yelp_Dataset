import argparse
import json
import pandas as pd

#create argarse for script
parser = argparse.ArgumentParser()
parser.add_argument('Jfilename') 
parser.add_argument('cityname') 
parser.add_argument('statename') 

args = parser.parse_args()

#get data from JSON and read it with Pandas's Dataframe
data_file = open(args.Jfilename, encoding='utf-8')
data = []
for line in data_file:
    data.append(json.loads(line))
df = pd.DataFrame(data)
data_file.close()

outfile = open('Q1.out.txt', 'w')

#The number of bussiness in the picked city and state
a = df.loc[(df['city'] == args.cityname) & (df['state'] == args.statename)]
print(a.shape[0])
outfile.write(str(a.shape[0]) + '\n')

#The average number of stars of businesses in the picked city and state
print(round(a['stars'].mean(),2))
outfile.write(str(round(a['stars'].mean(),2)) + '\n')

#The number of restaurants in the picked city and state
b = a.loc[a['categories'].str.contains('Restaurants', case = False).fillna(False)]
print(b.shape[0])
outfile.write(str(b.shape[0]) + '\n')

#The average number of stars of restaurants in the picked city and state
print(round(b['stars'].mean(),2))
outfile.write(str(round(b['stars'].mean(),2)) + '\n')

#The average number of reviews for all businesses in the picked city and state
print(round(a['review_count'].mean(),2))
outfile.write(str(round(a['review_count'].mean(),2)) + '\n')

#The average number of reviews for restaurants in the picked city and state
print(round(b['review_count'].mean(),2))
outfile.write(str(round(b['review_count'].mean(),2)) + '\n')