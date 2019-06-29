# Mastering Elastic Search 6.X and Elastic Stack by Chris Fauerbach
# Document Indexes with bulk api

import requests
import csv
import json

commands = []

def commit_bulk():
    global commands
    if commands:
        commands.append("\n")
        command = "\n".join(commands)
        headers = {'Content-Type': 'application/x-ndjson'}
        result = requests.post('http://localhost:9200/cars/_bulk', data=command, headers=headers)
        print(result.text)
        commands = []

def add_car():
    global commands
    command_row = {"index":{"_type": "car"}}
    commands.append(json.dumps(command_row))
    #Bulk load sizes of 500, doubled because of command row.
    if len(commands) > 1000:
        commit_bulk()

if __name__ == "__main__":
    count = 0
    with open('vehicle.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for car in reader:
            add_car(car)
            #print(json.dumps(car))
            #count += 1
            #if count > 10:
                #sys.exit(1)
    commit_bulk()
