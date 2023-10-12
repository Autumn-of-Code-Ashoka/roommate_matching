import csv
import numpy as np
import json

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
matching = {i:pair for i,pair in enumerate(matching)}
with open(rel+'matches.json','w') as json_file:
    json.dump(matching,json_file)
