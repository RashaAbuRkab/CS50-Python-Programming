user = input("Greeting: ").strip().upper()
if user[0:5] == "HELLO" :
    print("$0")
elif user[0] == "H" :
    print("$20")
else:
    print("$100")
