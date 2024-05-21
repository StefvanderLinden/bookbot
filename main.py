def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("number of words in  file:", get_word_count(file_contents))
        print("number of characters:", get_characters_count(file_contents))

def get_word_count(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    characters_count = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    text_lowercase = text.lower()
    for c in text_lowercase:
        if c in characters_count:
            characters_count[c] += 1
    return characters_count

main()
