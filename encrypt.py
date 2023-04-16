import string
from typing import List, Tuple
import warnings
from custom_warnings import TextNotEncrypted


class Cipher:
    CHARACTERS: List[str] = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.punctuation,
    ]
    characters_joined: str = "".join(CHARACTERS)

    def __init__(self, shift: int, encryptor: bool) -> None:
        self._shift = shift
        self.encryptor = encryptor

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

    def encipher(self, text: str) -> Tuple[str, str]:
        """Encrypt or decrypt text."""
        final_shifted_alphabet = self.shift_alphabets()
        if self.encryptor:
            table = str.maketrans(self.characters_joined, final_shifted_alphabet)
            status = "encrypted"
        else:
            table = str.maketrans(final_shifted_alphabet, self.characters_joined)
            status = "decrypted"
        return status, text.translate(table)
