class Translator:
    def __init__(self, rawFile):
        self.file = rawFile
        self._LOC = []
        self._STATEMENT = []
        self._OBJ = []

    def analyse(self) -> tuple:
        pass

    def checker(self) -> bool:
        pass

    def Loc(self):
        pass

    def Printer(self):
        if not self._LOC:
            print("There doesn't have any location data!!")
        elif not self._STATEMENT:
            print("There doesn't have any statement data!!")
        elif not self._OBJ:
            print("There doesn't have any object code please use calculate!!")
        else:
            print("LOC", "STATEMENT", "OBJECT CODE", sep="       ")
            for i in range(max(len(self._LOC), len(self._STATEMENT), len(self._OBJ))):
                print(self._LOC[i], self._STATEMENT[i], self._OBJ[i], sep="        ")

    def Tester(self):
        self.Printer()


if __name__ == "__main__":
    try:
        with open("testing.txt") as file:
            Translator(file).Tester()
    except FileNotFoundError:
        print("There just not file to translate")
