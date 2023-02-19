import random
import os

class GearRandomizer:

    def __init__(self, data_path):
        self._data_path = data_path

    def get_random_selection_by_type(self, type: str, amount: int, allow_duplicates: bool) -> list:
        
        entries = self._get_entries_by_type(type)

        if allow_duplicates:
            return random.choices(entries, k=amount)
        else:
            return random.sample(entries, k=amount)

    def get_available_types(self) -> list:
        return os.listdir(self._data_path)

    def _get_entries_by_type(self, type) -> list:
        
        with open(f"./{self._data_path}/{type}", 'r') as f:
            return f.read().splitlines()