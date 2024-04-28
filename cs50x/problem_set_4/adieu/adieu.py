import inflect
p = inflect.engine()
nombres = []
while True:
   try:
     nombres.append(input("Name: "))
   except EOFError:
      print("\nAdieu, adieu, to", p.join(nombres))
      break


