# Zander Poole
# EE361
# Project 3
# sortWords.py


def sortWords(listOfWords, length):
    countDict = {}  # Initializing a dictionary for word count

    for item in listOfWords:  # Generate dictionary of counts
        if len(item) == length:  # Checking all words at the user defined length
            if item in countDict:  # If the word is already in the dictionary, add one to the count
                countDict[item] = countDict[item] + 1
            else:  # If the word is not already in the dictionary, start count
                countDict[item] = 1
    sortedDict = sorted(countDict.items(), key=lambda x: x[1],
                        reverse=True)  # Sort the dictionary in decending order according to frequency
    return sortedDict


# ---------------------------------------------- FOR TEST --------------------------------------------------------------
# def main():
#     iList = ["the", "the", "the", "pie",
#     "child", "word", "word", "me", "she", "she", "he", "word", "Hello", "world", "cat", "dog", "sun", "moon", "tree",
#     "flower", "rain", "snow", "beach", "mountain", "city", "country", "house", "car", "train", "plane", "boat",
#     "bicycle", "computer", "phone", "television", "book", "pen", "pencil", "paper", "chair", "table", "bed", "lamp",
#     "door", "window", "wall", "floor", "ceiling", "sky", "cloud", "wind", "fire", "water", "earth", "air", "music",
#     "art", "dance", "film", "theater", "science", "mathematics", "history", "language", "culture", "food", "drink",
#     "love", "hate", "happy", "sad", "angry", "fear", "joy", "surprise", "excitement", "boredom", "sleep", "awake",
#     "dream", "reality", "imagination", "memory", "thought", "emotion", "behavior", "habit", "routine", "friend",
#     "family", "work", "play", "study", "learn", "teach", "help", "hurt", "forgive", "forget", "remember", "give",
#     "take", "buy", "sell", "eat", "drink", "sleep", "wake", "family", "work", "play", "study", "learn", "teach",
#     "help", "hurt", "forgive", "forget", "remember", "give", "take", "buy", "sell", "eat", "drink", "sleep", "wake",
#     "family", "work", "play", "study", "learn", "teach", "help", "hurt", "forgive", "forget", "remember", "give",
#     "take", "buy", "sell", "eat", "drink", "sleep", "wake", "family", "work", "play", "study", "learn", "teach",
#     "help", "hurt", "forgive", "forget", "remember", "give", "take", "buy", "sell", "eat", "drink", "sleep", "wake"]
#
#     print(sortWords(iList, 3))
#
#
# if __name__ == '__main__':
#     main()
