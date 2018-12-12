# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import translate_to_romaji, kanji_to_romaji


class TestHiraganaRomajiTranslation(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_brackets(self):
        self.assertEqual("[]", translate_to_romaji("「」"))
        self.assertEqual("[]", translate_to_romaji("『』"))
        self.assertEqual("()", translate_to_romaji("（）"))
        self.assertEqual("[]", translate_to_romaji("〔〕"))
        self.assertEqual("[]", translate_to_romaji("［］"))
        self.assertEqual("{}", translate_to_romaji("｛｝"))
        self.assertEqual("()", translate_to_romaji("〈〉"))
        self.assertEqual("[]", translate_to_romaji("【】"))
        self.assertEqual("[]", translate_to_romaji("〖〗"))
        self.assertEqual("[]", translate_to_romaji("〘〙"))
        self.assertEqual("[]", translate_to_romaji("〚〛"))

    def test_punctuation_and_specials(self):
        self.assertEqual("--", translate_to_romaji("゠"))
        self.assertEqual("-", translate_to_romaji("〓"))
        self.assertEqual("=", translate_to_romaji("＝"))

        self.assertEqual("~", translate_to_romaji("〜"))
        self.assertEqual("_", translate_to_romaji("…"))
        self.assertEqual("", translate_to_romaji("※"))

        self.assertEqual("", translate_to_romaji("♪"))
        self.assertEqual("", translate_to_romaji("♫"))
        self.assertEqual("", translate_to_romaji("♬"))
        self.assertEqual("", translate_to_romaji("♩"))

        self.assertEqual("!", translate_to_romaji("！"))
        self.assertEqual("?", translate_to_romaji("？"))

    def test_typographic_replacement_len_is_0(self):
        self.assertEqual(kanji_to_romaji("ケΨカ"), "keka")
        self.assertEqual(kanji_to_romaji("Ψケカ"), "keka")
        self.assertEqual(kanji_to_romaji("ケカΨ"), "keka")

    def test_keep_new_line_after_translation(self):
        test_text = r"""
        アパート
        くる
        のけ
        """

        expected = "apaato\n" \
                   "kuru\n" \
                   "noke"

        self.assertEqual(kanji_to_romaji(test_text).encode().decode("unicode_escape"),
                         expected)

    def test_typo_not_overwritten(self):
        self.assertEqual(kanji_to_romaji("～未来への絆～"), "~ mirai e no kizuna~")


if __name__ == "__main__":
    unittest.main()
