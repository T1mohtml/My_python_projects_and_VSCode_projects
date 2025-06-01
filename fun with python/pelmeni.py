A = "OK"
B = "Well, do you have anything else?:  "
C = "Well, then I guess you need to buy kebab for dinner."
D = "Well then cook it you lazy a**".upper()
# Here we have all my variables

pelmeni = input("Did you cook the pelmeni? ").lower()
# This is an input field

if pelmeni == "yes":
    print(A)
elif pelmeni == "no":
    second_food = input(B).lower()
    if second_food == "no":
        print(C)
    elif second_food == "yes":
        print(D)
    else:
        print("Please answer 'yes' or 'no'.")
else:
    print("Please answer 'yes' or 'no'.")