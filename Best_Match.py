import json 

data=json.load(open("data.json"))

def translate(w):  #word is a local variable passed as a parameter in the function
    w = w.lower()
    if w in data:
        return data[w]  
    elif len(get_close_matches(w,data.keys()))>0: 
        return "Did you mean %s ?" %get_close_matches(w,data.keys())[0]   
    else:
        return "The word does not exist. Please check it again." 

word = input("Enter Word : ")  #word is a global variable
print (translate(word))
