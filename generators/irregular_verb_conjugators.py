# coding=utf-8
import os
import json
from collections import OrderedDict

PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")


if __name__ == "__main__":
    f = os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json")
    with open(os.path.join(f)) as data_file:
        jm_dict = json.load(data_file)

    svt = {
        "します": "shimasu",
        "しない": "shinai",
        "しません": "shimasen",
        "した": "shita",
        "しました": "shimashita",
        "しなかった": "shinakatta",
        "しませんでした": "shimasen deshita",
        "して": "shite",
        "しまして": "shimashite",
        "しないで": "shinaide",
        "しませんで": "shimasende",
        "しよう": "shiyou",
        "しましょう": "shimashou",
        "しい": "shii",
        "しろ": "shiro",
        "しなさい": "shinasai",
        "しなさるな": "shinasaruna",
    }

    suru_conjugated_mappings = OrderedDict({})
    for k in list(jm_dict.keys()):
        if jm_dict[k]["w_type"] == "suru verb":
            for vk in list(svt.keys()):
                suru_conjugated_mappings[k[:-2] + vk] = {
                    "romaji": jm_dict[k]["romaji"][:-4].strip() + " " + svt[vk].strip(),
                    "w_type": "conjugated suru verb"
                }

    kvt = {
        "来ます": "kimasu",
        "来ない": "konai",
        "来ません": "kimasen",
        "来た": "kita",
        "来ました": "kimashita",
        "来なかった": "konakatta",
        "来ませんでした": "kimasen deshita",
        "来て": "kite",
        "来まして": "kimashite",
        "来ないで": "konaide",
        "来ませんで": "kimasende",
        "来よう": "koyou",
        "来ましょう": "kimashou",
        "来い": "koi",
        "来なさい": "kinasai",
        "来なさるな": "kinasaruna",

        "來ます": "kimasu",
        "來ない": "konai",
        "來ません": "kimasen",
        "來た": "kita",
        "來ました": "kimashita",
        "來なかった": "konakatta",
        "來ませんでした": "kimasen deshita",
        "來て": "kite",
        "來まして": "kimashite",
        "來ないで": "konaide",
        "來ませんで": "kimasende",
        "來よう": "koyou",
        "來ましょう": "kimashou",
        "來い": "koi",
        "來なさい": "kinasai",
        "來なさるな": "kinasaruna"
    }

    kuru_conjugated_mappings = OrderedDict({})
    for k in list(jm_dict.keys()):
        if jm_dict[k]["w_type"] == "kuru verb":
            for vk in list(kvt.keys()):
                kuru_conjugated_mappings[k[:-2] + vk] = {
                    "romaji": jm_dict[k]["romaji"][:-4].strip() + " " + kvt[vk].strip(),
                    "w_type": "conjugated kuru verb"
                }

    okd_str = json.dumps(suru_conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_irr_suru_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))

    okd_str = json.dumps(kuru_conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))
    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_irr_kuru_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
