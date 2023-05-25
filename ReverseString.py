# --> Code to demonstarte how a stack can be used to reverse a string
# --> Based on the tutorial from the link below
# --> https://www.geeksforgeeks.org/stack-set-3-reverse-string-using-stack/

# --> index [-1] ise defined as the 'top' of the stack

#---------- GENERAL FUNCTIONS -----------

def CreateStack():
	#instantiate list as Stack
	Stack = []
	return Stack
#end def

def SizeOfStack(Stack):
	return len(Stack)
#end def

def IsEmpty(Stack):
	if SizeOfStack(Stack) == 0:	#ie the stack contains no data
		return True
	#end if
#end def

#---------- PUSH AND POP OPERATIONS -----------

def push(Stack, item):
	#LIFO data structure therefore, push item onto the top of the stack
	Stack.append(item)
	#Stack size has increased by 1
#end def

def pop(Stack):
	#LIFO data structure therefore, pop item from the top of the stack
	if IsEmpty(Stack):
		print("There is no data to pop from the stack")
		return
	else:
		return Stack.pop()
	#end if
		
#end def

#---------- FUNCTION TO REVERSE THE STRING -----------

def Reverse(string):
#get the length of the user input string
	length = len(string)
	
	#Create an empty stack
	Stack = CreateStack()
	
	#Push all characters from the string onto the stack
	#iterate through the string
	for character in range(0, length):
	#add character to stack
		push(Stack, string[character])
	#end for
	
	#empty the string since all characters are now stored in stack
	string = ""
	
	#pop all charcaters off the stack and back into the string
	for index in range(0, length):
		string += pop(Stack)
	#end for
	
	#return the result to the main function
	return string
#end def


#---------- MAIN FUNCTION -----------

def main():
	#instantiate string
	string = input("Please enter your string: ")
	#store the result of the function
	string = Reverse(string)
	#output the result
	print ("Your string reversed is: ", string)
#end def

#---------- CALL MAIN FUNCTION -----------
main()
