import time
password = "2262"

while True:
    user_input = input(
        "enter password:  ")


    if user_input == password:
        print("Acces granted")
        time.sleep(2)
        print("joke of the day:")
        break



    else:
        print("wrong password, try again")