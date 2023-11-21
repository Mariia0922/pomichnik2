def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"

    return wrapper

class ContactAssistant:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change_contact(self, name, phone):
        if name not in self.contacts:
            raise IndexError
        self.contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"

    @input_error
    def show_phone(self, name):
        if name not in self.contacts:
            raise IndexError
        return f"Phone number for {name}: {self.contacts[name]}"

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found."
        result = "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())
        return result

    @input_error
    def main(self):
        while True:
            command = input("Enter command: ").lower()
            if command in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command.startswith("add"):
                _, name, phone = command.split(" ", 2)
                print(self.add_contact(name, phone))
            elif command.startswith("change"):
                _, name, phone = command.split(" ", 2)
                print(self.change_contact(name, phone))
            elif command.startswith("phone"):
                _, name = command.split(" ", 1)
                print(self.show_phone(name))
            elif command == "show all":
                print(self.show_all_contacts())
            else:
                print("Unknown command. Try again.")

if __name__ == "__main__":
    assistant = ContactAssistant()
    assistant.main()
