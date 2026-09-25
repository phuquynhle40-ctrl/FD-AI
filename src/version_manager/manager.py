class VersionManager:
    def __init__(self):
        self.version = "0.2.0"

    def current_version(self):
        return self.version

    def upgrade_path(self):
        return ["0.2.0"]
