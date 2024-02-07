import os
from lupa import LuaRuntime

class LuaProcessor:
    def __init__(self) -> None:
        self.modules = './lua/modules'
        self.lua = LuaRuntime(unpack_returned_tuples=True)

        self.__loadModules();
        
        pass

    def __loadModules(self):
        for file in os.listdir(self.modules):
            module_route = os.path.join(self.modules, file)
            absolute_route = os.path.abspath(module_route)
            absolute_route = absolute_route.replace('\\', '/')
            self.lua.execute(f'package.path = package.path .. ";{absolute_route}"')
    
    def __loadLuaTable(self, code):
        

    def luaTableToJson(self, filePath: str):
        with open(filePath, 'r') as file:
            lua_func = self.lua.eval(file.read())
            lua_func({})
