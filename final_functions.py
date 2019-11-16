from time import sleep

def go_back():
    a = 0
    while a == 0:
        back = input("Do you want to go back to the main menu?\n")
        if back == "yes" or back == "Yes" or back == "YES":
            print("Going back...")
            sleep(1)
            a = 1
        elif back == "no" or back == "No" or back == "NO":
            print("that`s ok!")
            a = 1
            boolean = 1
        else:
            print("Please choose yes or no")
            sleep(1)