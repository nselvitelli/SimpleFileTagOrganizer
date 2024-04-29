from typing import List

class Tag:

    def __init__(self, name : str, childTags: List[int] = []) -> None:
        self.name = name
        self.id = hash(name)
        self.childTags = childTags

    def add_child(self, tag_id: int) -> None:
        self.childTags.append(tag_id)