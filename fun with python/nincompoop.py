import time


print("are you nincompoop? take the test NOW")
time.sleep(1)

user = input("are you nincompoop? y/n:    ").lower()
if user == "y":
    print("calculating answer... wait")
    time.sleep(2)
    print("you are a nincompoop!")

elif user == "n":
    confirm = input("error code 4 are you sure? y/n:").lower()
    if confirm == "y":
        print("alright then if you insist...")

        print("you are a nincompoop indeed!")
    elif confirm == "n":
        print("exactly changing answer to 'y'... recalculating...")
        time.sleep(2)
        print("you are a nincompoop indeed!")

    else:
        print("dude type y or n")
else:
    print("type y or n you nincompoop")






