def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    wordArray = []
    reversedWord = ""
    numberOfStringPairs = 0

    for i in range(len(words)):

        if i == len(words) - 1: return numberOfStringPairs
        
        for j in range(i + 1, len(words)):

            for letter in words[j]:
                wordArray.append(letter)
            wordArray.reverse()
            for letter in wordArray:
                reversedWord += letter
            if words[i] == reversedWord:
                numberOfStringPairs += 1
            
            wordArray = []
            reversedWord = ""
    return numberOfStringPairs
            




