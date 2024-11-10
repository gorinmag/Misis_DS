def caches(func):
    cache = {}  # Словарь для хранения результатов

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)  # Вычисляем и кэшируем результат
        return cache[n]  # Возвращаем кэшированный результат

    return wrapper

@caches
def fibonacci(n):
    if n >= 0:
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("Число должно быть положительное")
        return None

# Пример использования
if __name__ == "__main__":
    n = -3
    print(f"Fib({n}) = {fibonacci(n)}")
    n = 20
    print(f"Fib({n}) = {fibonacci(n)}")
    n = 30
    print(f"Fib({n}) = {fibonacci(n)}")