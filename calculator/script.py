import time
def calculator() -> object:
    """

    :rtype: object
    """
    print("just a calculator")

    num1 = float(input("type your first number:   "))
    print("choose what you need")
    print("1 - plus")
    print("2 - minus")
    print("3 - multiplication")
    print("4 - division")

    operation = input("your choice  (1/2/3/4) :")
    num2 = float(input("type second number:"))
    print("calculating answer...please wait")
    time.sleep(2)
    if operation =='1' :
        print(f"result: {num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"result: {num1} - {num2} = {num1 - num2}")
    elif operation == '3' :
        print(f"result : {num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 == 0:
            return
        print(f"result: {num1} / {num2} = {num1 / num2}")


object = calculator()