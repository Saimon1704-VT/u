def divide(a,b):
    if a < b:
        return 0
    return 1 + divide(a-b,b)
print ("El resultado es: ",divide(10,2))