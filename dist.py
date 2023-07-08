import argparse
import json
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

#create argarse for script
parser = argparse.ArgumentParser()
parser.add_argument('Jfilename') 
parser.add_argument('cityname') 
parser.add_argument('statename') 

args = parser.parse_args()

#function to avoid divide zero error
def zerodiv(x,y):
    return x / y if y else 0

#get data from JSON and read it with Pandas's Dataframe
data_file = open(args.Jfilename, encoding='utf-8')
data = []
for line in data_file:
    data.append(json.loads(line))
df = pd.DataFrame(data)
data_file.close()

outfile1 = open('Q2_part1.out.txt', 'w')
outfile2 = open('Q2_part2.out.txt', 'w')

#extract the table of restaurants which relate to the picked city and state
a = df.loc[(df['city'] == args.cityname) & (df['state'] == args.statename)]
b = a.loc[a['categories'].str.contains('Restaurants', case = False).fillna(False)]

country_list = ['Japanese', 'Chinese', 'Canadian (New)', 'Italian', 'Vietnamese', 'American (New)', 'American (Traditional)', 
                'Asian Fusion', 'Mediterranean', 'Indian', 'Middle Eastern', 'Afghan', 'African', 'Arabian', 'Argentine', 
                'Armenian','Australian', 'Austrian', 'Bangladeshi', 'Basque', 'Belgian', 'Brazilian', 'British', 'Bulgarian', 
                'Burmese', 'Cajun', 'Cambodian', 'Caribbean', 'Cuban', 'Czech', 'Eritrean', 'Ethiopian', 'Filipino', 'French', 
                'German', 'Greek', 'Guamanian', 'Hawaiian', 'Honduran', 'Hungarian', 'Iberian', 'ndonesian', 'Irish', 'Korean', 
                'Laotian', 'Latin American', 'Colombian', 'Malaysian', 'Mexican', 'Modern European', 'Mongolian', 'Moroccan', 
                'New Mexican Cuisine', 'Nicaraguan', 'Pakistani', 'Iranian', 'Peruvian', 'Polish', 'Portuguese', 'Russian', 
                'Scandinavian', 'Scottish', 'Singaporean', 'Slovakian', 'Somali', 'Spanish', 'Syrian', 'Taiwanese', 'Thai', 
                'Turkish', 'Ukrainian', 'Uzbek', 'Canadian (old)', 'Hong Kong', 'Roman', 'Senegalese', 'South African', 'Dominican',
                'Puerto Rican', 'Trinidadian', 'Mauritius','Reunion', 'Szechuan', 'Shanghainese', 'Cantonese','Venezuelan']

#create two dictionary, rn_dict's key is the geographical restaurant categories, value is the number of restaurant
#vn_dict's key is the the geographical restaurant categories, value are list contain two value number of the review and average of review
rn_dict ={}
vn_dict ={}
for co in country_list:
    rn = b.loc[b['categories'].str.contains(co, regex=False, case = False).fillna(False)]
    rn_dict[co] = rn.shape[0]
    vn = rn['review_count'].sum()
    arc = zerodiv(vn,rn.shape[0])
    vn_dict.setdefault(co, [])
    vn_dict[co].append(vn)
    vn_dict[co].append(round(arc,2))

#find the top-10 categories
c = Counter(rn_dict)
for k, v in c.most_common(10):
    # print(f"{k}:{v}")
    outfile1.write(f"{k}:{v}"+"\n")

#find the top-10 most reviewed categories
d = Counter(vn_dict)
for k, v in d.most_common(10):
    # print(f"{k}:{v[0]}:{v[1]}")
    outfile2.write(f"{k}:{v[0]}:{v[1]}"+"\n")

#10-inch-by-10-inch bar-chart of top-5 categories
e = dict(c.most_common(5))
# print(e)
rc = list(e.keys())
nofr = list(e.values())
fig = plt.figure(figsize=(10, 10))
plt.bar(rc, nofr)
plt.xlabel("restaurant categories")
plt.ylabel("number of restaurant")
plt.title("Top-5 restaurants categories")
plt.savefig('Q2_part3.pdf')
