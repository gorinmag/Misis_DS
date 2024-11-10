class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Максимальная вместимость кэша
        self.cache_dict = {}  # Словарь для хранения кэша
        self.order = []  # Список для отслеживания порядка использования

    @property
    def cache(self):
        # Возвращает самый старый элемент в кэше
        if self.order:
            oldest_key = self.order[0]
            return (oldest_key, self.cache_dict[oldest_key])
        return None

    @cache.setter
    def cache(self, new_elem):
        # Проверяем, что новый элемент - это кортеж из двух элементов
        if isinstance(new_elem, tuple) and len(new_elem) == 2:
            key, value = new_elem  # Извлекаем ключ и значение из нового элемента
            if key in self.cache_dict:
                # Если ключ уже существует, обновляем значение и порядок
                self.cache_dict[key] = value
                self.order.remove(key)
                self.order.append(key)
            else:
                # Если ключ новый, добавляем его в кэш
                if len(self.cache_dict) >= self.capacity:
                    # Если кэш переполнен, удаляем самый старый элемент
                    oldest_key = self.order.pop(0)  # Удаляем самый старый ключ
                    del self.cache_dict[oldest_key]  # Удаляем элемент из кэша
                self.cache_dict[key] = value  # Добавляем новый элемент
                self.order.append(key)  # Обновляем порядок использованных ключей
        else:
            print("Ошибка: новый элемент должен быть кортежем из двух элементов (ключ, значение).")

    def get(self, key):
        # Метод для получения значения по ключу
        if key in self.cache_dict:
            # Если ключ существует, обновляем порядок
            self.order.remove(key)
            self.order.append(key)
            return self.cache_dict[key]
        return None  # Если ключ не найден, возвращаем None

    def print_cache(self):
        # Метод для вывода текущего состояния кэша
        print("LRU Cache:")
        for key in self.order:
            print(f"{key} : {self.cache_dict[key]}")

# Пример использования
if __name__ == "__main__":
    cache = LRUCache(3)  # Создаем экземпляр кэша с вместимостью 3
    cache.cache = ("key1", "value1")  # Добавляем элементы в кэш
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")
    cache.print_cache()  # Выводим текущий кэш
    print(cache.get("key2"))  # Получаем значение по ключу "key2"
    cache.cache = ("key4", "value4")  # Добавляем новый элемент, превышающий лимит
    cache.print_cache()  # Выводим обновленный кэш
