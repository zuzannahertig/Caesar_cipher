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

    def return_buffer_as_dict(self) -> List[Dict[str, str]]:
        """Return memory as list of dicts."""
        return [asdict(entry) for entry in self.memory]
