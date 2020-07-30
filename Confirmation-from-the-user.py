import json 
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):  
    w = w.lower()
    if w in data:
        return data[w]  
    elif len(get_close_matches(w,data.keys()))>0: 
        yes_no=input("Did you mean %s ? Enter y is yes, or n for no." %get_close_matches(w,data.keys())[0]) 
        if yes_no == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yes_no == "n":
            return "Word does not exist. Please check it again."    
        else:
            return "We did not understand your entry."    
    else:
        return "The word does not exist. Please check it again." 

word = input("Enter Word : ") 
print (translate(word))
