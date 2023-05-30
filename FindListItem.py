#find index for all items in a list equal to a given value

#input list to search and the search value
#return indeces lists
#account for nested lists
# -- https://www.learnbyexample.org/python-nested-list/
# -- https://stackoverflow.com/questions/24180879/python-check-if-a-list-is-nested-or-not#:~:text=You%20can%20use%20isinstance%20and,within%20your%20original%2C%20outer%20list.


def getList(): #https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
    lst = []
    # number of elements as input
    size = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, size):
        ele = int(input("Please enter a list item"))
        # adding the element
        lst.append(ele)
    #end for
    return lst
#end def

#https://www.linkedin.com/learning/python-code-challenges/find-all-list-items?autoplay=true&resume=false&u=42583876
def index_All(searchList, item):
    indeces = list()
    for i in range(len(searchList)):
        if searchList[i] == item:
            indeces.append([i])
        elif isinstance(searchList[i], list):
            for index in index_All(searchList[i], item):
                indeces.append([i]+index)
            #end for
        #end if
    #end for
    print(indeces)
#end def

def myIndexAll(searchList, searchItem):
    indeces = []
    for x in range(0, len(searchList)):
        for y in range(0, x):
            if searchList[x][y] == searchItem:
                position = "[" + x + "]" + "[" + y + "]"
                indeces.append(position)
            # end if
        # end for
    # end for
    print(indeces)
#end def

def main():
    searchList = getList()
    searchItem = input("Please enter your search item: ")

    #my method
    myIndexAll(searchList, searchItem)

    #solution method
    index_All(searchList, searchItem)

#end def

main()
