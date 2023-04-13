from typing import List
from dataclasses import dataclass


@dataclass
class Text:
    id: int
    text: str
    status: str
    rot_type: str


class MemoryBuffer:
    history: List[Text] = []

    @staticmethod
    def add(data: Text):
        MemoryBuffer.history.append(data)

    # def return_buffer_as_dict(self):
    # return []
