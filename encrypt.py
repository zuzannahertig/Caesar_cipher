from abc import ABC, abstractmethod
import string
from typing import List
import warnings
from exceptions import TextNotEncrypted


class Cipher(ABC):
    CHARACTERS: List[str] = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.punctuation,
    ]
    characters_joined: str = "".join(CHARACTERS)
    id = 0

    def __init__(self, shift: int) -> None:
        self._shift = shift
        Cipher.id += 1

    @property
    def shift(self) -> int:
        return self._shift

    @shift.setter
    def shift(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Wrong value type! Expected integer.")
        elif value == 0:
            warnings.warn(
                "Shift of value 0 will result in returning text in an unchanged form.",
                TextNotEncrypted,
            )
        elif value < 0:
            raise ValueError("Value should be greater than 0.")
        self._shift = value

    def shift_characters(self, characters: str) -> str:
        """Return list of characters shifted by chosen value."""
        self.shift %= 26
        return characters[self.shift :] + characters[: self.shift]

    def shift_alphabets(self) -> str:
        """Return string of shifted characters."""
        shifted = [self.shift_characters(character) for character in self.CHARACTERS]
        return "".join(shifted)

    @abstractmethod
    def cypher(self, text: str) -> str:
        """Encrypt or decrypt text."""
        raise NotImplementedError


class Encryptor(Cipher):
    def __init__(self, shift: int) -> None:
        super().__init__(shift)

    def cypher(self, text: str) -> str:
        """Encrypt text."""
        final_shifted_alphabet = self.shift_alphabets()
        table = str.maketrans(self.characters_joined, final_shifted_alphabet)
        return text.translate(table)


class Decryptor(Cipher):
    def __init__(self, shift: int) -> None:
        super().__init__(shift)

    def cypher(self, text: str) -> str:
        """Decrypt text."""
        final_shifted_alphabet = self.shift_alphabets()
        table = str.maketrans(final_shifted_alphabet, self.characters_joined)
        return text.translate(table)


def main():
    encryptor = Encryptor(3)
    encrypted = encryptor.cypher("Hello, hello!")
    print(encrypted)
    decryptor = Decryptor(3)
    decrypted = decryptor.cypher(encrypted)
    print(decrypted)


if __name__ == "__main__":
    main()
