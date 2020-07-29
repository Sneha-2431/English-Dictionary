import json 

data=json.load(open("data.json"))

def translate(w):  #word is a local variable passed as a parameter in the function
    if w in data:
        return data[w]  
    else:
        return "The word does not exist. Please check it again." 

word = input("Enter Word : ")  #word is a global variable
print (translate(word))
