class Client:  # Создание класса
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):  # Метод перевода данных в строку
        return f"\"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.\""

    def get_guest(self):  # Ограничение для вывода данных
        return f"{self.name}, {self.surname}, {self.city}."


#  Создание клиентов

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Виталий", "Козлов", "Северодвинск", 32)
client_3 = Client("Мария", "Власова", "Екатеринбург", 24)

client = [client_1, client_2, client_3]  # Создание списка клиентов

for x in client:  # Цикл поочередного вывода клиентов
    print(x.get_guest())

print(client_1)  # Вывод в строку одного клиента
