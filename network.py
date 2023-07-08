import argparse
import json
import pandas as pd

#create argarse for script
parser = argparse.ArgumentParser()
parser.add_argument('Jfilename') 
parser.add_argument('vote_n') 

args = parser.parse_args()

#get data from JSON and read it with Pandas's Dataframe
data_file = open(args.Jfilename, encoding='utf-8')
data = []
for line in data_file:
    data.append(json.loads(line))
df = pd.DataFrame(data)
data_file.close()

outfile = open('Q3.out.txt', 'w', encoding='utf-8')

#extract the table based on useful >= n
a = df.loc[(df['useful'] >= int(args.vote_n))]

#create dictionary which key are user_id with list of value contain friend user_id
user_friend_dict = dict(zip(a.user_id, a.friends))

#remove the friend user_id which not satisfied useful >= n, put which tuple in format (user_id, user_id) in list
edge_list = []
for k, v in user_friend_dict.items():
    x = v.split(", ")
    for i in x:
        if i.strip() in user_friend_dict.keys():
            y = (k,i)
            edge_list.append(y)
        else:
            pass

#keep only one duplicate edge such as ab and remove ba 
temp = [tuple(sorted(sub)) for sub in edge_list]
res = list(set(temp))

#output the edge list
for item in res:
    outfile.write(item[0].strip() + '  ' + item[1].strip() + '\n')
   
