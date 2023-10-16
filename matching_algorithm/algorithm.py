import csv
import numpy as np
import json

# change as per form options
options = {"What time do you usually sleep?": ['8-10', '10-12', '12-2', '2-4', '4-6'],
 "What time do you usually wake up?": ['6-8', '8-10', '10-12', '12-2'],
 "Visitor preferences": ['rarely', 'occasionally', 'neutral', 'frequently','always'],
 "Cleaning habits": ['extremely', 'generally', 'somewhat', 'not']}

# link each name to an n dimensional array
candidates = {}
rel1 = '../webapp/data/'

with open(rel1+'preferences.json','r') as json_file:
    data = json.load(json_file)
    for candidate in data:
        candidates[candidate["name"] + ':' + candidate["email"]] = list(map(lambda s: options[s].index(candidate[s]), list(candidate.keys())[2:]))
print(candidates)


# TODO: add code here to partition the data set based on sex


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

def irving(roommates_dict):
    person_list = list(roommates_dict.keys())
    n = len(person_list)

    def get_rankings(prefs):
        return {prefs[i]: i for i in range(len(prefs))}

    roommates = [[person_list.index(neighbor) for neighbor in roommates_dict[person]] for person in person_list]

    proposals = [-1] * n  # Keeps track of the proposals each person has made
    rank = {}  # Keeps track of the rank of each roommate for each person

    for i in range(n):
        rank[i] = get_rankings(roommates[i])

    matched = set()  # Keep track of matched individuals
    stable_matching = []

    for proposer in range(n):
        if proposer not in matched:
            recipient = -1

            for roommate in roommates[proposer]:
                if proposals[roommate] == -1:
                    recipient = roommate
                    break
                else:
                    current_suitor = proposals[roommate]
                    if current_suitor not in matched:  # Check if the suitor is in matched
                        matched.remove(current_suitor)
                        matched.add(proposer)
                        proposals[roommate] = proposer
                        recipient = roommate

            if recipient != -1:
                matched.add(proposer)
                matched.add(recipient)
                proposals[recipient] = proposer
                proposals[proposer] = recipient
                stable_matching.append((person_list[proposer], person_list[recipient]))

    return stable_matching

matching = irving(distances)

print(matching)
rel = 'matches/'
matching = {i+1:pair for i,pair in enumerate(matching)}
with open(rel+'matches.json','w') as json_file:
    json.dump(matching,json_file)
with open(rel+'preferences.json','w') as json_file:
    json.dump(distances,json_file)