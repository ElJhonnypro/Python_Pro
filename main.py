meme_dict = {
    "cringe": "Algo embarazante",
    "lol": "algo increible o gracioso"
}


word = input('palabra que no sepas:').lower()

if word in meme_dict.keys():
    print(f"la palabra {word} significa {meme_dict[word]}")
else:
    print("No conocemos esa palabra")