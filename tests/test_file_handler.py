import json
import os

from features.file_handler import FileHandler


def test_write_to_file(tmp_path):
    file_name = os.path.join(tmp_path, "test_file")

    data = [
        {"status": "encrypted", "ROT type": "ROT13"},
        {"status": "decrypted", "ROT type": "ROT47"},
    ]
    FileHandler.write_to_file(file_name, data)

    with open(file_name + ".json", "r") as file:
        saved_data = json.load(file)

    assert saved_data == data


def test_append_to_file():
    test_data = [
        {"status": "encrypted", "ROT type": "ROT13"},
        {"status": "decrypted", "ROT type": "ROT47"},
    ]
    path = "test_file"
    with open(f"{path}.json", "w") as file:
        json.dump(test_data, file)

    FileHandler.append_to_file(path, test_data)

    with open(f"{path}.json", "r") as file:
        assert json.load(file) == test_data + test_data

    os.remove(f"{path}.json")
