# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import kanji_to_romaji
from generators.ichidan_verb_conjugators import conjugate_ichidan_plain_te_form, \
    conjugate_ichidan_plain_te_form_negative, \
    conjugate_ichidan_plain_volitional, conjugate_ichidan_polite_volitional, conjugate_ichidan_plain_imperative, \
    conjugate_ichidan_polite_imperative, conjugate_ichidan_polite_present_affirmative, \
    conjugate_ichidan_plain_negative, \
    conjugate_ichidan_polite_present_negative, conjugate_ichidan_polite_past, conjugate_ichidan_plain_past, \
    conjugate_ichidan_polite_past_negative, conjugate_ichidan_plain_past_negative, \
    conjugate_ichidan_polite_imperative_negative, conjugate_ichidan_polite_te_form, \
    conjugate_ichidan_polite_te_form_negative, set_global_ichidan


class TestIchidanVerbConjugators(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_polite_present_affirmative(self):
        ichidan_expected = {
            "寝る": ("寝ます", "nemasu"),
            "出来る": ("出来ます", "dekimasu"),
            "見つける": ("見つけます", "mitsukemasu")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_present_affirmative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_negative(self):
        ichidan_expected = {
            "寝る": ("寝ない", "nenai"),
            "出来る": ("出来ない", "dekinai"),
            "見つける": ("見つけない", "mitsukenai")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_present_negative(self):
        ichidan_expected = {
            "寝る": ("寝ません", "nemasen"),
            "出来る": ("出来ません", "dekimasen"),
            "見つける": ("見つけません", "mitsukemasen")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_present_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_past(self):
        ichidan_expected = {
            "寝る": ("寝た", "neta"),
            "出来る": ("出来た", "dekita"),
            "見つける": ("見つけた", "mitsuketa")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_past()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_past(self):
        ichidan_expected = {
            "寝る": ("寝ました", "nemashita"),
            "出来る": ("出来ました", "dekimashita"),
            "見つける": ("見つけました", "mitsukemashita")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_past()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_past_negative(self):
        ichidan_expected = {
            "寝る": ("寝なかった", "nenakatta"),
            "出来る": ("出来なかった", "dekinakatta"),
            "見つける": ("見つけなかった", "mitsukenakatta")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_past_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_past_negative(self):
        ichidan_expected = {
            "寝る": ("寝ませんでした", "nemasen deshita"),
            "出来る": ("出来ませんでした", "dekimasen deshita"),
            "見つける": ("見つけませんでした", "mitsukemasen deshita")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_past_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_te_form(self):
        ichidan_expected = {
            "寝る": ("寝て", "nete"),
            "出来る": ("出来て", "dekite"),
            "見つける": ("見つけて", "mitsukete")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_te_form()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_te_form(self):
        ichidan_expected = {
            "寝る": ("寝まして", "nemashite"),
            "出来る": ("出来まして", "dekimashite"),
            "見つける": ("見つけまして", "mitsukemashite")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_te_form()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_te_form_negative(self):
        ichidan_expected = {
            "寝る": ("寝ないで", "nenaide"),
            "出来る": ("出来ないで", "dekinaide"),
            "見つける": ("見つけないで", "mitsukenaide")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_te_form_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_te_form_negative(self):
        ichidan_expected = {
            "寝る": ("寝ませんで", "nemasende"),
            "出来る": ("出来ませんで", "dekimasende"),
            "見つける": ("見つけませんで", "mitsukemasende")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_te_form_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_volitional(self):
        ichidan_expected = {
            "寝る": ("寝よう", "neyou"),
            "出来る": ("出来よう", "dekiyou"),
            "見つける": ("見つけよう", "mitsukeyou")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_volitional()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_volitional(self):
        ichidan_expected = {
            "寝る": ("寝ましょう", "nemashou"),
            "出来る": ("出来ましょう", "dekimashou"),
            "見つける": ("見つけましょう", "mitsukemashou")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_volitional()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_plain_imperative(self):
        ichidan_expected = {
            "寝る": ("寝ろ", "nero"),
            "出来る": ("出来ろ", "dekiro"),
            "見つける": ("見つけろ", "mitsukero")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_plain_imperative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_imperative(self):
        ichidan_expected = {
            "寝る": ("寝なさい", "nenasai"),
            "出来る": ("出来なさい", "dekinasai"),
            "見つける": ("見つけなさい", "mitsukenasai")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_imperative()
            self.assertEqual(ichidan_expected[k], (ck, cr))

    def test_polite_imperative_negative(self):
        ichidan_expected = {
            "寝る": ("寝なさるな", "nenasaruna"),
            "出来る": ("出来なさるな", "dekinasaruna"),
            "見つける": ("見つけなさるな", "mitsukenasaruna")
        }

        for k in list(ichidan_expected.keys()):
            set_global_ichidan(k[:-1], kanji_to_romaji(k)[:-2])
            ck, cr = conjugate_ichidan_polite_imperative_negative()
            self.assertEqual(ichidan_expected[k], (ck, cr))


if __name__ == "__main__":
    unittest.main()
