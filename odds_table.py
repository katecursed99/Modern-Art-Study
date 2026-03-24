import json

data_list = [
    {"id": 1, "odds": "45", "name": "Chordal Lines"},
    {"id": 2, "odds": "45", "name": "Fibonacci Lines"},
    {"id": 3, "odds": "45", "name": "Tri-Wave"},
    {"id": 4, "odds": "45", "name": "Fibonacci Tri-Wave"},
    {"id": 5, "odds": "45", "name": "Chordal Tri-Wave"},
    {"id": 6, "odds": "45", "name": "Gradient Rects"}
]

with open("odds_table.json", "w") as file:
    json.dump(data_list, file, indent=4)
