#accepts size and t-shirt size
#print a sentence summarizing the size and message on print

def main(size = "Large", print_message = "I love Python"):
    #size = input("Enter desired T- shirt size: \n")
    #print_message = input("Write desired statement print: \n")
    print('Size: ', size, '/', 'print message: ', print_message)


#call the function using positional arguments 

main("large", "CPA in transit")

#call for 2nd time using keyword argument

main(print_message = "CPA in transit", size = "Medium")

# Modify the make_shirt() function so that shirts are large by default 
# with a message that reads I love Python.

main()

#Make a large shirt and a medium shirt with the default message
main(size = "Small")
main(size = "Medium")

#and a shirt of any size with a different message.
main(size = "Small", print_message = "I am doing my best")