import json
from typing import Dict, List
import os
from buffer import MemoryBuffer


class FileHandler:

    @staticmethod
    def write_to_file(file_name: str, data: List[Dict[str, ...]]) -> None:
        """Write data to JSON file."""
        with open(f"{file_name}.json", "a") as f:
            json.dump(data, f)

    @staticmethod
    def append_to_file(file_path: str, data: List[Dict[str, ...]]) -> None:
        """Append information about the session to existing file."""
        with open(f"{file_path}.json", "r+") as file:
            existing_data = json.load(file)
            existing_data.extend(data)
            file.seek(0)
            json.dump(existing_data, file)
            file.truncate()

    @staticmethod
    def save_data() -> None:
        """Save information from current session in JSON file."""
        file_name = input("Name of the file: ")
        if os.path.exists(f"{file_name}.json"):
            FileHandler.append_to_file(file_name, MemoryBuffer.return_buffer_as_dict(MemoryBuffer.memory))
        else:
            FileHandler.write_to_file(file_name, MemoryBuffer.return_buffer_as_dict(MemoryBuffer.memory))


