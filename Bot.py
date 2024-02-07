from AddressBook import *
from realizationIO import cli

class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(cli.input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(cli.input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            cli.print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = cli.input('Search category: ')
            pattern = cli.input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    cli.print(result)
        elif action == 'edit':
            contact_name = cli.input('Contact name: ')
            parameter = cli.input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = cli.input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = cli.input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = cli.input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = cli.input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            cli.print(self.book.congratulate())
        elif action == 'view':
            cli.print(self.book)
        elif action == 'exit':
            pass
        else:
            cli.print("There is no such command!")
