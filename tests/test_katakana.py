# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import translate_to_romaji, kanji_to_romaji, translate_long_vowel, \
    translate_kana_iteration_mark, translate_dakuten_equivalent, convert_katakana_to_hiragana


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_basic_hiragana(self):
        iroha = "イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
        iroha_romaji = "Iro ha nihoheto " \
                       "Chirinuru wo " \
                       "Wa ka yo tare so " \
                       "Tsune naramu " \
                       "Uwi no okuyama " \
                       "Kefu koete " \
                       "Asaki yume mishi " \
                       "Wehi mo sesu"
        expected_result = iroha_romaji.lower()
        self.assertEqual(translate_to_romaji(iroha), expected_result)

    def test_dakuten(self):
        kana_expected_dict = {
            "ガ ギ グ ゲ ゴ": "ga gi gu ge go",
            "ザ ジ ズ ゼ ゾ": "za ji zu ze zo",
            "ダ ヂ ヅ デ ド": "da ji zu de do",
            "バ ビ ブ ベ ボ": "ba bi bu be bo",
            "パ ピ プ ペ ポ": "pa pi pu pe po"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(translate_to_romaji(k), kana_expected_dict[k])

    def test_youon(self):
        kana_expected_dict = {
            "キャ キュ キョ": "kya kyu kyo",
            "ギャ ギュ ギョ": "gya gyu gyo",
            "シャ シュ ショ": "sha shu sho",
            "ジャ ジュ ジョ": "ja ju jo",
            "ヒャ ヒュ ヒョ": "hya hyu hyo",
            "ビャ ビュ ビョ": "bya byu byo",
            "ピャ ピュ ピョ": "pya pyu pyo",
            "チャ チュ チョ": "cha chu cho",
            "ニャ ニュ ニョ": "nya nyu nyo",
            "ミャ ミュ ミョ": "mya myu myo",
            "リャ リュ リョ": "rya ryu ryo"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(translate_to_romaji(k)), kana_expected_dict[k])

    def test_soukon(self):
        kana_expected_dict = {
            "チョット": "chotto",
            "マッテ": "matte",
            "ハッピョウケッカ": "happyoukekka",
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_long_vowel(self):
        kana_expected_dict = {
            "メール": "meeru",
            "ケーキ": "keeki",
            "コーヒー": "koohii"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(translate_long_vowel(translate_to_romaji(k)), kana_expected_dict[k])

    def test_long_vowel_with_soukon(self):
        kana_expected_dict = {
            "リュー": "ryuu",
            "ニュース": "nyuusu",
            "デビュー": "debyuu",
            "チュー": "chuu"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_u_and_small_vowel(self):
        kana_expected_dict = {
            "ハロウィーン": "harowiin",
            "ソファ": "sofa",
            "ウィンドウズ": "windouzu",
            "チェック": "chekku",
            "ディスニ": "disuni",
            "ドゥラハン": "durahan",
            "パーティー": "paatii",
            "タトゥー": "tatuu",
            "クァルテット": "kwarutetto"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

        kana_expected_dict_s = {
            "ウィ": "wi",
            "ウェ": "we",
            "ウォ": "wo",

            "ヴァ": "va",
            "ヴィ": "vi",
            "ヴェ": "ve",
            "ヴォ": "vo",

            "ファ": "fa",
            "フィ": "fi",
            "フェ": "fe",
            "フォ": "fo",

            "ティ": "ti",
            "ディ": "di",
            "トゥ": "tu",
            "ドゥ": "du",

            "クァ": "kwa",
            "クィ": "kwi",
            "クェ": "kwe",
            "クォ": "kwo",
            "キェ": "kye",

            "グァ": "gwa",
            "グィ": "gwi",
            "グェ": "gwe",
            "グォ": "gwo",
            "ギェ": "gye",

            "スィ": "si",
            "ズィ": "zi",
            "シェ": "she",
            "ジェ": "je",
            "チェ": "che",

            "ツァ": "tsa",
            "ツィ": "tsi",
            "ツェ": "tse",
            "ツォ": "tso",

            "ホゥ": "hu",
            "イィ": "yi",
            "イェ": "ye"
        }

        for k in list(kana_expected_dict_s.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict_s[k])

    def test_soukon_ch(self):
        kana_expected_dict = {
            "ボッチャン": "botchan",
            "コッチ": "kotchi",
            "カッチョン": "katchon",
            "マッチャ": "matcha",
            "ミッチ": "mitchi"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_convert_hiragana_to_katakana(self):
        iroha_h = "いろ は にほへと ちりぬる を わ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
        iroha_k = "イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
        self.assertEqual(convert_katakana_to_hiragana(iroha_k), iroha_h)
        self.assertEqual(type(convert_katakana_to_hiragana(iroha_k)), str)

        dakuten_hiragana = "が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ"
        dakuten_katakana = "ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ"
        self.assertEqual(convert_katakana_to_hiragana(dakuten_katakana), dakuten_hiragana)

        youon_hiragana = "きゃ きゅ きょ ぎゃ ぎゅ ぎょ しゃ しゅ しょ じゃ じゅ じょ ひゃ ひゅ ひょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ " \
                         "ちゃ ちゅ ちょ にゃ にゅ にょ みゃ みゅ みょ りゃ りゅ りょ"
        youon_katakana = "キャ キュ キョ ギャ ギュ ギョ シャ シュ ショ ジャ ジュ ジョ ヒャ ヒュ ヒョ ビャ ビュ ビョ ピャ ピュ ピョ " \
                         "チャ チュ チョ ニャ ニュ ニョ ミャ ミュ ミョ リャ リュ リョ"
        self.assertEqual(convert_katakana_to_hiragana(youon_katakana), youon_hiragana)

        self.assertEqual(convert_katakana_to_hiragana("コヽーミッチヾ"), "こゝーみっちゞ")
        self.assertEqual(convert_katakana_to_hiragana("カヾールッチ"), "かゞーるっち")

    def test_translate_iteration_mark(self):
        self.assertEqual(translate_kana_iteration_mark("カヽキヽクヽケヽコヽ"), "カカキキククケケココ")
        self.assertEqual(translate_kana_iteration_mark("カヾキヾクヾケヾコヾ"), "カガキギクグケゲコゴ")

        self.assertEqual(kanji_to_romaji("カヾールッチ"), "kagaarutchi")
        self.assertEqual(kanji_to_romaji("コヽーミッチヾ"), "kokoomitchiji")

    def test_translate_dakuten_equivalent(self):
        for test_c, expected in zip(list("カキクケコサシスセソタチツテトハヒフヘホ"),
                                    list("ガギグゲゴザジズゼゾダヂヅデドバビブベボ")):
            self.assertEqual(translate_dakuten_equivalent(test_c), expected)
        self.assertEqual(translate_dakuten_equivalent("ガ"), "")

if __name__ == "__main__":
    unittest.main()
