def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление двух чисел с проверкой на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def calculate(operation: str, a: float, b: float) -> float:
    """Выполнение математической операции."""
    operations = {
        "add": add,
        "subtract": subtract, 
        "multiply": multiply,
        "divide": divide
    }
    
    if operation not in operations:
        raise ValueError(f"Неизвестная операция: {operation}")
    
    return operations[operation](a, b)

if __name__ == "__main__":
    # Пример использования
    try:
        result = calculate("add", 5, 3)
        print(f"Результат: {result}")
    except Exception as e:
        "divide": divide
  }

if operation not in operations:
    raise ValueError(f"Неизвестная операция: {operation}")

return operations[operation](a,b)

if __name__ == "__main__":
    #Пример использования
    try:
        result = calculate("add", 5, 3)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
