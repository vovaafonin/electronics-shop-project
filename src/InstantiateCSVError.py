class InstantiateCSVError(Exception):
    def __init__(self, path):
        self.message = f"Файл {path} поврежден"

    def __str__(self):
        return self.message
