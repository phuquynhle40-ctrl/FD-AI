# FD AI 5.0 - Module Integration Router

from src.ai_core.core import AICore
from src.api_manager.manager import APIManager
from src.security.manager import SecurityManager
from src.media_manager.manager import MediaManager
from src.coding_manager.manager import CodingManager
from src.user_manager.manager import UserManager
from src.billing.manager import BillingManager


class AI5Router:
    def __init__(self):
        self.ai_core = AICore()
        self.api_manager = APIManager()
        self.security = SecurityManager()
        self.media = MediaManager()
        self.coding = CodingManager()
        self.users = UserManager()
        self.billing = BillingManager()

    def status(self):
        return {
            "name": "FD AI",
            "version": "5.0",
            "modules": [
                "AI Core",
                "API Manager",
                "Security Manager",
                "Vision + Media",
                "Coding + Module Manager",
                "User Manager",
                "Billing Manager"
            ],
            "status": "ready"
        }

    def process_message(self, user_id, message):
        access = self.security.check_access(user_id, "chat")

        if not access.get("allowed", False):
            return {
                "status": "denied",
                "message": "Bạn không có quyền sử dụng chức năng này."
            }

        result = self.ai_core.process(message)

        return {
            "version": "5.0",
            "user_id": user_id,
            "message": message,
            "result": result,
            "status": "ready"
        }
