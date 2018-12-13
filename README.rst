Kanji\_to\_Romaji 3
===================

| Converted from Python2 to Python3, primarily using the 2to3 utility.
| The original can be found here: https://github.com/rcamba/kanji_to_romaji

| Formerly kana\_to\_romaji
| *Tries* to translate Kanji to Romaji with the help of `JMdict`_
| Some typograhic characters are also translated since one of the
  original goals was to make the string printable in ascii

Installation
------------

| ``git clone https://github.com/NetDenizen/kanji_to_romaji3``
| ``install.bat``
| Or if you have Linux:
| ``./install.sh``


Usage
-----

``ktr.py`` is a script included to be used in the command line provided
you have your python’s script folder in your environment variables

| > ktr.py 友達に会いました
| tomodachi ni aimashita

The more common usage will probably to be used in another program:

::

    from kanji_to_romaji import kanji_to_romaji
    print kanji_to_romaji("友達に会いました")

Argument must be in Unicode

More examples
-------------

| 私は嬉: watashi wa ureshii
| 更に向こうへ: sarani mukou e
| 友達に会いました: tomodachi ni aimashita
| 車には一人分の空きがあった: kuruma ni wa hitoribun no aki ga atta
| bl∞dy☆: bl dy
| 乷: 乷 (not in Kanji unicode range)

| See ``tests\test_kanji.py`` for more examples
| **Note**: The particles は (ha/wa) or へ (he/e) won’t always be
  translated properly. Same goes for some of the Kanji translations
  since there are multiple possible readings for some of them depending
  on the context.

.. _JMdict: http://www.edrdg.org/jmdict/edict_doc.html
