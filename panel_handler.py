from pathlib import Path
from typing import Dict, List, Any

import requests
from loguru import logger

import consts
from common_utils import WebUtils, FileUtils


class PanelHandler:
    _header_path: Path
    _panel_file_path: Path
    _id_map: Dict[int, Dict[str, Any]] = None

    def __init__(self, header_path: Path, panel_file_path: Path):
        self._header_path = header_path
        self._panel_file_path = panel_file_path

    def gen_panel_file(self):
        headers = WebUtils.get_header(self._header_path)
        response = requests.get(consts.PANEL_URL, headers=headers)
        FileUtils.save_json(response.json(), self._panel_file_path)

    def _load_packages(self) -> List[Dict[str, Any]]:
        return FileUtils.read_json(self._panel_file_path)["data"]["all_packages"]

    def _gen_id_map(self):
        packages = self._load_packages()
        id_map: Dict[int, Dict[str, Any]] = {}
        for p in packages:
            id_map[p["id"]] = p

        self._id_map = id_map

    def download_emote(self, save_path: Path, ids: List[int]):
        if not save_path.exists():
            save_path.mkdir(parents=True)

        if self._id_map is None:
            self._gen_id_map()

        for index in ids:
            if index not in self._id_map.keys():
                logger.error("不存在的index = {}", index)
                continue

            self._save_one_emote(index, save_path, False)

    def _save_one_emote(self, index: int, save_path: Path, skip_exist: bool = False):
        if index == 4:
            logger.info("不支持颜文字下载")
            return

        emote_json: Dict[str, Any] = self._id_map[index]
        emote_package_name: str = emote_json["text"]
        base_path: Path = save_path.joinpath(rf"{index}_{emote_package_name}")
        if not base_path.exists():
            base_path.mkdir(parents=True)
        elif skip_exist:
            return

        logger.info("开始下载{}-{}", index, emote_package_name)

        for item in emote_json["emote"]:
            emote_name: str = item["text"].strip('[').rstrip(']')
            emote_name = FileUtils.handle_special_char(emote_name)
            emote = requests.get(item["url"])
            png_save_path: Path = base_path.joinpath(rf"{emote_name}.png")
            FileUtils.save_png(emote, png_save_path)

        logger.info("完成下载{}-{}", index, emote_package_name)

    def download_all_emote(self, save_path: Path):

        if not save_path.exists():
            save_path.mkdir(parents=True)

        if self._id_map is None:
            self._gen_id_map()

        for index in self._id_map.keys():
            self._save_one_emote(index, save_path, True)
