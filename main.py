import sys

from stats import count_words
from stats import count_chars

def read_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("BOOKBOT".center(50,"="))
    filePath = sys.argv[1]
    print("Analyzing book found at ",filePath,"...",sep="")
    text = read_book_text(filePath)
    print("Word Count".center(50,"-"))
    count_words(text)
    print("Character Count".center(50,"-"))
    count_chars(text)
    
    

main()