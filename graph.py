import networkx as nx
import argparse

#create argarse for script
parser = argparse.ArgumentParser()
parser.add_argument('graphfile') 

args = parser.parse_args()

#read edge list from graph.txt which has the same format as Q3.out. Put vertices in list and edge in tuple as (user_id,user_id)
vertices = []
with open(args.graphfile) as f:
    lines = f.readlines()
    edges= list(tuple(line.split()) for line in lines)
    for line in lines:
        b = line.split()
        vertices.append(b[0])
        vertices.append(b[1])
vertices = list(dict.fromkeys(vertices))
outfile = open('Q4.out.txt','w')

# output number of vertices and number of edges
n_ver = len(vertices)
n_edges = len(edges)
print(f'{n_ver} {n_edges}')
outfile.write(f'{n_ver} {n_edges}' + '\n')

#utilize networkx create undirected graph 
g = nx.Graph()
for i in vertices:
    g.add_node(i)
for v in edges:
    g.add_edge(v[0],v[1])

#put each vertices' number of degree in to a list and compute its average degree
ki=[]
for i in g.degree():
     ki.append(i[1])
ave_de = round(sum(ki)/len(ki),2)
print(ave_de)
outfile.write(str(ave_de) + '\n')

#The number of connected components in the network
n_con = nx.number_connected_components(g)
print(n_con)
outfile.write(str(n_con) + '\n')

#The number of triangles in the network
tri = round(sum(nx.triangles(g).values())/3)
print(tri)
outfile.write(str(tri))