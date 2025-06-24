print ("Hello World")
a = int(input ("a: "))
b = int(input ("b: "))
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b    
def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def main():
    print("Suma:", suma(a, b))
    print("Resta:", resta(a, b))
    print("Multiplicacion:", multiplicacion(a, b))
    print("Division:", division(a, b))
if __name__ == "__main__":
    main()
    print("End of program")
    print("Goodbye")
    print ("Es solo para probar git añadido")