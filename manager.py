class VersionManager:
    def current_version(self):
        return "0.2.0"

    def upgrade_path(self):
        return ["0.2.0", "0.5.0", "1.0.0", "5.0.0"]
