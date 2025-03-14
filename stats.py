def count_words(text):
    words = text.split()
    print(len(words)," words found in the document")
    
def count_chars(text):
    words = text.split()
    char_dict = dict()
    for word in words:
        for char in word:
            char = char.lower()
            if(not char.isalpha()):
                continue
            if(char in char_dict.keys()):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    # char_dict.sort(reverse=True)
    # for letter in char_dict:
    #     print(letter," : ",char_dict[letter])
    order_chars(char_dict)

def order_chars(char_dict):
    charList = [{"char": letter,"count": char_dict[letter]} for letter in char_dict]
    charList.sort(reverse=True, key=order)
    for letter in charList:
        print(letter["char"],":",letter["count"])
        
        
def order(charList):
    return charList["count"]
    
    