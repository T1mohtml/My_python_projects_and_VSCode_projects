password = "2262"

attempts = 3

while attempts > 0:
    user_input = input(
        "enter password please:   ")
    if user_input == password:
        print("access granted")
        break
    else:
        attempts -= 1
        print(f"wrong password, you have {attempts} attempts left")
        if attempts == 0:
            print("access denied, too many incorrect attempts")