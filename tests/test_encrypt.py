from features.encrypt import Cipher
import pytest


encryptor_13 = Cipher(shift=13, encryptor=True)
decryptor_47 = Cipher(shift=47, encryptor=False)
encryptor_1 = Cipher(shift=1, encryptor=True)


@pytest.mark.parametrize(
    "input, output", [("abc", "abc"), ("?!.", "?!."), ("123", "123")]
)
def test_shift_characters(input, output):
    assert encryptor_13.shift_characters(input) == output


@pytest.mark.parametrize(
    "input, output",
    [("Abc", "Nop"), ("Hello, world!", "Uryyb] jbeyq."), ("xyz", "klm")],
)
def test_encipher_encrypt_13(input, output):
    assert encryptor_13.encipher(input) == ("encrypted", output)


@pytest.mark.parametrize(
    "input, output", [("Abc", "Fgh"), ("Hello!", "Mjqqt,"), ("12345", "12345")]
)
def test_encipher_decrypt_47(input, output):
    assert decryptor_47.encipher(input) == ("decrypted", output)


@pytest.mark.parametrize(
    "input, output", [("Abc", "Bcd"), ("Hello!", 'Ifmmp"'), ("12345", "12345")]
)
def test_encipher_encrypt_1(input, output):
    assert encryptor_1.encipher(input) == ("encrypted", output)


def test_shift_alphabets_13():
    alphabets = encryptor_13.shift_alphabets()
    assert alphabets[:5] == "nopqr"


def test_shift_alphabets_47():
    alphabets = decryptor_47.shift_alphabets()
    assert alphabets[:5] == "vwxyz"


def test_shift_alphabets_1():
    alphabets = encryptor_1.shift_alphabets()
    assert alphabets[:5] == "bcdef"


def test_cipher_setter_should_return_value_error():
    with pytest.raises(ValueError):
        encryptor_1.shift = -1


def test_cipher_setter_should_return_type_error():
    with pytest.raises(TypeError):
        encryptor_1.shift = "a"


def test_cipher_setter_should_warn():
    with pytest.warns(Warning):
        encryptor_1.shift = 0
