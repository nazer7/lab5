import re
text=input("enter word-")
def text_match(text):
        patterns = r'^ab{2,3}$' 
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match(text))
