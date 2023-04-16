import json
from typing import Dict, List
import os
from buffer import MemoryBuffer


class FileHandler:
    @staticmethod
    def write_to_file(file_name: str, data: List[Dict[str, ...]]) -> None:
        """Write data to JSON file."""
        with open(f"{file_name}.json", "a") as file:
            json.dump(data, file)

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
        max_length = 50
        file_name = input(f"Name of the file (max {max_length} characters): ")

        while len(file_name) > max_length or len(file_name.strip()) == 0:
            file_name = input(f"Invalid name. Enter new one: ")

        if os.path.exists(f"{file_name}.json"):
            FileHandler.append_to_file(
                file_name, MemoryBuffer.return_buffer_as_dict(MemoryBuffer.memory)
            )
            print(f"Data has been saved to existing file: {file_name}.json")
        else:
            FileHandler.write_to_file(
                file_name, MemoryBuffer.return_buffer_as_dict(MemoryBuffer.memory)
            )
            print(f"Data has been saved to new file: {file_name}.json")
