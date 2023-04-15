from menu import Menu
from typing import Tuple
from encrypt import Encryptor, Decryptor, Cipher
from buffer import MemoryBuffer, Text


class Executor:
    @staticmethod
    def map_rot_type(shift: int) -> int:
        """Return ROT type based on user's choice."""
        rot_types = {1: 13, 2: 47}
        if shift in rot_types.keys():
            return rot_types[shift]
        else:
            return shift

    @staticmethod
    def encrypt(text: str, shift: int) -> Tuple[str, str]:
        """Return status and encrypted text."""
        encryptor = Encryptor(shift)
        return "encrypted", encryptor.cypher(text)

    @staticmethod
    def decrypt(text: str, shift: int) -> Tuple[str, str]:
        """Return status and decrypted text."""
        decryptor = Decryptor(shift)
        return "decrypted", decryptor.cypher(text)

    def execute(self, cypher_type: int, text: str, shift: int) -> str:
        """Execute user's choice and save information about it."""
        shift = self.map_rot_type(shift)

        options = {1: self.encrypt, 2: self.decrypt}

        status, text = options.get(cypher_type)(text, shift)
        data = Text(Cipher.id, text, status, f"ROT{shift})")
        # {'id': Cipher.id, 'text': text, 'status': status, 'rot_type': f'ROT{shift}'}
        MemoryBuffer.add(data)

        print(data["text"])
        return data["text"]


class Manager:
    @staticmethod
    def run():
        menu = Menu()
        menu.show_menu()
