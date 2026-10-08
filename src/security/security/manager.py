class SecurityManager:
    def __init__(self):
        self.name = "FD AI Security"
        self.version = "5.0"

    def check_access(self, user_id, permission):
        return {
            "user_id": user_id,
            "permission": permission,
            "allowed": True
        }
