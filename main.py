def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except (ValueError, IndexError):
            return "Give me name and phone please"

    return wrapper


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Added {name} with phone number {phone}"

    @input_error
    def change_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Changed phone number for {name} to {phone}"
        else:
            return f"Contact {name} not found"

    @input_error
    def show_phone(self, name):
        if name in self.contacts:
            return f"{name}'s phone number is {self.contacts[name]}"
        else:
            AddressBook
        return f"Contact {name} not found"

    def show_all(self):
        if not self.contacts:
            return "No contacts found"
        else:
            result = ""
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result

    def handle_command(self, command):
        command = command.lower()
        if command == "hello":
            return "How can I help you?"
        elif command.startswith("add "):
            parts = command.split(" ", 2)
            if len(parts) != 3:
                return "Invalid input format"
            name, phone = parts[1], parts[2]
            return self.add_contact(name, phone)
        elif command.startswith("change "):
            parts = command.split(" ", 2)
            if len(parts) != 3:
                return "Invalid input format"
            name, phone = parts[1], parts[2]
            return self.change_contact(name, phone)
        elif command.startswith("phone "):
            name = command.split(" ", 1)[1]
            return self.show_phone(name)
        elif command == "show all":
            return self.show_all()
        elif command in ("good bye", "close", "exit"):
            return "Good bye!"
        else:
            return "Unknown command"

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == ".":
                break
            response = self.handle_command(command)
            print(response)


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(phone):
        return len(phone) == 10 and phone.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
            else:
                raise ValueError("Phone number not found")


    def find_phone(self, phone):
        for p in self.phones:
            if p == phone:
                return p
        return None


from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    bot = AssistantBot()
    bot.run()
