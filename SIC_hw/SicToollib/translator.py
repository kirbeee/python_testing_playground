import re
class Translator:
    def __init__(self, rawFile):
        self.file = rawFile
        self._LOC = []
        self._STATEMENT = []
        self._OBJ = []
        self.__analyse(rawFile)

    def __analyse(self,file):
        print(file.readline().split(" "))
        temp = re.split(' |\n|\t',file.read())
        temp = [value for value in temp if value != ""]
        for i in range(len(temp)//6):
            self._LOC.append(temp[i*6+1])
            self._STATEMENT.append([temp[i*6+2],temp[i*6+3],temp[i*6+4]])
            self._OBJ.append(temp[i*6+5])
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


