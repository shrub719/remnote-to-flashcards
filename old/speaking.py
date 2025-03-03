with open("../examples/speaking.txt", "r", encoding="utf-8") as s:
    doc = s.read()
    
doc = doc.split("Theme ")

split_doc = []
for theme in doc:
    theme = theme.split("\n\n")
    
    split_theme = []
    for question in theme:
        question = question.split("\n")
        split_theme.append(question)
        
    split_doc.append(split_theme)
    
flashcards = []
for theme in split_doc:
    for question in theme:
        if len(question) == 3:
            flashcard = question[0] + " == " + question[2]
            flashcards.append(flashcard)

for flashcard in flashcards:
    print(flashcard)