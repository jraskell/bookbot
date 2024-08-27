def main():
    book_path = "books/Frankenstein.txt"
    print(f"--- Opening {book_path} ---")
    text = get_text(book_path)
    printReport(text)



def get_text(path):
    with open(path) as f:
        return f.read()
    
def wc(text):
    words = text.split()
    return len(words)

def charcount(text):

    res = {}

    for c in text:
        c = c.lower()
        try:
            res[c] += 1
        except KeyError:
            #key doesnt' exist yet
            res[c] = 1
    return res

def printReport(text):
    word_count = wc(text)
    char_count = charcount(text)
    sorted_char_count = [{"char": key, "count": char_count[key]} for key in char_count ]
    sorted_char_count.sort(reverse=True, key=lambda x: x["count"])
    #print(sorted_char_count)
    print("===============================================")
    print(f"There are {word_count} in the document")
    print("")
    for entry in sorted_char_count:
        if entry["char"].isalpha():
            #Always hated dealing with quote ordering/mixing
            #so I prefer assigning dict entries to a simple local var to plug into the formatted string
            #keeps the string clean and easy to read
            c = entry["char"]
            i = entry["count"]
            print(f"The {c} character was found {i} times.")

main()