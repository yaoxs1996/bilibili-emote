import argparse
from pathlib import Path
from typing import List

import consts
from panel_handler import PanelHandler


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=str, default="1")
    parser.add_argument("--path", type=str, default="./emote")
    parser.add_argument("--all", type=bool, default=False)
    parser.add_argument("--refresh", type=str, default=False)

    return parser.parse_args()


def convert_str_to_list(original: str) -> List[int]:
    result: List[int] = []
    str_list: List[str] = original.replace(' ', '').split(',')
    for s in str_list:
        result.append(int(s))

    return result


if __name__ == "__main__":
    args = get_args()
    header_path: Path = consts.RESOURCE_PATH.joinpath(consts.HEADER_FILE_NAME)
    panel_path: Path = consts.RESOURCE_PATH.joinpath(consts.PANEL_FILE_NAME)

    handler = PanelHandler(header_path=header_path, panel_file_path=panel_path)
    if args.refresh:
        handler.gen_panel_file()

    save_path: Path = Path(args.path)

    if args.all:
        handler.download_all_emote(save_path)
    else:
        ids_str: str = args.index
        ids: List[int] = convert_str_to_list(ids_str)
        handler.download_emote(save_path, ids)
