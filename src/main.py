from vector import inputVector
import json

inputvec = inputVector()
print(inputvec)
path = 'data/index/fileFreq.json'
with open(path, 'r') as dataset:
    filevec = json.load(dataset)
