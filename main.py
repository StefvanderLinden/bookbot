def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_count = get_characters_count(file_contents)
        report = get_report(word_count, character_count)
        print(report)

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

def get_report(word_count, character_count):
    def sort_on(dict):
        return dict["count"]    

    letter_count_array = []
    for k in character_count:
        single_letter_dict = {"letter":k,"count":character_count[k]}
        letter_count_array.append(single_letter_dict)

    letter_count_array.sort(reverse=True, key=sort_on)
    # [{'letter': 'e', 'count': 46043}, {'letter': 't', 'count': 30365},...

    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"there are {word_count} words found in the document\n"
    for i in letter_count_array:
        character = i["letter"]
        count = i["count"]
        report += f"the character '{character}' is found {count} amount of times\n"
    report += "--- End of report ---"
    return report

main()
