def main():
    # input number to the map and split list
    isMonth, isDay = map(int,input().split())
    # use findSol to Calculation
    S = findSol(isMonth, isDay)
    # output the answer
    if S == 0:  
        print("普通")
    elif S == 1:
        print("吉")
    else:
        print("大吉") 

def findSol(isMonth, isDay):
    # Logic
    S = (isMonth * 2 + isDay) % 3
    return S

if __name__ == "__main__":
    main()