# coding=utf-8
import unittest
from kanji_to_romaji.kanji_to_romaji_module import kanji_to_romaji


class TestKanji(unittest.TestCase):
    def setUp(self):
        print("\nStarting " + self.__module__ + ": " + self._testMethodName)

    def test_arbit_common(self):
        test_and_expected = {
            "私": "watashi",
            "僕": "boku",
            "君": "kimi",
            "早々": "sousou",
            "河": "kawa",
            "曜日": "youbi",
            "今日": "kyou",
            "日記": "nikki",
            "日本": "nihon",
            "日和": "hiyori",
            "明日": "ashita",
            "昨日": "kinou",
            "今日は": "kyou wa"
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_match_starting_at_full(self):
        test_and_expected = {
            "のけ反る": "nokezoru",
            "反る": "kaeru",
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_kanji_iteration_mark(self):
        # regular
        self.assertEqual(kanji_to_romaji("若"), "waka")
        self.assertEqual(kanji_to_romaji("若々しい"), "wakawakashii")

        x = kanji_to_romaji("在")
        self.assertEqual(kanji_to_romaji("在"), x)
        self.assertEqual(kanji_to_romaji("在々"), x * 2)

        # irregular that has to be listed in dict
        self.assertEqual(kanji_to_romaji("精々"), "seizei")
        self.assertEqual(kanji_to_romaji("日々"), "hibi")

    def test_no_particle(self):
        test_and_expected = {
            "災厄の時代": "saiyaku no jidai",  # noun followed by KanjiBlock/noun
            "私のパーティー": "watashi no paatii",  # type change between no character  (hira no kata)
            "さいやくのじだい": "saiyakunojidai",  # no KanjiBlocks and no change in type
            "俺の": "ore no"  # is last character and previous is noun
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_wa_particle(self):
        test_and_expected = {
            "私は嬉": "watashi wa ureshii",  # noun followed by KanjiBlock/adjective
            "わたしはロバート": "watashi wa robaato",  # type change between ha character (hira ha kata)
            "わたしはうれしい": "watashihaureshii",  # no KanjiBlocks and no change in type
            "君の名は": "kimi no na wa"  # is last character and previous is noun
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_he_particle(self):
        test_and_expected = {
            "部屋へ帰る": "heya e kaeru",  # noun followed by KanjiBlock/adjective
            "アパートへくる": "apaato e kuru",  # type change between he character (kata he hira)
            "へやへかえる": "heyahekaeru",  # no KanjiBlocks and no change in type
            "更に向こうへ": "sarani mukou e"  # is last character and previous is noun
        }
        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_to_particle(self):
        test_and_expected = {
            "私と猫-ちゃん": "watashi to neko-chan",  # noun followed by KanjiBlock
            "運命という": "unmei to iu",  # type change between to character (kanji to hira)
            "わたしとねこ-ちゃん": "watashitoneko-chan",  # no KanjiBlocks and no change in type
            "やっと眼を覚ましたかい": "yatto me wo samashita kai"  # no type change, soukon not considered as hiragana
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_ni_particle(self):
        test_and_expected = {
            "友達に会いました": "tomodachi ni aimashita",  # noun followed by KanjiBlock/verb
            "ともだちにあいました": "tomodachiniaimashita",  # no KanjiBlocks and no change in type
            "会いました友達に": "aimashita tomodachi ni"  # is last character and previous is noun
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_mo_particle(self):
        test_and_expected = {
            "背中を押すもの": "senaka wo osu mo no",  # type change (押す) is Kanji to hiragana の
            "私も": "watashi mo"  # is last character and previous is noun
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_type_changes(self):
        self.assertEqual(kanji_to_romaji("ごと."), "goto.")

    def test_kanjiblock_curr_chars_rep(self):
        self.assertEqual(kanji_to_romaji("食べる存在"), "taberu sonzai")

    def test_particle_followed_by_particle(self):
        test_and_expected = {
            "アメリカでは何語が話されていますか": "amerika DE WA nanigo ga hanasarete imasuka".lower(),
            "車には一人分の空きがあった": "kuruma NI WA hitoribun no aki ga atta".lower(),
            "ボタンとはなんですか": "botan TO WA nandesuka".lower(),

            "僕にも責任があるんだ": "boku NI MO sekinin ga arunda".lower(),
            "どんな子供でもそのくらい答えられる": "donna kodomo DE MO sonokurai kotae rareru".lower(),

            "部屋にははいります": "heya NI WA HAirimasu".lower(),
            "私にはにだいめ": "watashi NI WA NIdaime".lower()
        }
        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_godan_conjugations(self):
        self.assertEqual(kanji_to_romaji("遊びます"), "asobimasu")
        self.assertEqual(kanji_to_romaji("遊ばない"), "asobanai")
        self.assertEqual(kanji_to_romaji("遊びません"), "asobimasen")
        self.assertEqual(kanji_to_romaji("遊んだ"), "asonda")
        self.assertEqual(kanji_to_romaji("遊びました"), "asobimashita")
        self.assertEqual(kanji_to_romaji("遊ばなかった"), "asobanakatta")
        self.assertEqual(kanji_to_romaji("遊びませんでした"), "asobimasen deshita")
        self.assertEqual(kanji_to_romaji("遊んで"), "asonde")
        self.assertEqual(kanji_to_romaji("遊びまして"), "asobimashite")
        self.assertEqual(kanji_to_romaji("遊ばないで"), "asobanaide")
        self.assertEqual(kanji_to_romaji("遊びませんで"), "asobimasende")
        self.assertEqual(kanji_to_romaji("遊ぼう"), "asobou")
        self.assertEqual(kanji_to_romaji("遊びましょう"), "asobimashou")
        self.assertEqual(kanji_to_romaji("遊べ"), "asobe")
        self.assertEqual(kanji_to_romaji("遊びなさい"), "asobinasai")
        self.assertEqual(kanji_to_romaji("遊びなさるな"), "asobinasaruna")

    def test_ichidan_conjugations(self):
        self.assertEqual(kanji_to_romaji("食べます"), "tabemasu")
        self.assertEqual(kanji_to_romaji("食べない"), "tabenai")
        self.assertEqual(kanji_to_romaji("食べません"), "tabemasen")
        self.assertEqual(kanji_to_romaji("食べた"), "tabeta")
        self.assertEqual(kanji_to_romaji("食べました"), "tabemashita")
        self.assertEqual(kanji_to_romaji("食べなかった"), "tabenakatta")
        self.assertEqual(kanji_to_romaji("食べませんでした"), "tabemasen deshita")
        self.assertEqual(kanji_to_romaji("食べて"), "tabete")
        self.assertEqual(kanji_to_romaji("食べまして"), "tabemashite")
        self.assertEqual(kanji_to_romaji("食べないで"), "tabenaide")
        self.assertEqual(kanji_to_romaji("食べませんで"), "tabemasende")
        self.assertEqual(kanji_to_romaji("食べよう"), "tabeyou")
        self.assertEqual(kanji_to_romaji("食べましょう"), "tabemashou")
        self.assertEqual(kanji_to_romaji("食べろ"), "tabero")
        self.assertEqual(kanji_to_romaji("食べなさい"), "tabenasai")
        self.assertEqual(kanji_to_romaji("食べなさるな"), "tabenasaruna")

    def test_not_using_verb_stem_by_itself(self):
        self.assertEqual(kanji_to_romaji("反映"), "hanei")
        self.assertEqual(kanji_to_romaji("反映 して"), "hanei shite")

        self.assertEqual(kanji_to_romaji("反映して"), "hanei shite")

        self.assertEqual(kanji_to_romaji("映して"), "utsushite")
        self.assertEqual(kanji_to_romaji("映し"), "eigashi")

        self.assertEqual(kanji_to_romaji("灯りました"), "tomorimashita")
        self.assertEqual(kanji_to_romaji("灯りを見ます"), "akari wo mimasu")

    def test_irregular_conjugation(self):
        test_and_expected = {
            # 勉強 not a listed suru verb
            "勉強する": "benkyou suru",
            "勉強しない": "benkyou shinai",
            "勉強しません": "benkyou shimasen",
            "勉強した": "benkyou shita",
            "勉強しました": "benkyou shimashita",
            "勉強しなかった": "benkyou shinakatta",
            "勉強しませんでした": "benkyou shimasendeshita",
            "勉強して": "benkyou shite",
            "勉強しまして": "benkyou shimashite",
            "勉強しないで": "benkyou shinaide",
            "勉強しませんで": "benkyou shimasende",
            "勉強しよう": "benkyou shiyou",
            "勉強しましょう": "benkyou shimashou",
            "勉強しろ": "benkyou shiro",
            "勉強しい": "benkyou shii",
            "勉強しなさい": "benkyou shinasai",
            "勉強しなさるな": "benkyou shinasaruna",

            # 了 a listed suru verb
            "了する": "ryou suru",
            "了しない": "ryou shinai",
            "了しません": "ryou shimasen",
            "了した": "ryou shita",
            "了しました": "ryou shimashita",
            "了しなかった": "ryou shinakatta",
            "了しませんでした": "ryou shimasen deshita",
            "了して": "ryou shite",
            "了しまして": "ryou shimashite",
            "了しないで": "ryou shinaide",
            "了しませんで": "ryou shimasende",
            "了しよう": "ryou shiyou",
            "了しましょう": "ryou shimashou",
            "了しろ": "ryou shiro",
            "了しい": "ryou shii",
            "了しなさい": "ryou shinasai",
            "了しなさるな": "ryou shinasaruna",

            "付いて来ます": "tsuite kimasu",
            "付いて来ない": "tsuite konai",
            "付いて来ません": "tsuite kimasen",
            "付いて来た": "tsuite kita",
            "付いて来ました": "tsuite kimashita",
            "付いて来なかった": "tsuite konakatta",
            "付いて来ませんでした": "tsuite kimasen deshita",
            "付いて来て": "tsuite kite",
            "付いて来まして": "tsuite kimashite",
            "付いて来ないで": "tsuite konaide",
            "付いて来ませんで": "tsuite kimasende",
            "付いて来よう": "tsuite koyou",
            "付いて来ましょう": "tsuite kimashou",
            "付いて来い": "tsuite koi",
            "付いて来なさい": "tsuite kinasai",
            "付いて来なさるな": "tsuite kinasaruna",

            "カッと来ます": "katto kimasu",
            "カッと来ない": "katto konai",
            "カッと来ません": "katto kimasen",
            "カッと来た": "katto kita",
            "カッと来ました": "katto kimashita",
            "カッと来なかった": "katto konakatta",
            "カッと来ませんでした": "katto kimasen deshita",
            "カッと来て": "katto kite",
            "カッと来まして": "katto kimashite",
            "カッと来ないで": "katto konaide",
            "カッと来ませんで": "katto kimasende",
            "カッと来よう": "katto koyou",
            "カッと来ましょう": "katto kimashou",
            "カッと来い": "katto koi",
            "カッと来なさい": "katto kinasai",
            "カッと来なさるな": "katto kinasaruna",
        }

        for key in list(test_and_expected.keys()):
            self.assertEqual(kanji_to_romaji(key), test_and_expected[key])

    def test_spacing_before_kanji(self):
        self.assertEqual(kanji_to_romaji("車はどこに行きましたか"), "kuruma wa doko ni ikimashita ka")
        # no being read as particle
        self.assertEqual(kanji_to_romaji("どの電車を取るべきですか"), "do no densha wo toru bekidesuka")

    def test_unknown_character(self):
        self.assertEqual(kanji_to_romaji("駲"), "駲")
        self.assertEqual("\\u99f2".encode().decode("unicode_escape"), "駲")


if __name__ == "__main__":
    unittest.main()
