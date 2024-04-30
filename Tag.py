from typing import Set, Dict

class Tag:

    def __init__(self, name : str, childTags: Set[int] = set()) -> None:
        self.name = name
        self.id = hash(name)
        self.childTags = childTags

    def add_child(self, tag_id: int) -> None:
        self.childTags.add(tag_id)

    
    def to_dict(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'id': self.id,
            'child_tags': list(self.childTags)
        }