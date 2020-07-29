import json 

data=json.load(open("data.json"))

def translate(word):  #word is a local variable passed as a parameter in the function
    return data(word)

word = input("Enter Word : ")  #word is a global variable
print (translate(word))
