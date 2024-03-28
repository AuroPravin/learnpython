# Task (lang code to identify)

'''
def check():
    lang=input("Enter the language code: ")
    if(lang=="en"):
        print("English language is Indicated as:",lang)
    elif(lang=="fr"):
        print("French language is indicated as: ",lang)
    else:
        print("limited language code are available")

check()

'''
'''
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

'''

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)