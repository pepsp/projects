exp = input("Expression: ")
x = exp.split(" ")[0]
symbol = exp.split(" ")[1]
y = exp.split(" ")[2]

match symbol:
    case "+":
        print(float(x) + float(y))
    case "-":
        print(float(x) - float(y))
    case "/":
        print(float(x) / float(y))
    case "*":
        print(float(x) * float(y))
