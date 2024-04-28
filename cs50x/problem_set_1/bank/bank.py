answer = input("Greeting: ").casefold()
x = answer.find("h")

if "hello" in answer:
    print("$0")
elif x == 0:
    print("$20")
else:
    print("$100")
