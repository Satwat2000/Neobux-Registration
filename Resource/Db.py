import json

def update(Class,value):
    jsonFile = open("Data.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    # tmp = data["location"] 
    for key, value in value.items():
        data[Class][key] = value

    ## Save our changes to JSON file
    jsonFile = open("Data.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

def get_val():
    jsonFile = open("Data.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    return data

# def update(value):  
#     db = open('Data.json','a')
#     json.dump(value,db)
#     db.close()

# a ={'1':,"2":2}
# update(a)