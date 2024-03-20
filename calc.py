#calculator
# ADD
def add(n1, n2):
    return n1 + n2
#subract
def subract(n1,n2):
    return n1-n2
#multiply
def multiply(n1,n2):
    return n1*n2
#divide
def divide(n1,n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : subract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))


for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

calculation_func = operations[operation_symbol]
answer =  calculation_func(num1,num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")
