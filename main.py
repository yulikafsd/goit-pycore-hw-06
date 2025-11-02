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

    def remove_phone(self, number):
        for phone_obj in self.phones:
            if phone_obj.value == number:
                self.phones.remove(phone_obj)

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
