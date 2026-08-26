# Клас Subject - це предмет, який має назву та тип (обов'язковий чи ні)
class Subject:
    # Конструктор - створює новий предмет з назвою та типом
    def __init__(self, name, type):

        self.name = name  # назва предмета
        self.type = type  # тип предмета (обов'язковий чи ні)



# Створюємо тестовий предмет для перевірки
subject1 = Subject("Computer Science", "necessarily")

