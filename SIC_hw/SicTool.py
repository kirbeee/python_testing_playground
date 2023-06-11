import SicToollib.translator

if __name__ == "__main__":
    try:
        with open("testing.txt") as file:
            SicToollib.translator.Translator(file).Printer()
    except FileNotFoundError:
        print("There just not file to translate")
