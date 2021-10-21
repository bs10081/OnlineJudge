def main():
    # put the number to the list and split the list
    isInput = input().split()
    # Use addSol to Calculation
    isAnser = addSol(isInput)
    # Print answer
    print(isAnser)

def addSol(isInput):
    # Set the variable to null
    isAnser = 0
    for i in range(len(isInput)):
        isAnser += int(isInput[i])
    # turn isAnser to main()
    return isAnser

if __name__ == "__main__":
    main()