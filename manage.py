from __future__ import annotations
from encrypt import Cipher
from buffer import MemoryBuffer, Text
from menu import Menu
from file_handler import FileHandler


class Mapper:
    def __init__(self, manager: Manager) -> None:
        self.manager = manager

    def map_actions(self, choice: str) -> None:
        """Map user's input choice to corresponding method and run it."""
        options = {
            "1": self.manager.execute_default_path,
            "2": self.manager.change_settings,
            "3": self.manager.save_and_quit,
            "4": self.manager.quit,
        }

        while choice not in options.keys():
            Menu.invalid_answer("action to perform")
            choice = Menu.choose()

        options.get(choice)()

    @staticmethod
    def map_rot_type(shift: str) -> str:
        """Return ROT type based on user's choice."""
        rot_types = {"1": 13, "2": 47}

        while shift not in ("1", "2", "3"):
            Menu.invalid_answer("ROT type")
            shift = Menu.choose()

        if shift == "3":
            shift = Menu.choose()

        if shift in rot_types.keys():
            return rot_types[shift]
        else:
            return shift

    @staticmethod
    def map_cipher_type(cipher_type: str) -> bool:
        """Return cipher type based on user's choice."""
        options = {"1": True, "2": False}

        while cipher_type not in options.keys():
            Menu.invalid_answer("cipher type")
            cipher_type = Menu.choose()

        return options[cipher_type]


class Manager:
    default_shift: int = 13
    default_encryptor: bool = True

    def __init__(self) -> None:
        self.running: bool = True
        self.cipher: Cipher = Cipher(Manager.default_shift, Manager.default_encryptor)

    def save_and_display_data(self, text: str, status: str):
        """Keep information about enciphered string and display the result."""
        data = Text(text, status, f"ROT{self.cipher.shift}")
        MemoryBuffer.add(data)
        print(f"Text {status}: {data.text}")

    def execute_default_path(self) -> None:
        """Run program with default settings: encryption and ROT13 algorithm."""
        text = Menu.enter_text()
        status, text = self.cipher.encipher(text)
        self.save_and_display_data(text, status)

    def execute_custom_path(self, cipher_type: str, shift: str) -> None:
        """Run program with custom settings."""
        self.cipher.encryptor = Mapper.map_cipher_type(cipher_type)
        self.cipher.shift = Mapper.map_rot_type(shift)
        text = Menu.enter_text()
        status, text = self.cipher.encipher(text)
        self.save_and_display_data(text, status)

    def quit(self) -> None:
        """Quit the program."""
        self.running = False

    def save_and_quit(self) -> None:
        """Save results and quit the program."""
        FileHandler.save_data()
        self.quit()

    def change_settings(self) -> None:
        """Change default settings."""
        Menu.show_settings_cipher_type()
        cipher_type = Menu.choose()
        Menu.show_settings_rot()
        rot = Menu.choose()
        self.execute_custom_path(cipher_type=cipher_type, shift=rot)

    def run(self) -> None:
        """Run the program."""
        Menu.show_start()

        while self.running:
            Menu.show_options()
            choice = Menu.choose()
            mapper = Mapper(self)
            mapper.map_actions(choice)
