import hashlib
import os


class Server:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        salt = os.urandom(16)  # Generate a random salt
        password_hash = self.generate_password_hash(password, salt)
        self.users[username] = {"password_hash": password_hash, "salt": salt}

    def authenticate(self, username, password):
        if username in self.users:
            input_password_hash = self.generate_password_hash(
                password, self.users[username]["salt"]
            )
            return self.users[username]["password_hash"] == input_password_hash
        return False

    def generate_password_hash(self, password, salt):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(password.encode("utf-8") + salt)
        return hash_algorithm.hexdigest()


class Client:
    def __init__(self):
        pass

    def register(self, server):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        server.add_user(username, password)
        print("Rejestracja zakończona pomyślnie.")

    def login(self, server):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if server.authenticate(username, password):
            print("Logowanie udane!")
        else:
            print("Logowanie nieudane.")


def main():
    server = Server()
    client = Client()

    print("Witaj w panelu klienta!")
    while True:
        print("\nWybierz działanie:")
        print("1. Zarejestruj nowe konto")
        print("2. Zaloguj się")
        print("3. Wyjdź")
        print("4. Test")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            client.register(server)
        elif choice == "2":
            client.login(server)
        elif choice == "3":
            print("Do widzenia!")
            break
        elif choice == "4":
            for username, user_data in server.users.items():
                print(username, ":", user_data)

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
