def reverse_words(message):

    # Decode the message by reversing the words
    for i in range(len(message)):
        if message[i] != ' ':
            message.insert(len(message) - 1, message.pop(0))
        else:
            message.insert(0, messa)
            
        
    return message

message = list('vailt cake')
print reverse_words(message)