file = input("Enter file name: ")

with open(file, "r", encoding="UTF-8") as q:
    doc = q.read()

doc = doc.split("- ")[1:]
doc = doc[doc.index("Quotes\n")+1:]
with open(f"{file[:-3]} Flashcards.md", "w", encoding="UTF-8") as e:
    for line in doc:
        if line[0] not in ["#", "\n"]:    # Remnote does not export headings with #
            line = line[:-1].split("#")
            quote = line.pop(0).replace(" __", "*").replace("__ ", "*")    # Remnote exports italics as bold with spaces
            tags = [tag.replace("[", ""). replace("]", "").strip() for tag in line]
            
            pre = [""]
            if len(tags) > 0:
                pre.append(tags[0])
                if len(tags) > 1:
                    pre.append(" (*")
                    for tag in tags[1:]:
                        pre.append(tag)
                    pre.append("*)")
                pre.append(": ")
            pre = "".join(pre)
            
            short = []
            for word in quote.split():
                try:
                    first_letter = word.find(next(filter(str.isalpha, word)))
                    last_letter = word.rfind(next(filter(str.isalpha, word[::-1])))
                    short.append(word[:first_letter+1] + word[last_letter+1:])
                except StopIteration:
                    short.append(word)
            short = " ".join(short)
            
            e.write(f"- {pre}{short} == {quote}\n")
            print(f"{quote:<20}... flashcard added.")
