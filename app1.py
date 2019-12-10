import json

data = json.load(open('data.json'))


def translate(w ):
    w=w.lower()

    if w in data:
        return data[w]
        print("please try again")
    else:
        return "this is not a word try again"


word = input('enter a word:   ')

print(translate(word))
