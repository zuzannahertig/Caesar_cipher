from menu import Menu


class Manager:
    @staticmethod
    def run():
        menu = Menu()
        menu.show_menu()


def main():
    Manager.run()


if __name__ == '__main__':
    main()
