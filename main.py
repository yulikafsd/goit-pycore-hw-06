from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(value=name)


class Phone(Field):
    def __init__(self, number):
        super().__init__(value=self.validate_number(number))

    def validate_number(self, number):
        if len(number) == 10 and number.isdigit():
            return number
        else:
            raise ValueError("Wrong number length, need 10 digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone, new_phone):
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                self.phones.remove(phone_obj)
                break
        self.phones.append(Phone(new_phone))

    def find_phone(self, number):
        found_phone = None
        for phone_obj in self.phones:
            if phone_obj.value == number:
                found_phone = phone_obj
                break
        if found_phone:
            return found_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"Record for {record.name.value} was added to the book:\n{self.data}"

    def find(self, name):
        record = self.data.get(name)
        if record:
            return record

    def delete(self, name):
        if name in self.data:
            self.data.pop(name, None)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone(
    "1234567890", "1112223333"
)  # Не удается получить доступ к атрибуту "edit_phone" для класса "str"
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone(
    "5555555555"
)  # Не удается получить доступ к атрибуту "find_phone" для класса "str"
print(
    f"{john.name}: {found_phone}"
)  # Не удается получить доступ к атрибуту "name" для класса "str"

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
