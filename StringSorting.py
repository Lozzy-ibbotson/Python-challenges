#sort a list of words alphabetically
#output as entered as upper / as lower

def main():
    string = input("please enter a phrase: ")
    # https://www.w3schools.com/python/ref_string_split.asp#:~:text=The%20split()%20method%20splits,number%20of%20elements%20plus%20one.
    wordList = string.split(" ")  # split into words
    #https://stackoverflow.com/questions/13954841/sort-list-of-strings-ignoring-upper-lower-case
    wordList = sorted(wordList, key=lambda v: v.upper())
    print("sorted words: ")
    print(wordList)
#end def

main()
