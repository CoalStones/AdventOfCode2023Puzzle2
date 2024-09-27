from time import sleep


def wordToNum(string):
    string_to_int_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    return string_to_int_map.get(string, None)  # Returns None if the string is not found

if __name__ == "__main__":
    coords = open("coords.txt","r")
    array = []
    for xy in coords:
        array.append(xy.strip())
    coords.close()

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    wordNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

    sum = 0
    # for each line in the array...
    for x in array:
        one = False
        first = ""
        second = ""
        wordNumber = ""
        # for each character in the line...
        for y in x:
            # print(y)
            # if the character is a number...
            if y in numbers:
                if one == False:
                    first = y
                    one = True
                    # print("Found the first number!")
                else:
                    # print("any truers?", end=" ")
                    second = y
                    # print("Found the second number!")
            # elif any(y in word for word in wordNumbers):
            #     print(any(y in word for word in wordNumbers))

            #determines if the substring is in the wordNumbers list
            isInWord = False
            for word in wordNumbers:
                print("word: " + word + " y: " + y, end=" ")
                # if the character is part of a number
                if(y in word):
                    print("y is in word")
                    wordNumber += y
                    isInWord = True
                    break
            
            #resets the word if the substring is not in the wordNumbers list
            #TODO: remove debugging
            print("wordNumber: " + wordNumber)
            sleep(1)
            #TODO: if multiple characters belong to different words but together are not a number
            # it does not reset the wordNumber leading to cases such as znn where the second n could be nine but will
            # never be recognized as such because it would be znnine, please fix
            if isInWord == False:
                wordNumber = ""
                print("resetting wordNumber")
            elif isInWord == True:
                print("wordNumber: " + wordNumber)
                if wordNumber in wordNumbers:
                    if one == False:
                        first = wordToNum(wordNumber)
                        one = True
                        # print("Found the first number!")
                    else:
                        second = wordToNum(wordNumber)
                        # print("Found the second number!")
                    wordNumber = ""
                
        if one == True:
            if second == "":
                second = first
            toAppend = first + second
            print("toAppend " + toAppend + " first: " + first + " second: " + second + " line: " + x)
            sum += int(toAppend)
    print(sum)
