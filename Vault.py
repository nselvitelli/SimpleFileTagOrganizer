from typing import List, Dict

from FileInfo import FileInfo
from Tag import Tag

class Vault:
    def __init__(self, name: str,
                 description: str = '',
                 files: List[FileInfo] = [],
                 tags: Dict[int, Tag] = {}) -> None:
        self.name = name
        self.description = description
        self.files = files
        self.tags = tags
        self.id = hash(name)


    def add_description(self, description: str) -> None:
        self.description = description

    def add_file(self, fileInfo) -> None:
        self.files.append(fileInfo)

    def add_tag(self, tag) -> None:
        self.tags[tag.id] = tag



    def query_files(self, tag_ids: List[int]) -> List[FileInfo]:
        print("searching for ", tag_ids)
        return []
    

    def get_tags(self) -> List[Tag]:
        return list(self.tags.values())
    
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description

    def get_id(self) -> int:
        return self.id
    
    def to_dict(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'tags': { k: v.to_dict() for k, v in self.tags.items() },
            'files': [ f.to_dict() for f in self.files ]
        }