class Router:
    def __init__(self, tool_manager, module_manager, version_manager):
        self.tools = tool_manager
        self.modules = module_manager
        self.versions = version_manager

    def handle(self, message: str) -> dict:
        text = message.lower()

        if any(word in text for word in ("phiên bản", "version", "bản nào")):
            return {
                "type": "version",
                "reply": f"Bạn đang dùng FD AI {self.versions.current_version()}. "
                          f"Lộ trình: {' → '.join(self.versions.upgrade_path())}."
            }

        if any(word in text for word in ("công cụ", "tool", "tools")):
            names = ", ".join(self.tools.list_tools())
            return {
                "type": "tools",
                "reply": f"Tool Manager hiện có: {names}."
            }

        if any(word in text for word in ("module", "mô-đun", "mô đun")):
            names = ", ".join(self.modules.list_modules())
            return {
                "type": "modules",
                "reply": f"Module Manager hiện có: {names}."
            }

        return {
            "type": "chat",
            "reply": (
                "FD AI 0.2 đã nhận yêu cầu của bạn. "
                "Router đã phân tích yêu cầu và chuyển đến lớp xử lý cơ bản. "
                "Bạn có thể mở rộng Tool Manager và Module Manager để thêm khả năng mới."
            )
        }
