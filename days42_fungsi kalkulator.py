def kalkulator ():
    for i in range(100):
        angka1 = int(input("angka 1 :"))
        angka2 = int(input("angka2 :"))
        operator =input("operator :")
      
        if operator == "+" :
            print (angka1 + angka2)
        elif operator == "-" :
            print ( angka1 - angka2)
        elif operator == "*" :
            print ( angka1 * angka2)
        elif operator == "/" :
            print ( angka1 / angka2)
   


kalkulator()
