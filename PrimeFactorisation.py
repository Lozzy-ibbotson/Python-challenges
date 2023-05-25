#take integer input
#return output list of all of its prime factors
#calculation reference : https://byjus.com/maths/prime-factorization/#:~:text=The%20simplest%20algorithm%20to%20find,it%20cannot%20be%20further%20factorized.

def main():
    string = input("Please enter a whole number: ")
    try:
        integer = int(string)
        factors = get_prime_factorsSol(integer)
        print("The prime factors of your number are: ")
        print(factors)
    except:
        print("invalid input")
        main() #loop back to run the function again
    #end except
#end def

#My attempt
def get_prime_factors(integer):
    factorsfound = []
    divisor = 2
    while divisor <= integer:
        mod = integer % divisor
        if mod == 0:
            factorsfound += divisor
            integer = integer / divisor
        else:
            divisor += 1
        # end if
    #end while
    return factorsfound
#end def

#tutorial solution - https://www.linkedin.com/learning/python-code-challenges/find-prime-factors-14473085?autoplay=true&resume=false&u=42583876
def get_prime_factorsSol(integer):
    factors = list()
    divisor = 2
    while (divisor <= integer):
        if(integer % divisor) == 0:
            factors.append(divisor)
            integer = integer / divisor
        else:
            divisor += 1
        #end def
    #end while
    return factors
#end def

main()