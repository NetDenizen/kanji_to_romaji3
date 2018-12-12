# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import kanji_to_romaji
from generators.godan_verb_conjugators import conjugate_godan_plain_te_form, conjugate_godan_plain_te_form_negative, \
    conjugate_godan_plain_volitional, conjugate_godan_polite_volitional, conjugate_godan_plain_imperative, \
    conjugate_godan_polite_imperative, conjugate_godan_polite_present_affirmative, conjugate_godan_plain_negative, \
    conjugate_godan_polite_present_negative, conjugate_godan_polite_past, conjugate_godan_plain_past, \
    conjugate_godan_polite_past_negative, conjugate_godan_plain_past_negative, \
    conjugate_godan_polite_imperative_negative, conjugate_godan_polite_te_form, \
    conjugate_godan_polite_te_form_negative, set_global_godan


class TestGodanVerbConjugators(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_polite_present_affirmative(self):
        godan_expected = {
            "会う": ("会います", "aimasu"),
            "待つ": ("待ちます", "machimasu"),
            "撮る": ("撮ります", "torimasu"),
            "読む": ("読みます", "yomimasu"),
            "遊ぶ": ("遊びます", "asobimasu"),
            "死ぬ": ("死にます", "shinimasu"),
            "書く": ("書きます", "kakimasu"),
            "行く": ("行きます", "ikimasu"),
            "泳ぐ": ("泳ぎます", "oyogimasu"),
            "話す": ("話します", "hanashimasu")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_present_affirmative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_negative(self):
        godan_expected = {
            "会う": ("会わない", "awanai"),
            "待つ": ("待たない", "matanai"),
            "撮る": ("撮らない", "toranai"),
            "読む": ("読まない", "yomanai"),
            "遊ぶ": ("遊ばない", "asobanai"),
            "死ぬ": ("死なない", "shinanai"),
            "書く": ("書かない", "kakanai"),
            "行く": ("行かない", "ikanai"),
            "泳ぐ": ("泳がない", "oyoganai"),
            "話す": ("話さない", "hanasanai")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_present_negative(self):
        godan_expected = {
            "会う": ("会いません", "aimasen"),
            "待つ": ("待ちません", "machimasen"),
            "撮る": ("撮りません", "torimasen"),
            "読む": ("読みません", "yomimasen"),
            "遊ぶ": ("遊びません", "asobimasen"),
            "死ぬ": ("死にません", "shinimasen"),
            "書く": ("書きません", "kakimasen"),
            "行く": ("行きません", "ikimasen"),
            "泳ぐ": ("泳ぎません", "oyogimasen"),
            "話す": ("話しません", "hanashimasen")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_present_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_past(self):
        godan_expected = {
            "会う": ("会った", "atta"),
            "待つ": ("待った", "matta"),
            "撮る": ("撮った", "totta"),
            "読む": ("読んだ", "yonda"),
            "遊ぶ": ("遊んだ", "asonda"),
            "死ぬ": ("死んだ", "shinda"),
            "書く": ("書いた", "kaita"),
            "行く": ("行った", "itta"),
            "泳ぐ": ("泳いだ", "oyoida"),
            "話す": ("話した", "hanashita")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_past(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_past(self):
        godan_expected = {
            "会う": ("会いました", "aimashita"),
            "待つ": ("待ちました", "machimashita"),
            "撮る": ("撮りました", "torimashita"),
            "読む": ("読みました", "yomimashita"),
            "遊ぶ": ("遊びました", "asobimashita"),
            "死ぬ": ("死にました", "shinimashita"),
            "書く": ("書きました", "kakimashita"),
            "行く": ("行きました", "ikimashita"),
            "泳ぐ": ("泳ぎました", "oyogimashita"),
            "話す": ("話しました", "hanashimashita")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_past(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_past_negative(self):
        godan_expected = {
            "会う": ("会わなかった", "awanakatta"),
            "待つ": ("待たなかった", "matanakatta"),
            "撮る": ("撮らなかった", "toranakatta"),
            "読む": ("読まなかった", "yomanakatta"),
            "遊ぶ": ("遊ばなかった", "asobanakatta"),
            "死ぬ": ("死ななかった", "shinanakatta"),
            "書く": ("書かなかった", "kakanakatta"),
            "行く": ("行かなかった", "ikanakatta"),
            "泳ぐ": ("泳がなかった", "oyoganakatta"),
            "話す": ("話さなかった", "hanasanakatta")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_past_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_past_negative(self):
        godan_expected = {
            "会う": ("会いませんでした", "aimasen deshita"),
            "待つ": ("待ちませんでした", "machimasen deshita"),
            "撮る": ("撮りませんでした", "torimasen deshita"),
            "読む": ("読みませんでした", "yomimasen deshita"),
            "遊ぶ": ("遊びませんでした", "asobimasen deshita"),
            "死ぬ": ("死にませんでした", "shinimasen deshita"),
            "書く": ("書きませんでした", "kakimasen deshita"),
            "行く": ("行きませんでした", "ikimasen deshita"),
            "泳ぐ": ("泳ぎませんでした", "oyogimasen deshita"),
            "話す": ("話しませんでした", "hanashimasen deshita")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_past_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_te_form(self):
        godan_expected = {
            "会う": ("会って", "atte"),
            "待つ": ("待って", "matte"),
            "撮る": ("撮って", "totte"),
            "読む": ("読んで", "yonde"),
            "遊ぶ": ("遊んで", "asonde"),
            "死ぬ": ("死んで", "shinde"),
            "書く": ("書いて", "kaite"),
            "行く": ("行って", "itte"),
            "泳ぐ": ("泳いで", "oyoide"),
            "話す": ("話して", "hanashite")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_te_form(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_te_form(self):
        godan_expected = {
            "会う": ("会いまして", "aimashite"),
            "待つ": ("待ちまして", "machimashite"),
            "撮る": ("撮りまして", "torimashite"),
            "読む": ("読みまして", "yomimashite"),
            "遊ぶ": ("遊びまして", "asobimashite"),
            "死ぬ": ("死にまして", "shinimashite"),
            "書く": ("書きまして", "kakimashite"),
            "行く": ("行きまして", "ikimashite"),
            "泳ぐ": ("泳ぎまして", "oyogimashite"),
            "話す": ("話しまして", "hanashimashite")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_te_form(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_te_form_negative(self):
        godan_expected = {
            "会う": ("会わないで", "awanaide"),
            "待つ": ("待たないで", "matanaide"),
            "撮る": ("撮らないで", "toranaide"),
            "読む": ("読まないで", "yomanaide"),
            "遊ぶ": ("遊ばないで", "asobanaide"),
            "死ぬ": ("死なないで", "shinanaide"),
            "書く": ("書かないで", "kakanaide"),
            "行く": ("行かないで", "ikanaide"),
            "泳ぐ": ("泳がないで", "oyoganaide"),
            "話す": ("話さないで", "hanasanaide")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_te_form_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_te_form_negative(self):
        godan_expected = {
            "会う": ("会いませんで", "aimasende"),
            "待つ": ("待ちませんで", "machimasende"),
            "撮る": ("撮りませんで", "torimasende"),
            "読む": ("読みませんで", "yomimasende"),
            "遊ぶ": ("遊びませんで", "asobimasende"),
            "死ぬ": ("死にませんで", "shinimasende"),
            "書く": ("書きませんで", "kakimasende"),
            "行く": ("行きませんで", "ikimasende"),
            "泳ぐ": ("泳ぎませんで", "oyogimasende"),
            "話す": ("話しませんで", "hanashimasende")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_te_form_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_volitional(self):
        godan_expected = {
            "会う": ("会おう", "aou"),
            "待つ": ("待とう", "matou"),
            "撮る": ("撮ろう", "torou"),
            "読む": ("読もう", "yomou"),
            "遊ぶ": ("遊ぼう", "asobou"),
            "死ぬ": ("死のう", "shinou"),
            "書く": ("書こう", "kakou"),
            "行く": ("行こう", "ikou"),
            "泳ぐ": ("泳ごう", "oyogou"),
            "話す": ("話そう", "hanasou")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_volitional(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_volitional(self):
        godan_expected = {
            "会う": ("会いましょう", "aimashou"),
            "待つ": ("待ちましょう", "machimashou"),
            "撮る": ("撮りましょう", "torimashou"),
            "読む": ("読みましょう", "yomimashou"),
            "遊ぶ": ("遊びましょう", "asobimashou"),
            "死ぬ": ("死にましょう", "shinimashou"),
            "書く": ("書きましょう", "kakimashou"),
            "行く": ("行きましょう", "ikimashou"),
            "泳ぐ": ("泳ぎましょう", "oyogimashou"),
            "話す": ("話しましょう", "hanashimashou")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_volitional(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_plain_imperative(self):
        godan_expected = {
            "会う": ("会え", "ae"),
            "待つ": ("待て", "mate"),
            "撮る": ("撮れ", "tore"),
            "読む": ("読め", "yome"),
            "遊ぶ": ("遊べ", "asobe"),
            "死ぬ": ("死ね", "shine"),
            "書く": ("書け", "kake"),
            "行く": ("行け", "ike"),
            "泳ぐ": ("泳げ", "oyoge"),
            "話す": ("話せ", "hanase")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_plain_imperative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_imperative(self):
        godan_expected = {
            "会う": ("会いなさい", "ainasai"),
            "待つ": ("待ちなさい", "machinasai"),
            "撮る": ("撮りなさい", "torinasai"),
            "読む": ("読みなさい", "yominasai"),
            "遊ぶ": ("遊びなさい", "asobinasai"),
            "死ぬ": ("死になさい", "shininasai"),
            "書く": ("書きなさい", "kakinasai"),
            "行く": ("行きなさい", "ikinasai"),
            "泳ぐ": ("泳ぎなさい", "oyoginasai"),
            "話す": ("話しなさい", "hanashinasai")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_imperative(k)
            self.assertEqual(godan_expected[k], (ck, cr))

    def test_polite_imperative_negative(self):
        godan_expected = {
            "会う": ("会いなさるな", "ainasaruna"),
            "待つ": ("待ちなさるな", "machinasaruna"),
            "撮る": ("撮りなさるな", "torinasaruna"),
            "読む": ("読みなさるな", "yominasaruna"),
            "遊ぶ": ("遊びなさるな", "asobinasaruna"),
            "死ぬ": ("死になさるな", "shininasaruna"),
            "書く": ("書きなさるな", "kakinasaruna"),
            "行く": ("行きなさるな", "ikinasaruna"),
            "泳ぐ": ("泳ぎなさるな", "oyoginasaruna"),
            "話す": ("話しなさるな", "hanashinasaruna")
        }

        for k in list(godan_expected.keys()):
            set_global_godan(kanji_to_romaji(k), kanji_to_romaji(k[-1]))
            ck, cr = conjugate_godan_polite_imperative_negative(k)
            self.assertEqual(godan_expected[k], (ck, cr))


if __name__ == "__main__":
    unittest.main()
