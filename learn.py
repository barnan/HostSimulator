
################################################################################################################################
# python változó átadás:

mutable = [0, 1, 2]  # A list
mutable[0] = "x"
print(f'list (mutable): {mutable}')

not_mutable = (0, 1, 2)  # A tuple
# not_mutable[0] = "x"
print(f'tuple (not mutable): {not_mutable}')

not_mutable = "012"  # A string
#not_mutable[0] = "x"
print(f'string (not mutable): {not_mutable}')

mutable = {0, 1, 2}  # A set
mutable.remove(0)
mutable.add("x")
print(f'set (mutable): {mutable}')




def CheckId(variab:int) -> int :
    print(f'2. input id: {id(variab)}')
    variab = 20
    print(f'3. input id: {id(variab)}')
    return variab

x = 10
print(f'1. input id: {id(x)}')
ret = CheckId(x)            # a megváltozott változót adja vissza
print(f'4. input id: {id(x)}')
print(f'5. input id: {id(ret)}')


################################################################################################################################
# python interface:

#informális interface-ek:
class InformalInterface :

    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass
    
# konkrét osztály:
class PdfParser(InformalInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalInterface.extract_text()"""
        pass

class EmlParser(InformalInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalInterface.extract_text()
        """
        pass

################################################################################################################################
# python classes:

class MyClass :

    # az init felel az objektum inicilizálásáért, nem ad vissza semmit
    def __init__ (selfy, name:str, age:int) :
        selfy.name = name
        selfy.age = age

    # ez (new) felel az objektum kreálásért, visszaad egy példányt az adott osztályból (amire ezután rögtön az init hívódik meg)
    # def __new__() :

    # pythonban nincs metod overloading (egy dict tárolja a metódus neveket a namespace-ben)(és egyébként az elérhető változó neveket is)

    # olyasmi mint c# ban a ToString()
    def __str__(selfy) -> str : 
        return f'The name {selfy.name} and age: {selfy.age}'

    def myMethod(selfy) -> None :
        print(f'MyClass {selfy.age}')
        return

    def myMethod2(selfy) -> None :
        pass # -> ezt akkor használjuk, ha nem akarunk semmit a metódustörzsbe vagy osztálytörzsbe írni
    
myClass2 = MyClass('John',20)
myClass3 = MyClass('John',50)

print(myClass2.age)
print(myClass2)
myClass2.myMethod()

del myClass2        # objektum törlése

################################################################################################################################
# python derived classes:
 
class DerivedClass(MyClass) :

    def __init__(self, age:int, name:str, address:str) :
        MyClass.__init__(self, name, age)                       # ha az osztály nevével írjuk érjük el az ősosztályt, akkor kell a metódus paraméterbe a 'self' paraméter
        self.address = address

    def __str__(self) -> str :
        return f'{super().__str__()} and address: {self.address}'       # ha superrel érjük el az őst, akor nem kell bele a 'self' paraméter a metódushívásba


derived = DerivedClass(34, 'Johny', 'Budapest')
print(derived)


x = "awesome"
y = 'good'

def myfunc():
    x = 'fantastic'         # csak a metóduson belül kap új értéket
    print("Python is " + x + ' ' + y)

myfunc()

print("Python is " + x + ' ' + y) 


################################################################################################################################
# list: lehet benne duplikáció és többféle típus is
# indexelhető, megváltoztatható

xList = [10, 15, 20, 10]
yList = list()
yList.append(30)

yList[0] = 70

################################################################################################################################
# tuple: lehet benne duplikáció és többféle típus is
# indexelhető, IMMUTABLE

xTuple = (10, 20, 30, 10)

################################################################################################################################
# set: a benne lévő elemek nem megváltoztathatóak!
# nem rendezett, a benne lévő elemek más sorrendben jöhetnek elő (?) és nem indexelhető

xSet = {'10', 30, 30, 'tiz'}
# xSet[1] = '50' # ez exceptiont okoz

################################################################################################################################
# dictionariy: kulcs-érték párok. az elemek megváltoztathatóek, de a sorrend nem rendezett
dict = {}

try :
    dict['valami'].append(20)
except KeyError :
    dict['valami'] = []

try :
    dict['valami'].append(20)
except KeyError :
    dict['valami'] = []

################################################################################################################################
# metódusok:

# C# params-nak a *args felel meg (ilyenkor nem tudjuk pontosan hány paraméter érkezik be) -> ilyenkor tuple-nek veszi az inputot
# ha nem tudjuk hány nevesített argumentm érkezik be akkor lehet **kwargs-ot írni, ekkor dictinoary-ben érkeznek be az argumentumok
# lehet default paramétereket definiálni


################################################################################################################################
# lambda:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 


################################################################################################################################
# exception handling:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") 
finally:
    print('this is will definitly hit')


################################################################################################################################
# user input:
print('enter someting:')
valami = input()
print(valami)


################################################################################################################################
# https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
# tkinter

