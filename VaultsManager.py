import os, json
from typing import List, Dict, Tuple

from Vault import Vault
from FileOrganizer import Global
import VaultSerialization

class VaultsManager:

    def __init__(self, filepath: str) -> None:
        self.vaults = {}
        self.__load_vaults_file(filepath)
        self.filepath = filepath


    def get_all_vault_info(self) -> List[Tuple[int, Dict[str, str]]]:
        return list(self.vaults.items())


    def load_vault(self, vaultId: int) -> Vault:
        if vaultId in self.vaults:
            vaultInfo = self.vaults[vaultId]
            vaultPath = vaultInfo['filepath']
            return VaultSerialization.load_vault(vaultPath)
        raise Exception("Vault with id {} does not exist.".format(vaultId))



    def add_vault(self, vault: Vault, filepath: str|None, autosave: bool=True):
        id = vault.get_id()
        name = vault.get_name()
        path = '{}/{}.json'.format(Global.VAULT_DIRECTORY, name) if not filepath else filepath
        self.vaults[id] = {
            'name': name,
            'filepath': path
        }
        if autosave:
            VaultSerialization.save_vault(vault, path)
            self.save_vaults_file()


    def save_vaults_file(self):
        with open(self.filepath, 'w') as file:
            file.write(json.dumps(self.vaults))


    def __ensure_file_exists(self, filepath: str) -> None:
        if not (os.path.isfile(filepath) and os.path.getsize(filepath) > 0):
            print("Unable to load vaults manager file, creating file at [{}]".format(filepath))
            with open(filepath, 'a') as file:
                file.write('{}\n')

    def __load_vaults_file(self, filepath: str):
        self.__ensure_file_exists(filepath)

        with open(filepath) as file:
            self.vaults = json.load(file)


    