from typing import Set


class FileInfo:

    def __init__(self, filepath: str, 
                 name: str|None = None, 
                 description: str = '',
                 tags: Set[int] = set()) -> None:
        self.filepath = filepath
        self.name = name if name else filepath
        self.description = description
        self.tags = tags

    def add_description(self, description:str) -> None:
        self.description = description

    def add_name(self, name: str) -> None:
        self.name = name

    def add_tag(self, tag_id: int) -> None:
        self.tags.add(tag_id)

    def get_tags(self) -> Set[int]:
        return self.tags