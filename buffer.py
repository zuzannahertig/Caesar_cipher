from typing import List, Dict
from dataclasses import dataclass, asdict


@dataclass
class Text:
    text: str
    status: str
    rot_type: str


class MemoryBuffer:
    memory: List[Text] = []

    @staticmethod
    def add(data: Text) -> None:
        """Add information about session to the buffer."""
        MemoryBuffer.memory.append(data)

    @staticmethod
    def return_buffer_as_dict(memory) -> List[Dict[str, ...]]:
        """Return memory as list of dicts."""
        return [asdict(entry) for entry in memory]
