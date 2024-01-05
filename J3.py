#defining the instruction decoder
def decode_instruction(instruction,prev_direction):
# variable for direction we need to go
    direction = ""
    #addition the the first two numbers
    addition_of_first_two = int(instruction[0]) + int(instruction[1])
    # if the number is even then we go right
    if (addition_of_first_two % 2 == 0):
        direction = "right"
    #if the number is odd then we go left
    elif (addition_of_first_two % 2 != 0):
        direction = "left"
    #otherwise we go the previous direction
    elif (addition_of_first_two == 0):
        direction = prev_direction
    #counting the steps
    steps = instruction[2:]
    #returning the direction and steps 
    return f"{direction} {steps}"    



def main():
#Creating a list so that we can operate with each number in the numbers
    instruction = []
#Makeing a variable for previous instrusction since if the sum of the first two numbers is zero, then the direction to turn is the same as the previous instruction    
    prev_direction = ""
#While loop because we need to take input until the user inputs 99999
    while True:
        #take input
        instruction = input().strip()
        #if statement to stop when user inputs 99999
        if instruction == "99999":
            break 
        #calling the function
        code = decode_instruction(instruction,prev_direction)
        print (code)



if __name__ == "__main__":
    main()




#57234
#00907
#34100
#99999
