def create_the_dic(the_str):
    # Call the helper function
    words = split_words(the_str)
    for elem in words:
        print elem
    

def split_words(the_str):
    # The array to keep the words
    words = []
    start_of_the_word = 0
    length_of_the_word = 0
    for i, char in enumerate(the_str):
        # you need to take care of the last word as it might not end with a punctuation or space 
        # In this case the last word will be skipped!
        if i == len(the_str) - 1:
            if char.isalpha():
                length_of_the_word += 1
                word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
                words.append(word)
            else:
                word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
                words.append(word)
        elif char.isalpha():
            if length_of_the_word == 0:
                start_of_the_word = i
            length_of_the_word += 1
        else:
            word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
            words.append(word)
            length_of_the_word = 0
    return words

create_the_dic("this: is: omid.")