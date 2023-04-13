from encrypt import Encryptor, Decryptor, Cipher
from buffer import MemoryBuffer
from filehandler import FileHandler
from typing import List, Dict, Tuple
import os.path
from dataclasses import dataclass, asdict


class Menu:
    def __init__(self) -> None:
        self.executor: Executor = Executor()
        self.running: bool = True

    def show_menu(self) -> None:
        """Display menu and interact with the user."""
        while self.running:
            text = input("Enter your text:\n")
            cypher_type = int(
                input("Choose:\n1 – to encrypt your text\n2 – to decrypt your text\n")
            )
            rot_type = int(
                input(
                    "Choose ROT type:\n1 – ROT13\n2 – ROT47\n3 – I want to enter my type of ROT (a "
                    "number)\n"
                )
            )
            if rot_type == 3:
                rot_type = int(input("Enter your type of ROT:\n"))

            self.executor.execute(cypher_type=cypher_type, text=text, shift=rot_type)

            answer = input("Do you want to enter another text? y/n\n")
            if answer == "y":
                continue
            elif answer == "n":
                save = input("Do you want to save your data? y/n\n")
                if save == "y":
                    file_name = input("Name of the file: ")
                    if os.path.exists(f"{file_name}.json"):
                        FileHandler.append_to_file(file_name, MemoryBuffer.history)
                    else:
                        FileHandler.write_to_file(file_name, MemoryBuffer.history)
                self.running = False
            else:
                raise ValueError("Invalid answer.")


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == "__main__":
    main()
