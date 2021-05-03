def year_1(x):
    if x % 4 == 0:
        if x % 100 != 0:
            print("True")
        elif x % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("False")
year_1(int(input("Year:\n")))
