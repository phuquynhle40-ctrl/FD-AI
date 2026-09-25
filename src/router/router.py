import os
import json
import urllib.request


class Router:
    def __init__(self, tool_manager, module_manager, version_manager):
        self.tool_manager = tool_manager
        self.module_manager = module_manager
        self.version_manager = version_manager

    def handle(self, message):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return {
                "message": "FD AI chưa được cấu hình OPENAI_API_KEY trên Render."
            }

        data = {
            "model": "gpt-5.6-luna",
            "input": message
        }

        request = urllib.request.Request(
            "https://api.openai.com/v1/responses",
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                result = json.loads(response.read().decode("utf-8"))

            answer = result.get("output", [])

            for item in answer:
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        return {
                            "message": content.get("text", ""),
                            "version": self.version_manager.current_version(),
                            "tools": self.tool_manager.list_tools(),
                            "modules": self.module_manager.list_modules(),
                        }

            return {
                "message": "FD AI không nhận được nội dung trả lời từ AI."
            }

        except Exception as e:
            return {
                "message": f"FD AI gặp lỗi kết nối AI: {str(e)}"
            }

