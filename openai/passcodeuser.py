users = {
    "Timo": "2262",
    "Roman": "211089",
    "Kateryna": "7777",
}
username = input("enter username please:  ")
if username in users:
    password = input("enter password please:  ")
    if users[username] == password:
        print(f"welcome back, {username}!")
    else:
        print("wrong password, try again")
else: 
    print("wrong username, try again")
