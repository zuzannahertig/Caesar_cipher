import json
from typing import Dict


class FileHandler:
    @staticmethod
    def append_to_file(file_name: str, data: Dict) -> None:
        with open(f"{file_name}.json", "a+") as f:
            json.dump(data, f)

    @staticmethod
    def write_to_file(file_name: str, data: Dict) -> None:
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f)
