import VoiceCore as vo
import MeCab

text = """
こんにちわぁ、九歳です❤️。みんなぁ〜。元気ぃ？
"""

# 漢字変換関数定義
def kanjiToKatakana(text: str) -> str :
    t = MeCab.Tagger("-Oyomi")
    return t.parse(text)

# 漢字変換
sce = kanjiToKatakana(text) 

# 変換
sce = vo.scenario(sce)


# 発音
vo.speak(sce)
