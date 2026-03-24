import json

#This determines how likely each feature is to appear in a given piece.
#Odds values are given in percentages.
odds_list = [
    {"oid": 1, "odds": "67", "name": "Chordal Lines"},
    {"oid": 2, "odds": "54", "name": "Fibonacci Lines"},
    {"oid": 3, "odds": "72", "name": "Tri-Wave"},
    {"oid": 4, "odds": "78", "name": "Fibonacci Tri-Wave"},
    {"oid": 5, "odds": "46", "name": "Chordal Tri-Wave"},
    {"oid": 6, "odds": "90", "name": "Gradient Rects"}
]

#This is the default settings for running quick mode.
preset_list = [
    {"filename": "n"},
    {"overwrite":"n"},
    {"output_mode":"1"},
    {"seed":"1"},
    {"seq_min":"0"},
    {"seq_max":"100"},
    {"seq_step":"1"}
]



with open("odds_table.json", "w") as file:
    json.dump(odds_list, file, indent=4)

with open("preset_table.json", "w") as file:
    json.dump(preset_list, file, indent=4)

print('Data table(s) updated!')
