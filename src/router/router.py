class Router:
    def __init__(self, tool_manager, module_manager, version_manager):
        self.tool_manager = tool_manager
        self.module_manager = module_manager
        self.version_manager = version_manager

    def handle(self, message):
        return {
            "message": message,
            "version": self.version_manager.current_version(),
            "tools": self.tool_manager.list_tools(),
            "modules": self.module_manager.list_modules(),
        }
