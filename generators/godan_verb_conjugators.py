# coding=utf-8
import os
import json
from collections import OrderedDict
from kanji_to_romaji.kanji_to_romaji_module import kanji_to_romaji


PATH_TO_MODULE = os.path.dirname(__file__)
JP_MAPPINGS_PATH = os.path.join(PATH_TO_MODULE, os.pardir, "jp_mappings")


def set_global_godan(gr, gtr):
    global godan_romaji
    global godan_type_romaji
    godan_romaji = gr
    godan_type_romaji = gtr


def _godan_i_stem(godan):
    u_i_mapping = {
        "う": "い",
        "く": "き",
        "ぐ": "ぎ",
        "す": "し",
        "ず": "じ",
        "つ": "ち",
        "づ": "ぢ",
        "ぬ": "に",
        "ふ": "ひ",
        "ぶ": "び",
        "ぷ": "ぴ",
        "む": "み",
        "る": "り"
    }

    if godan[-1] in u_i_mapping:
        return godan[:-1] + u_i_mapping[godan[-1]]
    else:
        raise Exception("Not a valid godan ending: " + godan[-1])


def _godan_i_stem_romaji(godan_romaji_, godan_type):
    u_i_mapping_romaji = {
        "u": "i",
        "ku": "ki",
        "gu": "gi",
        "su": "shi",
        "zu": "ji",
        "tsu": "chi",

        "nu": "ni",
        "fu": "hi",
        "bu": "bi",
        "pu": "pi",
        "mu": "mi",
        "ru": "ri"
    }

    return u_i_mapping_romaji[godan_type].join(godan_romaji_.rsplit(godan_type, 1))


def get_godan_i_stem(godan):
    godan_stem_romaji = _godan_i_stem_romaji(godan_romaji, godan_type_romaji)
    godan_stem = _godan_i_stem(godan)
    return godan_stem, godan_stem_romaji


def _godan_a_stem(godan):
    u_a_mapping = {
        "う": "わ",
        "く": "か",
        "ぐ": "が",
        "す": "さ",
        "ず": "ざ",
        "つ": "た",
        "づ": "だ",
        "ぬ": "な",
        "ふ": "は",
        "ぶ": "ば",
        "ぷ": "ぱ",
        "む": "ま",
        "る": "ら"
    }

    if godan[-1] in u_a_mapping:
        return godan[:-1] + u_a_mapping[godan[-1]]
    else:
        raise Exception("Not a valid godan ending: " + godan[-1])


def _godan_a_stem_romaji(godan_romaji_, godan_type):
    u_a_mapping_romaji = {
        "u": "wa",
        "ku": "ka",
        "gu": "ga",
        "su": "sa",
        "zu": "za",
        "tsu": "ta",

        "nu": "na",
        "fu": "ha",
        "bu": "ba",
        "pu": "pa",
        "mu": "ma",
        "ru": "ra"
    }

    return u_a_mapping_romaji[godan_type].join(godan_romaji_.rsplit(godan_type, 1))


def get_godan_a_stem(godan):
    godan_stem_romaji = _godan_a_stem_romaji(godan_romaji, godan_type_romaji)
    godan_stem = _godan_a_stem(godan)
    return godan_stem, godan_stem_romaji


def _godan_o_stem(godan):
    u_o_mapping = {
        "う": "お",
        "く": "こ",
        "ぐ": "ご",
        "す": "そ",
        "ず": "ぞ",
        "つ": "と",
        "づ": "ど",
        "ぬ": "の",
        "ふ": "ほ",
        "ぶ": "ぼ",
        "ぷ": "ぽ",
        "む": "も",
        "る": "ろ"
    }

    if godan[-1] in u_o_mapping:
        return godan[:-1] + u_o_mapping[godan[-1]]
    else:
        raise Exception("Not a valid godan ending: " + godan[-1])


def _godan_o_stem_romaji(godan_romaji_, godan_type):
    u_o_mapping_romaji = {
        "u": "o",
        "ku": "ko",
        "gu": "go",
        "su": "so",
        "zu": "zo",
        "tsu": "to",

        "nu": "no",
        "fu": "ho",
        "bu": "bo",
        "pu": "po",
        "mu": "mo",
        "ru": "ro"
    }

    return u_o_mapping_romaji[godan_type].join(godan_romaji_.rsplit(godan_type, 1))


def get_godan_o_stem(godan):
    godan_stem_romaji = _godan_o_stem_romaji(godan_romaji, godan_type_romaji)
    godan_stem = _godan_o_stem(godan)
    return godan_stem, godan_stem_romaji


def _godan_e_stem(godan):
    u_e_mapping = {
        "う": "え",
        "く": "け",
        "ぐ": "げ",
        "す": "せ",
        "ず": "ぜ",
        "つ": "て",
        "づ": "で",
        "ぬ": "ね",
        "ふ": "へ",
        "ぶ": "べ",
        "ぷ": "ぺ",
        "む": "め",
        "る": "れ"
    }

    if godan[-1] in u_e_mapping:
        return godan[:-1] + u_e_mapping[godan[-1]]
    else:
        raise Exception("Not a valid godan ending: " + godan[-1])


def _godan_e_stem_romaji(godan_romaji_, godan_type):
    u_e_mapping_romaji = {
        "u": "e",
        "ku": "ke",
        "gu": "ge",
        "su": "se",
        "zu": "ze",
        "tsu": "te",

        "nu": "ne",
        "fu": "he",
        "bu": "be",
        "pu": "pe",
        "mu": "me",
        "ru": "re"
    }
    return u_e_mapping_romaji[godan_type].join(godan_romaji_.rsplit(godan_type, 1))


def get_godan_e_stem(godan):
    godan_stem_romaji = _godan_e_stem_romaji(godan_romaji, godan_type_romaji)
    godan_stem = _godan_e_stem(godan)
    return godan_stem, godan_stem_romaji


def conjugate_godan_polite_present_affirmative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ます"
    conjugated_romaji = i_stem_romaji + "masu"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_negative(godan):
    a_stem_kana, a_stem_romaji = get_godan_a_stem(godan)
    conjugated_kana = a_stem_kana + "ない"
    conjugated_romaji = a_stem_romaji + "nai"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_present_negative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ません"
    conjugated_romaji = i_stem_romaji + "masen"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_past(godan):
    godan_last_syllable_removed = godan[:-1]
    godan_last_syllable_romaji = godan_type_romaji
    godan_last_syllable_removed_romaji = "".join(godan_romaji.rsplit(godan_last_syllable_romaji, 1))

    group_mapping = {
        "く": ("いた", "ita"),
        "ぐ": ("いだ", "ida"),
        "す": ("した", "shita"),
    }

    group_mapping.update(dict.fromkeys(["う", "つ", "る"], ("った", "tta")))
    group_mapping.update(dict.fromkeys(["む", "ぶ", "ぬ"], ("んだ", "nda")))

    if godan == "行く":
        godan_type = "う"
    else:
        godan_type = godan[-1]

    conjugated_kana = godan_last_syllable_removed + group_mapping[godan_type][0]
    conjugated_romaji = godan_last_syllable_removed_romaji + group_mapping[godan_type][1]
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_past(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ました"
    conjugated_romaji = i_stem_romaji + "mashita"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_past_negative(godan):
    i_stem_kana, i_stem_romaji = get_godan_a_stem(godan)
    conjugated_kana = i_stem_kana + "なかった"
    conjugated_romaji = i_stem_romaji + "nakatta"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_past_negative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ませんでした"
    conjugated_romaji = i_stem_romaji + "masen deshita"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_te_form(godan):
    godan_last_syllable_romaji = godan_type_romaji
    godan_last_syllable_removed = godan[:-1]
    godan_last_syllable_removed_romaji = "".join(godan_romaji.rsplit(godan_last_syllable_romaji, 1))

    if godan == "行く":
        godan_type = "う"
    else:
        godan_type = godan[-1]
    group_mapping = {
        "く": ("いて", "ite"),
        "ぐ": ("いで", "ide"),
        "す": ("して", "shite"),
    }
    group_mapping.update(dict.fromkeys(["う", "つ", "る"], ("って", "tte")))
    group_mapping.update(dict.fromkeys(["む", "ぶ", "ぬ"], ("んで", "nde")))

    conjugated_kana = godan_last_syllable_removed + group_mapping[godan_type][0]
    conjugated_romaji = godan_last_syllable_removed_romaji + group_mapping[godan_type][1]
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_te_form(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "まして"
    conjugated_romaji = i_stem_romaji + "mashite"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_te_form_negative(godan):
    a_stem_kana, a_stem_romaji = get_godan_a_stem(godan)
    conjugated_kana = a_stem_kana + "ないで"
    conjugated_romaji = a_stem_romaji + "naide"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_te_form_negative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ませんで"
    conjugated_romaji = i_stem_romaji + "masende"
    return conjugated_kana, conjugated_romaji

# plain/polite conditional(negative) are past + ra


def conjugate_godan_plain_volitional(godan):
    o_stem_kana, o_stem_romaji = get_godan_o_stem(godan)
    conjugated_kana = o_stem_kana + "う"
    conjugated_romaji = o_stem_romaji + "u"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_volitional(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "ましょう"
    conjugated_romaji = i_stem_romaji + "mashou"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_plain_imperative(godan):
    e_stem_kana, e_stem_romaji = get_godan_e_stem(godan)
    conjugated_kana = e_stem_kana
    conjugated_romaji = e_stem_romaji
    return conjugated_kana, conjugated_romaji


# plain imperative negative is dictionary form + na; no need to conjugate

def conjugate_godan_polite_imperative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "なさい"
    conjugated_romaji = i_stem_romaji + "nasai"
    return conjugated_kana, conjugated_romaji


def conjugate_godan_polite_imperative_negative(godan):
    i_stem_kana, i_stem_romaji = get_godan_i_stem(godan)
    conjugated_kana = i_stem_kana + "なさるな"
    conjugated_romaji = i_stem_romaji + "nasaruna"
    return conjugated_kana, conjugated_romaji


if __name__ == "__main__":
    f = os.path.join(JP_MAPPINGS_PATH, "jm_dict_autod_kanji.json")
    with open(os.path.join(f)) as data_file:
        jm_dict = json.load(data_file)

    conjugator_funcs = [
        get_godan_a_stem,
        get_godan_i_stem,
        get_godan_e_stem,
        get_godan_o_stem,

        conjugate_godan_plain_past,
        conjugate_godan_plain_te_form
    ]

    conjugated_mappings = OrderedDict({})
    for k in list(jm_dict.keys()):
        if jm_dict[k]["w_type"] == "godan verb":
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            for c_func in conjugator_funcs:
                ck, cr = c_func(k)
                # assume first is a more common reading and second/others will have alt readings
                if ck not in conjugated_mappings:
                    if "conjugate" in c_func.__name__ or "get_godan_e_stem" == c_func.__name__:
                        conjugated_mappings[ck] = {
                            "romaji": cr,
                            "w_type": "conjugated godan verb"
                        }
                    else:
                        conjugated_mappings[ck] = {
                            "romaji": cr,
                            "w_type": "godan verb stem"
                        }

    okd_str = json.dumps(conjugated_mappings, indent=2, ensure_ascii=False, encoding="utf-8",
                         separators=(',', ': '))

    with open(os.path.join(JP_MAPPINGS_PATH, "conjugated_godan_kanji.json"), 'w') as writer:
        writer.write(str(okd_str.encode("utf-8")))
