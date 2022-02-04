import requests, json

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

class City:
    def __init__(self, name):
        self.name = name

    def getCity(self):
        pass


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
        self.visited = False

