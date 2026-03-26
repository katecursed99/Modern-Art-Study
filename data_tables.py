import json

#This determines how likely each feature is to appear in a given piece.
#Odds values are given in percentages.
odds_list = [
    {"oid": 1, "odds": "67", "name": "Chordal Lines"},
    {"oid": 2, "odds": "54", "name": "Fibonacci Lines"},
    {"oid": 3, "odds": "72", "name": "Tri-Wave"},
    {"oid": 4, "odds": "78", "name": "Fibonacci Tri-Wave"},
    {"oid": 5, "odds": "46", "name": "Chordal Tri-Wave"},
    {"oid": 6, "odds": "90", "name": "Gradient Rects"},
    {"oid": 7, "odds": "90", "name": "Triangle"},
    {"oid": 8, "odds": "90", "name": "Arrow"},
    {"oid": 9, "odds": "90", "name": "Sine Wave"}
]

#These are the default settings for running quick mode. The actual JSON
#gets updated by the user's inputs
preset_list = [
    {"name":"filename", "value":"n"},
    {"name":"overwrite", "value":"n"},
    {"name":"output_mode", "value":"1"},
    {"name":"seed", "value":"1"},
    {"name":"seq_min", "value":"0"},
    {"name":"seq_max", "value":"150"},
    {"name":"seq_step", "value":"1"}
]

with open("preset_table.json", "w") as file:
    json.dump(preset_list, file, indent=4)

with open("odds_table.json", "w") as file:
    json.dump(odds_list, file, indent=4)



print('Data table(s) updated!')
