import Calculator
#user input
list1=[]
for i in range(0,10):
  element=float(input('enter a number'))
  list1.append(element)
#output result
print(Calculator.calculate(list1))