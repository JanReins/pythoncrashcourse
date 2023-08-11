#accepts size and t-shirt size
#print a sentence summarizing the size and message on print

def main(size, print_message):
    #size = input("Enter desired T- shirt size: \n")
    #print_message = input("Write desired statement print: \n")
    print('Size: ', size, '/', 'print message: ', print_message)


#call the function using positional arguments 

main("large", "CPA in transit")

#call for 2nd time using keyword argument

main(print_message = "CPA in transit", size = 'Large')

