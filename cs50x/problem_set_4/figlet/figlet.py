from pyfiglet import Figlet
import sys
import random


if len(sys.argv) == 1:
    texto_custom = input("Input: ")
    random_font = random.choice(Figlet().getFonts())
    figlet = Figlet(font=random_font)
    print("Output: \n", figlet.renderText(texto_custom))
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    f = sys.argv[2]
    lista_fuentes = Figlet().getFonts()
    if f not in lista_fuentes:
        print("Error!!!, font not found!!")
        sys.exit(1)
    else:
        texto_custom = input("Input: ")
        figlet = Figlet(font=f)
        print("Output: \n", figlet.renderText(texto_custom))
else:
    print("Provide valid arguments, loser!")
    sys.exit(1)
