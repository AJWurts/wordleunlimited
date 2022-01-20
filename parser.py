import re

with open("more_words.txt") as wordFile:
    
    words = wordFile.read().split('\n')

    parsedWords = ''

    for line in words:
        word = line.split(' ')[0]
        if len(word) < 4:
            continue
        word = re.sub(r'[0-9]+', '', word)
        parsedWords += word.lower() + '\n'

    with open("parsed_words.txt", "w") as outputFile:
        outputFile.write(parsedWords)

    