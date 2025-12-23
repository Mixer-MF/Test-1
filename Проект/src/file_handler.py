import json
import os

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        # Создаем папку data, если её нет
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    def load(self):
        """Загрузка данных из JSON файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save(self, data):
        """Сохранение данных в JSON файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False