import re

OPCODE = diction = {
    "ADD": "18",
    "ADDF": "58",
    "ADDR": "90",
    "AND": "40",
    "CLEAR": "B4",
    "COMP": "28",
    "COMPF": "88",
    "COMPR": "A0",
    "DIV": "24",
    "DIVF": "64",
    "DIVR": "9C",
    "FIX": "C4",
    "FLOAT": "C0",
    "HIO": "F4",
    "J": "3C",
    "JEQ": "30",
    "JGT": "34",
    "JLT": "38",
    "JSUB": "48",
    "LDA": "00",
    "LDB": "68",
    "LDCH": "50",
    "LDF": "70",
    "LDL": "08",
    "LDS": "6C",
    "LDT": "74",
    "LDX": "04",
    "LPS": "E0",
    "UML": "20",
    "MULF": "60",
    "MULR": "98",
    "NORM": "C8",
    "OR": "44",
    "RD": "D8",
    "RMO": "AC",
    "RSUB": "4C",
    "SHIFTL": "A4",
    "SHIFTR": "A8",
    "SIO": "F0",
    "SSK": "EC",
    "STA": "0C",
    "STB": "78",
    "STCH": "54",
    "STF": "80",
    "STI": "D4",
    "STL": "14",
    "STS": "7C",
    "STSW": "E8",
    "STT": "84",
    "STX": "10",
    "SUB": "1C",
    "SUBF": "5C",
    "SUBR": "94",
    "SVC": "B0",
    "TD": "E0",
    "TIO": "F8",
    "TIX": "2C",
    "TIXR": "B8",
    "WD": "DC"
}


class Translator:
    def __init__(self, rawFile):
        self.file = rawFile
        self._LOC = []
        self._STATEMENT = []
        self._OBJ = []
        self.__analyse(rawFile)

    def __analyse(self, file):
        print(file.readline().split(" "))
        temp = re.split(' |\n|\t', file.read())
        temp = [value for value in temp if value != ""]
        for i in range(len(temp) // 6):
            self._LOC.append(temp[i * 6 + 1])
            self._STATEMENT.append([temp[i * 6 + 2], temp[i * 6 + 3], temp[i * 6 + 4]])
            # self._OBJ.append(temp[i * 6 + 5])

    def checker(self) -> bool:
        pass

    def Loc(self):
        pass

    def objCode(self):
        for i in range(len(self._STATEMENT)):
            if self._STATEMENT[i][1] in diction:
                answer = diction[self._STATEMENT[i][1]]

                for j in range(len(self._STATEMENT)):
                    if self._STATEMENT[i][2] == "None":
                        break
                    if self._STATEMENT[i][2] ==self._STATEMENT[j][0]:
                        answer += self._LOC[j]
                        break
                if len(answer) != 6:
                    self._OBJ.append(answer+"0000")
                else:
                    self._OBJ.append(answer)
            elif self._STATEMENT[i][1] == "BYTE":
                if self._STATEMENT[i][2] == "C'EOF'":
                    self._OBJ.append("454F46")
                else:
                    return self._STATEMENT[i][2].split("C'").split("'")
            elif self._STATEMENT[i][1] == "WORD":
                self._OBJ.append(  format(int(self._STATEMENT[i][2]), '06X'))
            else:
                self._OBJ.append("None")

    def Printer(self):
        self.objCode()
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
        self.objCode()
