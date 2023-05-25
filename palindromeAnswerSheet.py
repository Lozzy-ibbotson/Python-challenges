#https://www.linkedin.com/learning/python-code-challenges/identify-a-palindrome?autoSkip=true&autoplay=true&resume=false&u=42583876
import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower())) #sanitise to remove all non alpha and convert to lowercase #same as my sanitise function
    backwards = forwards[::-1] #performs the same as my Reverse function with push and pop stack operations
    return forwards == backwards #returns boolean flag for palindrome match or not
#end def

def main():
    string = input("please enter a string: ")
    if (is_palindrome(string)):
        print(string + " is a palindrome")
    else:
        print(string + " is not a palindrome")
    #end if
#end def

main()
