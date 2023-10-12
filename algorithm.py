import csv
import numpy as np
import json
import networkx as nx

# change as per form options
options = {0: ['Friend', 'Partner', 'Parents', 'Pet', 'Myself'],
 1: ['I like reading poems', 'I like listening to lyrical poems and ghazals', 'I attend recitals or open-mics or live performances', 'I enjoy watching videos'],
 2: ['Radiant Red', 'Ocean Blue', 'Golden Yellow', 'Glossy Green'],
 3: ['Couplet', 'Free Verse', 'Spoken Word', 'Ghazal'],
 4: ['Melancholic', 'Reflective', 'Romantic', 'Cheerful']}

# link each name to an n dimensional array
candidates = {}
rel = 'matches/'
with open(rel+'makematch.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for i,row in enumerate(reader):
        # change indexes as per csv file
        candidates[row[2]+':'+row[1]] = list(map(lambda s: options[row.index(s) - 3].index(s),row[3:8]))
print(candidates)

# calculate the distance between polar coordinates
def calculate_distance(p1,p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# rank the distances for each corresponding array
distances = {}
for i in candidates:
    tmp_candidates = candidates.copy()
    tmp_candidates.pop(i)
    distances[i] = sorted(tmp_candidates.keys(),key=lambda s: calculate_distance(candidates[i],candidates[s]))
    
print(distances)



# create a minimum weighted graph with the distances corresponding to each node
G = nx.Graph()
for person, preferences in distances.items():
  for other_person in preferences:
    G.add_edge(person, other_person, weight=preferences.index(other_person))

matching = nx.min_weight_matching(G)

print(matching)
matching = {i:pair for i,pair in enumerate(matching)}
with open(rel+'matches.json','w') as json_file:
   json.dump(matching,json_file)
