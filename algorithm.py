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

def stable_roommates(preferences):
    # Initialize the roommates dictionary.
    roommates = {}
    for person in preferences:
        roommates[person] = None

    # Start the proposal process.
    proposers = list(preferences.keys())
    while proposers:
        proposer = proposers.pop()
        proposee = preferences[proposer][0]

    # If the proposee is not already paired up, then accept the proposal.
    if roommates[proposee] is None:
        roommates[proposer] = proposee
        roommates[proposee] = proposer
    else:
        # If the proposee is already paired up, then reject the proposal if they
        # prefer the proposer over their current roommate.
        if preferences[proposee][preferences[proposee].index(proposer)] < preferences[proposee][preferences[proposee].index(roommates[proposee])]:
            roommates[proposer] = proposee
            roommates[roommates[proposee]] = None
            proposers.append(roommates[proposee])

    # If anyone is not paired up, pair them up with the person who rejected
    # them last.
    for person in roommates:
        if roommates[person] is None:
            rejected_by = preferences[person][-1]
            roommates[person] = rejected_by
            roommates[rejected_by] = person

    # Return the roommates dictionary.
    return roommates

matching = stable_roommates(distances)

print(matching)
matching = {opt1:matching[opt1] for opt1 in matching}
with open(rel+'matches.json','w') as json_file:
    json.dump(matching,json_file)
