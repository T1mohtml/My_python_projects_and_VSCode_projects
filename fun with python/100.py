
passcode = "2222"

while True:
    user_input = input("Enter the passcode: ")
    if user_input == passcode:
        for i in range(1):
            print(f"hello user, just a reminder your password is {passcode}")
        break
    else:
        print("Access denied.")