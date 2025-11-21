# Калькулятор с преднамеренными ошибками для Code Review

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    # Проблема: нет проверки деления на ноль
    result = a / b
    return result

def calculate(operation, x, y):
    # Проблема: плохая структура if-elif
    if operation == "add":
        return add(x, y)
    if operation == "subtract":
        return subtract(x, y)
    if operation == "multiply":
        return multiply(x, y)
    if operation == "divide":
        return divide(x, y)
    # Проблема: нет обработки неверной операции

# Проблема: код без main guard
print("Результат:", calculate("add", 5, 3))
 return subtract(x, y)
    if operation == "multiply":
        return multiply(x, y)
    if operation == "divide":
        return divide(x, y)
    # Проблема: нет обработки неверной операции

# Проблема: код без main guard
        return subtract(x, y)
  if operation == "multiply":
      return multiply(x, y)
  if operation == "divide":
      return divide (x,y)
  # Проблема: нет обработки неверной операции

# Проблема: код без main guard
print ("Результат:", calculate("add", 5, 3))
