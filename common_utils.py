import json
from pathlib import Path
from typing import Any, Dict

from requests import Response


class FileUtils:

    @staticmethod
    def read_json(file_path: Path) -> Any:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save_json(data: Any, save_path: Path):
        content = json.dumps(data, indent=4, ensure_ascii=False).encode()
        with open(save_path, "wb") as f:
            f.write(content)

    @staticmethod
    def save_png(data: Response, save_path: Path):
        with open(save_path, "wb") as f:
            f.write(data.content)

    @staticmethod
    def handle_special_char(name: str) -> str:
        name = name.rstrip(' ')
        if '?' in name:
            name = name.replace('?', '')

        if '...' in name:
            name = name.replace('...', '')

        return name


class WebUtils:

    @staticmethod
    def get_header(file_path: Path) -> Dict[str, str]:
        return FileUtils.read_json(file_path)
