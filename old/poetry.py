with open("../examples/poetry.md", "r", encoding="UTF-8") as p:
    doc = p.read()

doc = doc.split("- # ")[1:]

for poem in doc:
    poem = poem.split("- ")
    title = poem[0][:-1]
    for chunk in poem[1:]:
        chunk = chunk[:-1].replace("\n", " / ")
        short = []
        for word in chunk.split():
            try:
                first_letter = word.find(next(filter(str.isalpha, word)))
                last_letter = word.rfind(next(filter(str.isalpha, word[::-1])))
                short.append(word[:first_letter+1] + word[last_letter+1:])
            except StopIteration:
                short.append(word)
        short = " ".join(short)
        print(f"({title}) " + short + " == " + chunk)
        