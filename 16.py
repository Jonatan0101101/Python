def invertir(a):
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r
# pp
b= input("Introduir una paraula")
c= invertir(b)
print("La paraula",b,"Si la girem es",c)
