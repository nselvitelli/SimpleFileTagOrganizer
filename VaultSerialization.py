import os, json

from Vault import Vault
from FileOrganizer import Global
from Tag import Tag
from FileInfo import FileInfo

def load_vault(filepath: str) -> Vault:
    if not (os.path.isfile(filepath) and os.path.getsize(filepath) > 0):
        raise Exception("Invalid vault filepath {}".format(filepath))
    
    vaultJson = {}
    with open(filepath) as file:
        vaultJson = json.load(file)
    try:
        name = vaultJson['name']
        description = vaultJson['description']
        tags = { k: Tag(v['name'], set(v['child_tags'])) for k, v in vaultJson['tags']}
        files = [ FileInfo(file['filepath'], file['name'], file['description'], set(file['tags'])) for file in vaultJson['files'] ]
        return Vault(name, description, files, tags)
    except:
        raise Exception('Invalid vault format. Attempted loading from file: {}'.format(filepath))



def save_vault(vault: Vault, filepath:str|None = None):
    if not filepath:
        filepath = '{}/{}.json'.format(Global.VAULT_DIRECTORY, vault.get_name())
    
    vault_dict = vault.to_dict()

    with open(filepath, 'w') as file:
        file.write(json.dumps(vault_dict))

    print('Saved vault [{}] to {}'.format(vault.get_name(), filepath))