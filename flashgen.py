file = input("Enter file name: ") + ".md"
label = input("Label quotes by:\n[1] Tags\n[2] Section\n> ")

with open(file, "r", encoding="UTF-8") as q:
    doc = q.read()

doc = doc.split("\n")[:-1]

with open(f"{file[:file.find(".")]} Flashcards.md", "w", encoding="UTF-8") as f:
    for index, line in enumerate(doc):
        if len(line) > 2:
            start = line.find("-")
            if line[start+2] == "\"":
                line = line[start+1:].split("#")
                quote = line.pop(0)
                # Remnote exports italics as bold with spaces for some unfathomable reason
                quote = quote.replace(" __", "*").replace("__ ", "*")
                tags = [tag.replace("[", ""). replace("]", "").strip() for tag in line]

                pre = [""]
                if label == "2":
                    indent_level = len(quote[:start])
                    found_section = False
                    i = index
                    while not found_section and i > 0:
                        i -= 1
                        start = doc[i].find("-")
                        found_section = indent_level > len(doc[i][:start])
                    if found_section:
                        section = doc[i][start+2:]
                        pre.append(section + " ")
                elif label == "1":
                    if len(tags) > 0:
                        pre.append(tags[0] + " ")
                        tags.pop(0)
                if len(tags) > 0:
                    pre.append("(*")
                    pre.append(tags[0])
                    if len(tags) > 1:
                        for tag in tags[1:]:
                            pre.append(", " + tag)
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

                f.write(f"- {pre}{short} >> {quote}\n")
                print(f"{quote} flashcard added.")

