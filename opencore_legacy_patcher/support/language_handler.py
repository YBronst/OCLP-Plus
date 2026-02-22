"""
language_handler.py: Library for handling translations
"""

import json
import logging
import locale
from pathlib import Path

class Translator:
    def __init__(self, language: str = "Auto") -> None:
        self.requested_language = language
        self.language = language
        self.translations = {}
        self.current_path = Path(__file__).parent.parent.resolve()
        self.translations_path = self.current_path / "translations"

        if self.language == "Auto":
            self.language = self._detect_language()

        self._load_translations()

    def _detect_language(self) -> str:
        try:
            loc = locale.getlocale()[0]
            if loc and loc.startswith("ru"):
                return "Russian"
        except:
            pass
        return "English"

    def _load_translations(self) -> None:
        lang_code = "en"
        if self.language == "Russian":
            lang_code = "ru"

        file_path = self.translations_path / f"{lang_code}.json"
        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.translations = json.load(f)
            except Exception as e:
                logging.error(f"Failed to load translations for {self.language}: {e}")
        else:
            logging.error(f"Translation file not found: {file_path}")

    def translate(self, key: str) -> str:
        return self.translations.get(key, key)
