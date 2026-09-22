from flask import Flask, jsonify, render_template, request
from src.router.router import Router
from src.tool_manager.manager import ToolManager
from src.module_manager.manager import ModuleManager
from src.version_manager.manager import VersionManager

def create_app():
    app = Flask(__name__, template_folder="../../templates", static_folder="../../static")

    tool_manager = ToolManager()
    module_manager = ModuleManager()
    version_manager = VersionManager()
    router = Router(tool_manager, module_manager, version_manager)

    @app.get("/")
    def home():
        return render_template(
            "index.html",
            version=version_manager.current_version(),
            tools=tool_manager.list_tools(),
            modules=module_manager.list_modules(),
        )

    @app.post("/api/chat")
    def chat():
        data = request.get_json(silent=True) or {}
        message = str(data.get("message", "")).strip()
        if not message:
            return jsonify({"ok": False, "error": "Vui lòng nhập nội dung."}), 400
        result = router.handle(message)
        return jsonify({"ok": True, **result})

    @app.get("/api/status")
    def status():
        return jsonify({
            "name": "FD AI",
            "version": version_manager.current_version(),
            "upgrade_path": version_manager.upgrade_path(),
            "tools": tool_manager.list_tools(),
            "modules": module_manager.list_modules(),
        })

    return app
