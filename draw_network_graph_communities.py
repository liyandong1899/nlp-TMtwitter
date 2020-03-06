import json
import io
import ijson
import networkx as nx
import matplotlib.pyplot as plt
import community
import numpy
import math

#f=open('/home/user/Documents/YandongLi/CQfiles/corpora1000','w')
G=nx.DiGraph()
leafDict={}
singleNode=[]
with open('/home/user/Documents/YandongLi/CQfiles/toni-morrison-tweets_2019.json', 'r') as json_file:
    for line_number, line in enumerate(json_file):
      if line_number<=5000:
        print(line_number)
        poster="0"
        userRTed="0"
        data_per_line = json.loads(line)
        #print(data_per_line['entities']['user_mentions'])
        #print(data_per_line.keys())
        
        
        mentioned_list = []
        for mentioned in data_per_line['entities']['user_mentions']:
            mentioned_list.append(mentioned['id_str'])
        print(mentioned_list)
        userRTed = mentioned_list
        poster = data_per_line['user']['id_str']

        if userRTed!="0":
            for item in mentioned_list:
                G.add_edge(item,poster)
        else:
            if "toni morrison" in text:
                G.add_node(poster)
    
#f.close()

for item in G.nodes:
    if G.in_degree(item)==1 and G.out_degree(item)==0:
        leafDict.update({item : G.neighbors(item)})

G.remove_nodes_from(leafDict.keys())

H=G.to_undirected()

for item in H.nodes:
    if H.degree(item)==0:
        singleNode.append(item)
H.remove_nodes_from(singleNode)

partition = community.best_partition(H)  # compute communities
#print(len(partition))
print(partition)
print(partition.values())
  # compute graph layout
pos={}
d1 = {}
for category in partition.values():
    d1[category] = {}
for item in partition:
    d1[partition[item]][item] = 0
print(d1)

NumberCategory=[len(value) for key,value in d1.items()]
MaxNumberCategory=max(NumberCategory)
MaxCateLoc=[i for i,j in enumerate(NumberCategory) if j==MaxNumberCategory][0]

baseGraph = nx.Graph()
for category in d1.keys():
    baseGraph.add_node(category)
for j in range(0,len(d1.keys())):
    if j!=MaxCateLoc:
        baseGraph.add_edge(MaxCateLoc,j,weight=1/NumberCategory[j])
BasePos = nx.spring_layout(baseGraph)
print(BasePos)

for category in d1.keys():
    tempGraph = nx.Graph()
    for userid in d1[category].keys():
        tempGraph.add_node(userid)
        for nghb in H.neighbors(userid):
            tempGraph.add_edge(userid,nghb)
        tempPos = nx.kamada_kawai_layout(tempGraph)
        pos[userid] = BasePos[category] + tempPos[userid]*math.sqrt(NumberCategory[category]/sum(NumberCategory))##*math.sqrt(1/len(d1.keys()))

nx.draw_networkx_nodes(H, pos, node_size=10, cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
nx.draw_networkx_edges(H, pos, alpha=0.3)
plt.show(H)



'''4
part = community.best_partition(H)
mod = community.modularity(part,H)

# Plot, color nodes using community structure
values = [part.get(node) for node in H.nodes()]
nx.draw_spring(H, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show()
'''