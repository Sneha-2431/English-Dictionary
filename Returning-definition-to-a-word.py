import json 

data=json.load(open("data.json"))

def translate(w):  #word is a local variable passed as a parameter in the function
    return data(w)

word = input("Enter Word : ")  #word is a global variable
print (translate(word))
