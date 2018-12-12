# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import translate_to_romaji, kanji_to_romaji, convert_hiragana_to_katakana, \
    translate_kana_iteration_mark, translate_dakuten_equivalent


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_basic_hiragana(self):
        iroha = "いろ は にほへと ちりぬるをわ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
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
        self.assertEqual(type(kanji_to_romaji(iroha)), str)

    def test_dakuten(self):
        kana_expected_dict = {
            "が ぎ ぐ げ ご": "ga gi gu ge go",
            "ざ じ ず ぜ ぞ": "za ji zu ze zo",
            "だ ぢ づ で ど": "da ji zu de do",
            "ば び ぶ べ ぼ": "ba bi bu be bo",
            "ぱ ぴ ぷ ぺ ぽ": "pa pi pu pe po"
        }

        for k in list(kana_expected_dict.keys()):
            self.assertEqual(translate_to_romaji(k), kana_expected_dict[k])

    def test_youon(self):
        kana_expected_dict = {
            "きゃ きゅ きょ": "kya kyu kyo",
            "ぎゃ ぎゅ ぎょ": "gya gyu gyo",
            "しゃ しゅ しょ": "sha shu sho",
            "じゃ じゅ じょ": "ja ju jo",
            "ひゃ ひゅ ひょ": "hya hyu hyo",
            "びゃ びゅ びょ": "bya byu byo",
            "ぴゃ ぴゅ ぴょ": "pya pyu pyo",
            "ちゃ ちゅ ちょ": "cha chu cho",
            "にゃ にゅ にょ": "nya nyu nyo",
            "みゃ みゅ みょ": "mya myu myo",
            "りゃ りゅ りょ": "rya ryu ryo"
        }

        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_soukon(self):
        kana_expected_dict = {
            "ちょっと": "chotto",
            "まって": "matte",
            "はっぴょうけっか": "happyoukekka",
        }

        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_soukon_ch(self):
        kana_expected_dict = {
            "ぼっちゃん": "botchan",
            "こっち": "kotchi",
            "かっちょん": "katchon",
            "まっちゃ": "matcha",
            "みっち": "mitchi"
        }
        for k in list(kana_expected_dict.keys()):
            self.assertEqual(kanji_to_romaji(k), kana_expected_dict[k])

    def test_convert_hiragana_to_katakana(self):
        iroha_h = "いろ は にほへと ちりぬる を わ か よ たれ そ つね ならむ うゐ の おくやま けふ こえて あさき ゆめ みし ゑひ も せす"
        iroha_k = "イロ ハ ニホヘト チリヌル ヲ ワ カ ヨ タレ ソ ツネ ナラム ウヰ ノ オクヤマ ケフ コエテ アサキ ユメ ミシ ヱヒ モ セス"
        self.assertEqual(convert_hiragana_to_katakana(iroha_h), iroha_k)
        self.assertEqual(type(convert_hiragana_to_katakana(iroha_h)), str)

        dakuten_hiragana = "が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ"
        dakuten_katakana = "ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ"
        self.assertEqual(convert_hiragana_to_katakana(dakuten_hiragana), dakuten_katakana)

        youon_hiragana = "きゃ きゅ きょ ぎゃ ぎゅ ぎょ しゃ しゅ しょ じゃ じゅ じょ ひゃ ひゅ ひょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ " \
                         "ちゃ ちゅ ちょ にゃ にゅ にょ みゃ みゅ みょ りゃ りゅ りょ"
        youon_katakana = "キャ キュ キョ ギャ ギュ ギョ シャ シュ ショ ジャ ジュ ジョ ヒャ ヒュ ヒョ ビャ ビュ ビョ ピャ ピュ ピョ " \
                         "チャ チュ チョ ニャ ニュ ニョ ミャ ミュ ミョ リャ リュ リョ"
        self.assertEqual(convert_hiragana_to_katakana(youon_hiragana), youon_katakana)

        self.assertEqual(convert_hiragana_to_katakana("こゝーみっちゞ"), "コヽーミッチヾ")
        self.assertEqual(convert_hiragana_to_katakana("かゞーるっち"), "カヾールッチ")

    def test_translate_iteration_mark(self):
        self.assertEqual(translate_kana_iteration_mark("かゝきゝくゝけゝこゝ"), "かかききくくけけここ")
        self.assertEqual(translate_kana_iteration_mark("かゞきゞくゞけゞこゞ"), "かがきぎくぐけげこご")

        self.assertEqual(kanji_to_romaji("かゞーるっち"), "kagaarutchi")
        self.assertEqual(kanji_to_romaji("こゝーみっちゞ"), "kokoomitchiji")

    def test_translate_dakuten_equivalent(self):
        for test_c, expected_result in zip(list("かきくけこさしすせそたちつてとはひふへほ"),
                                           list("がぎぐげござじずぜぞだぢづでどばびぶべぼ")):
            self.assertEqual(translate_dakuten_equivalent(test_c), expected_result)
        self.assertEqual(translate_dakuten_equivalent("が"), "")


if __name__ == "__main__":
    unittest.main()
