from io import StringIO
import sys
from features.menu import Menu
import pytest
from pytest import MonkeyPatch


@pytest.fixture()
def redirect_stdout():
    sys.stdout = StringIO()
    yield
    sys.stdout = sys.__stdout__


def test_show_start(redirect_stdout, capsys):
    Menu.show_start()
    assert (
        capsys.readouterr().out.strip()
        == "This program lets you encrypt any text using Caesar cipher.\nThe "
        "default settings are: "
        "encryption and ROT13 algorithm, but you can change them at any time.\n".strip()
    )


def test_show_options(redirect_stdout, capsys):
    Menu.show_options()
    assert (
        capsys.readouterr().out.strip()
        == "Choose:\n1 – to enter the text\n2 – to change the default settings\n3 "
        "– to save the data and quit\n4 – to quit without saving.\n".strip()
    )


def test_show_settings_cipher_type(redirect_stdout, capsys):
    Menu.show_settings_cipher_type()
    assert (
        capsys.readouterr().out.strip() == "Choose:\n"
        "1 – to encrypt\n"
        "2 – to decrypt\n".strip()
    )


def test_show_settings_rot(redirect_stdout, capsys):
    Menu.show_settings_rot()
    assert (
        capsys.readouterr().out.strip()
        == "Choose:\n1 – to choose ROT13 algorithm\n2 – to choose ROT47 "
        "algorithm\n3 – to set algorithm's shift\n".strip()
    )


def test_invalid_answer(redirect_stdout, capsys):
    text = "test"
    Menu.invalid_answer(text)
    assert (
        capsys.readouterr().out.strip()
        == f"Invalid option chosen for {text}. Please choose one of the available "
        f"options.".strip()
    )


def test_enter_text(monkeypatch: MonkeyPatch):
    text = "Hello!"
    monkeypatch.setattr("builtins.input", lambda _: text)
    assert Menu.enter_text() == text


def test_enter_text_warning(monkeypatch: MonkeyPatch):
    with pytest.warns(Warning):
        text = ""
        monkeypatch.setattr("builtins.input", lambda _: text)
        assert Menu.enter_text() == text


def test_choose(monkeypatch: MonkeyPatch):
    text = "test"
    monkeypatch.setattr("builtins.input", lambda: text)
    assert Menu.choose() == text
