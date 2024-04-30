from typing import List, Tuple, Callable
from FileOrganizer import Global
from VaultsManager import VaultsManager

class CommandLineController:

    def __init__(self) -> None:
        self.manager = VaultsManager(Global.VAULT_MAIN_FILE)
        self.__loop()
    

    def __loop(self, commands: List[Tuple[str, Callable[[], bool]]] = []) -> None:
        quit = False

        while not quit:
            if len(commands) == 0:
                return
            
            pass

    def __select_command(self, commands: List[Tuple[str, Callable[[], bool]]] = []) -> bool:
        for name, func in commands:
            """
            TODO: select command, run function, return func output
            """