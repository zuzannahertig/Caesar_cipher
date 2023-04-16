import warnings
from custom_warnings import EnteredEmptyString


class Menu:
    @staticmethod
    def show_start() -> None:
        """Display information about the program."""
        print(
            "This program lets you encrypt any text using Caesar cipher.\n"
            "The default settings are: encryption and ROT13 algorithm, but you can change them at any time.\n"
        )

    @staticmethod
    def show_options() -> None:
        """Display options."""
        print(
            "Choose:\n"
            "1 – to enter the text\n"
            "2 – to change the default settings\n"
            "3 – to save the data and quit\n"
            "4 – to quit without saving.\n"
        )

    @staticmethod
    def show_settings_cipher_type() -> None:
        """Display available cipher types."""
        print("Choose:\n" "1 – to encrypt\n" "2 – to decrypt\n")

    @staticmethod
    def show_settings_rot() -> None:
        """Display available ROT types."""
        print(
            "Choose:\n"
            "1 – to choose ROT13 algorithm\n"
            "2 – to choose ROT47 algorithm\n"
            "3 – to set algorithm's shift\n"
        )

    @staticmethod
    def invalid_answer(operation: str) -> None:
        """Display invalid answer message."""
        print(
            f"Invalid option chosen for {operation}. Please choose one of the available options."
        )

    @staticmethod
    def enter_text() -> str:
        """Enter text to encipher."""
        text = input("Enter your text:\n")
        text = text.strip()
        if len(text) == 0:
            warnings.warn(
                "Empty string cannot be enciphered.",
                EnteredEmptyString,
            )
        return text

    @staticmethod
    def choose() -> str:
        """Enter your choice."""
        return input()


def main():
    menu = Menu()
    menu.show_start()


if __name__ == "__main__":
    main()
