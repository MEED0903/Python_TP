#****************TP1******************

a = int(input("please enter a number : "))
b = int(input("please enter another number : "))

print(f"{a} + {b} = {a+b}\n{a} - {b} = {a-b}")
#----------------------------------------------------------------------------------------------------------------------------------------------#
b = float(input(print("please enter a number in euro : ")))

print("Euro : ",b,",MAD : ",b*10.627)
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("enter a number : "))
print("int a = ",a)
b = int(input("enter another number : "))
print("int b = ",b)

if(a+b>100):
    print(f"{a+b} is Above 100",end='')
else:
    print(f"{a+b}under 100")
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("please enter a number : "))
b = int(input("please enter another number : "))
c = int(input("please enter another number : "))

max = a
if b>max:
    max = b
if c>max:
    max = c

print(f"max({a,b,c}) = {max}")
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("how many taimes do u want to echo 'la' : "))
while(a<0):
    a = int(input("how many taimes do u want to echo 'la' : "))
else : 
    i = 0
    while(i<a):
        print("la",end='')
        i+=1
#----------------------------------------------------------------------------------------------------------------------------------------------#
r = True
while(r == True):
    a = int(input("please enter a number : "))
    print(f"{a}² = {a**2}")
    c = input("Do you want to repeat the operation (Yes/No) : ")
    if(c.lower() == 'no'):
        r = False
    else:
        pass
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("please enter a number : "))
while(a%2 != 0):
    a = int(input("I've demanded an odd number, please retry : "))
else:
    print("Thank you !")
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("please enter the start : "))
b = int(input("please enter the end : "))
c = int(input("how many times do u want to repeat z : "))
for i in range(a,b+1,2):
    print("z"*c+"zigzag",i)
    if(i+1<=b):
        print(i+1,"z"*c+"zigzag")
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("please enter  a number : "))
if (a<0):
    print("The factorial is not possible for negative digits !")
else :
    if(a == 0 or a == 1):
        print(f"{a}! = 1")
    else :
        i = 1
        f = 1
        while(i<=a):
            f *= i
            i+=1
        print(f"{a}! = {f}")
#----------------------------------------------------------------------------------------------------------------------------------------------#
a = int(input("please enter a number : "))
c = ""
i = 0
while(i<a):
    b = input("enter a letter : ")
    if (b.lower() == 'stop'):
        break
    c+=f"{b} "
    i+=1
print(c)
#----------------------------------------------------------------------------------------------------------------------------------------------#
n  = int(input("please enter a number : "))
print()
print()
for i in range (1,n):
    print(f"{i}",end=', ')
print(n)
print("\n")
print()
print()
for i in range (n,1,-1):
    print(f"{i}",end=', ')
print('1')
print()
print()
for i in range (1,n,2):
    print(f"{i}",end=', ')
if n % 2 != 0 :
    print(n)
else:
    print()
    print()
for i in range(n):
    print(" "*i+"1")
print()
print()
for i in range(n-1,-1,-1):
    print(" "*i+str(i+1))


################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

#----------------------------------------------------------------------------------------------------------------------------------------------#
def valeur_abs(a):
    if a<0:
        return -a
    else :
        return a
#----------------------------------------------------------------------------------------------------------------------------------------------#
def distance_manh(xA, yA, xB, yB):
    return (valeur_abs(xA - xB) + valeur_abs(yA - yB))
#----------------------------------------------------------------------------------------------------------------------------------------------#
def signe_different(x,y):
    if(x*y<0):
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------------------------------#
def f(x):
    return (3*(x**2) + 2*x + 3)
#----------------------------------------------------------------------------------------------------------------------------------------------#
def nb_racines(a,b,c):
    print(f"A = {a}a² + {b}a + {c}")
    if a == 0:
        #print(f"x = {-c/b}")
        return 1
    else : 
        d = b**2 - 4*a*c
        if (d>0):
            """print(f"x1 = {((-b + d**0.5)/2*a):.2f}")
            print(f"x2 = {((-b - d**0.5)/2*a):.2f}")"""
            return 2
        elif (d<0):
            """print(f"x1 = {((-b + d**0.5)/2*a):.2f}")
            print(f"x2 = {((-b - d**0.5)/2*a):.2f}")"""
            return 0
        elif (d == 0):
            #print(f"x = {-b/(2*a)}")
            return 1
#----------------------------------------------------------------------------------------------------------------------------------------------#
def moyenne_ponderee(a,b,c1,c2):
    moyenne = ((a*c1)+(b*c2))/(c1+c2)
#----------------------------------------------------------------------------------------------------------------------------------------------#
def ajoute_prefixe(word,prefixe):
    return prefixe+word

def repete(word,n):
    i = 0
    c = ""
    while(i<n):
        c += word
        i+=1
    return c

def ajoute_longueur(word):
    n = len(word)
    return f"{n}{word}{n}"
#----------------------------------------------------------------------------------------------------------------------------------------------#
def compte_chiffres():
    a, b = map(int, input("Please enter two numbers seperated by a ',' : ").split(","))
    r = a * b
    print(f"{r} has {len(str(abs(r)))} digits")
    return 0
#----------------------------------------------------------------------------------------------------------------------------------------------#
def maximum(a,b):
    if(a>b):
        return a
    else:
        return b

def maximum3(a,b,c):
    if maximum(a,b)>c:
        return maximum(a,b)
    else:
        return c

def maximum3_input():
    a = int(input("please enter a number : "))
    b = int(input("please enter another number : "))
    c = int(input("please enter another number : "))
    return maximum3(a,b,c)
#----------------------------------------------------------------------------------------------------------------------------------------------#
def moyenne (n1,n2,bonus=0):
    moyenne = (n1 + n2) / 2
    moyenne +=bonus
    if moyenne>20:
        return 20
    else:
        return moyenne
def division_arrondi(a,b,round = False,decimales=0):
    if(b!=0):
        if(round == True):
            return f"{a/b:.{decimales}f}"
        else :
            return f"{a/b}"
    else:
        print("you cannot devide by 0!")
        return 0
#----------------------------------------------------------------------------------------------------------------------------------------------#
def factoriel(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factoriel(n-1)
    
def depasse(A):
    i = 1
    while(factoriel(i)<A):
        i+=1
    else:
        return i

def coeff_binomial(n,k):
    while n < 0 or k < 0 or k> n:
        return "ivalid inputs"
    coeff = factoriel(n)//(factoriel(k)*factoriel(n-k))
    return coeff

#C({n},{k}) = 

def triangle_pascal(nb_L):
    for i in range(nb_L):
        L = []
        for j in range(i + 1):
            L.append(str(coeff_binomial(i, j)))
        print(" ".join(L))
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

"""
+-------------------------------------+---------------------------------------------------------------+
| Instruction à saisir                | Résultat obtenu + Commentaire ou explication                  |
+-------------------------------------+---------------------------------------------------------------+
| maliste = [22,"coucou"....]         | Initilise the list with elements                              |
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints  list after initialisation                             | [22,"coucou",33,"z",'a','b',111,99]
+-------------------------------------+---------------------------------------------------------------+
| len(maliste)                        | returns the length of list which is in this case = 8          | len(malist) = 8
+-------------------------------------+---------------------------------------------------------------+
| 'z' in maliste                      | check if z is in the list, it will return True                | True
+-------------------------------------+---------------------------------------------------------------+
| maliste[3] = 1024                   | change the value of index 3 by 1024                           | 
+-------------------------------------+---------------------------------------------------------------+
| 'z' in maliste                      | check if z is in the list, it will return Fasle               | False
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | [22,"coucou",33,1024,'a','b',111,99]
+-------------------------------------+---------------------------------------------------------------+
| maliste.append(33)                  | Adds 33 at the end of the list                                |
+-------------------------------------+---------------------------------------------------------------+
| maliste.append("hello")             | Adds hello at the end of the list                             |
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | [22,"coucou",33,1024,'a','b',111,99,33,"hello"]
+-------------------------------------+---------------------------------------------------------------+
| maliste.remove(33)                  | removes the first 33 it incounters                            | 
+-------------------------------------+---------------------------------------------------------------+
| 33 in maliste                       | checks if 33 is present in the list it will return True       | True
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | [22,"coucou",1024,'a','b',111,99,33,"hello"]
+-------------------------------------+---------------------------------------------------------------+
| maliste.pop()                       | Removes the last element in list and returns it               | 'hello'
+-------------------------------------+---------------------------------------------------------------+
| maliste.pop(1)                       | Removes the element on index 1 it incounters                 | "coucou"
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | [22,1024,'a','b',111,99,33,"hello"]
+-------------------------------------+---------------------------------------------------------------+
| maliste.index('a')                  | returns the index of the first 'a' it incounters              | 2
+-------------------------------------+---------------------------------------------------------------+
| maliste.index(111)                  | returns the index of the first '111' it incounters            | 4
+-------------------------------------+---------------------------------------------------------------+
| maliste.sort()                      | If the elements can be compared it sorts the list (ascending by default)| Error int and elements connot be compared
+-------------------------------------+---------------------------------------------------------------+
| maliste.remove('a')                 | removes the first 'a' it incounters                           | 
+-------------------------------------+---------------------------------------------------------------+
| maliste.remove('b')                 | removes the first 'b' it incounters                           | 
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | [22,"coucou",1024,111,99,33,"hello"]
+-------------------------------------+---------------------------------------------------------------+
| maliste.sort()                      | If the elements can be compared it sorts the list (ascending by default)| Error int and elements connot be compared
+-------------------------------------+---------------------------------------------------------------+
| maliste                             | Prints the final list after modifications                     | Error int and elements connot be compared
+-------------------------------------+---------------------------------------------------------------+
| uneListe = ['z', 'a', 'd', 'aa']    | create a new list and initilize it with numbers.              | ['z', 'a', 'd', 'aa']
+-------------------------------------+---------------------------------------------------------------+
| uneListe.sort()                     | If the elements can be compared it sorts the list (ascending by default)| 
+-------------------------------------+---------------------------------------------------------------+
| uneListe                            | Prints the final list after modifications                     | ['a', 'aa', 'd', 'z']
+-------------------------------------+---------------------------------------------------------------+
"""
#----------------------------------------------------------------------------------------------------------------------------------------------#

"""
                        | instruction à taper     | résultat attendu + commentaire ou explication |
                        |-------------------------|-----------------------------------------------|
                        | maListe                 | [22,"coucou",1024,111,99,33,"hello"]          |
                        | maListe[0:3]            | [22,"coucou",1024]                            |
                        | maListe[0:4:2]          | [22,1024]                                     |
                        | maListe[0:3]            | [22,"coucou",1024]                            |
                        | maListe[:]              | [22,"coucou",1024,111,99,33,"hello"]          |
                        | maListe[:-2]            | [22,"coucou",1024,111,99]                     |
                        | maListe[::-1]           | ['hello', 33, 99, 111, 1024, 'coucou', 22]    |
                        | maListe[0]              | [22]                                          |
                        | maListe[1]              | ["coucou"]                                    |
                        | maListe[4]              | [99]                                          |
                        | maListe[5]              | [33]                                          |
                        | maListe[-1]             | ["hello"]                                     |
                        | maListe[-2]             | [33]                                          |
                        | maListe[-5]             | [1024]                                        |
                        | maListe[-6]             | ["coucou"]                                    |
                        | maListe[3]              | [111]                                         |
                        | maListe[2]              | [1024]                                        |
                        | maListe[-1] = "b"       |                                               |
                        | maListe                 | [22,"coucou",1024,111,99,33,"b"]              |
                        ---------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------------------------------------------------------#

def nb_occ(c):
    c = c.lower()
    c = ''.join(element if element.isalnum() else ' ' for element in c)
    words = c.split()
    occ = {}
    
    for word in words:
        if word in occ:
            occ[word] += 1
        else:
            occ[word] = 1
            
    return occ

def sum_values(d):
    sum = 0
    for num in d.values():
        sum += num
    return sum
#----------------------------------------------------------------------------------------------------------------------------------------------#
c = 0
def fibonacci(index):
    global c    # This will prevent raising an UnboundLocalError
    c+=1
    if (index ==0 or index == 1):
        return index
    else :
        return fibonacci(index-1)+fibonacci(index-2)
        
"""a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        c+=1
    return b"""

#fib(10) = 55
#fib(5) = 5
#fib(50) = 12586269025 
#//When using recursion it takes so long because of the case (48)  cuz the funct is being called for about 99 times!
c = 0
add = {}
def fibonacci(index):
    global c
    c += 1
    if index in add:
        return add[index]
    if index == 0 or index == 1:
        return index
    else:
        add[index] = fibonacci(index - 1) + fibonacci(index - 2)
        return add[index]


#Devoir
def dictinverse(d):
    return {value: key for key, value in d.items()}
