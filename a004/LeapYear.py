def main():
    try:    # try to run
        while True:
            # input the year
            cin = int(input())
            # output answer
            if judgeLeap(cin):
                print("閏年")
            else:
                print("平年")

    except EOFError:    # if error then pass
        pass

def judgeLeap(cin):
    return cin % 400 == 0 or (cin % 100 != 0 and cin % 4 == 0)


if __name__ == "__main__":
    main()