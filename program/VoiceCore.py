from pydub import AudioSegment
from pydub.playback import play
from typing import List, Dict

VOICE_FILES = {
    "あ": "../あ行/あ.wav",
    "い": "../あ行/い.wav",
    "う": "../あ行/う.wav",
    "え": "../あ行/え.wav",
    "お": "../あ行/お.wav",
    "か": "../か行/か.wav",
    "き": "../か行/き.wav",
    "く": "../か行/く.wav",
    "け": "../か行/け.wav",
    "こ": "../か行/こ.wav",
    "さ": "../さ行/さ.wav",
    "し": "../さ行/し.wav",
    "す": "../さ行/す.wav",
    "せ": "../さ行/せ.wav",
    "そ": "../さ行/そ.wav",
    "た": "../た行/た.wav",
    "ち": "../た行/ち.wav",
    "つ": "../た行/つ.wav",
    "て": "../た行/て.wav",
    "と": "../た行/と.wav",
    "な": "../な行/な.wav",
    "に": "../な行/に.wav",
    "ぬ": "../な行/ぬ.wav",
    "ね": "../な行/ね.wav",
    "の": "../な行/の.wav",
    "は": "../は行/は.wav",
    "ひ": "../は行/ひ.wav",
    "ふ": "../は行/ふ.wav",
    "へ": "../は行/へ.wav",
    "ほ": "../は行/ほ.wav",
    "ま": "../ま行/ま.wav",
    "み": "../ま行/み.wav",
    "む": "../ま行/む.wav",
    "め": "../ま行/め.wav",
    "も": "../ま行/も.wav",
    "や": "../や行/や.wav",
    "ゆ": "../や行/ゆ.wav",
    "よ": "../や行/よ.wav",
    "ら": "../ら行/ら.wav",
    "り": "../ら行/り.wav",
    "る": "../ら行/る.wav",
    "れ": "../ら行/れ.wav",
    "ろ": "../ら行/ろ.wav",
    "わ": "../わ行/わ.wav",
    "を": "../わ行/を.wav",
    "ん": "../わ行/ん.wav",
    "が": "../が行/が.wav",
    "ぎ": "../が行/ぎ.wav",
    "ぐ": "../が行/ぐ.wav",
    "げ": "../が行/げ.wav",
    "ご": "../が行/ご.wav",
    "ざ": "../ざ行/ざ.wav",
    "じ": "../ざ行/じ.wav",
    "ず": "../ざ行/ず.wav",
    "ぜ": "../ざ行/ぜ.wav",
    "ぞ": "../ざ行/ぞ.wav",
    "だ": "../だ行/だ.wav",
    "ぢ": "../だ行/ぢ.wav",
    "づ": "../だ行/ず.wav",
    "で": "../だ行/で.wav",
    "ど": "../だ行/ど.wav",
    "ば": "../ば行/ば.wav",
    "び": "../ば行/び.wav",
    "ぶ": "../ば行/ぶ.wav",
    "べ": "../ば行/べ.wav",
    "ぼ": "../ば行/ぼ.wav",
    "ぱ": "../ぱ行/ぱ.wav",
    "ぴ": "../ぱ行/ぴ.wav",
    "ぷ": "../ぱ行/ぷ.wav",
    "ぺ": "../ぱ行/ぺ.wav",
    "ぽ": "../ぱ行/ぽ.wav",
    "きゃ": "../きゃ行/きゃ.wav",
    "きゅ": "../きゃ行/きゅ.wav",
    "きょ": "../きゃ行/きょ.wav",
    "しゃ": "../しゃ行/しゃ.wav",
    "しゅ": "../しゃ行/しゅ.wav",
    "しょ": "../しゃ行/しょ.wav",
    "ちゃ": "../ちゃ行/ちゃ.wav",
    "ちゅ": "../ちゃ行/ちゅ.wav",
    "ちょ": "../ちゃ行/ちょ.wav",
    "にゃ": "../にゃ行/にゃ.wav",
    "にゅ": "../にゃ行/にゅ.wav",
    "にょ": "../にゃ行/にょ.wav",
    "ひゃ": "../ひゃ行/ひゃ.wav",
    "ひゅ": "../ひゃ行/ひゅ.wav",
    "ひょ": "../ひゃ行/ひょ.wav",
    "ぴゃ": "../ぴゃ行/ぴゃ.wav",
    "ぴゅ": "../ぴゃ行/ぴゅ.wav",
    "ぴょ": "../ぴゃ行/ぴょ.wav",
    "みゃ": "../みゃ行/みゃ.wav",
    "みゅ": "../みゃ行/みゅ.wav",
    "みょ": "../みゃ行/みょ.wav",
    "りゃ": "../りゃ行/りゃ.wav",
    "りゅ": "../りゃ行/りゅ.wav",
    "りょ": "../りゃ行/りょ.wav",
    "っ": "../その他/っ.wav",
    "ふぁ": "../その他/ふぁ.wav",
    "ふぃ": "../その他/ふぃ.wav",
    "ふぇ": "../その他/ふぇ.wav",
    "ふぉ": "../その他/ふぉ.wav",
    "ふゅ": "../その他/ふゅ.wav",
    "うぁ": "../その他/うぁ.wav",
    "うぃ": "../その他/うぃ.wav",
    "うぇ": "../その他/うぇ.wav",
    "うぉ": "../その他/うぉ.wav",
    "ゔぁ": "../その他/ゔぁ.wav",
    "ゔぃ": "../その他/ゔぃ.wav",
    "ゔぇ": "../その他/ゔぇ.wav",
    "ゔぉ": "../その他/ゔぉ.wav",
    "つぁ": "../その他/つぁ.wav",
    "つぃ": "../その他/つぃ.wav",
    "つぇ": "../その他/つぇ.wav",
    "つぉ": "../その他/つぉ.wav",
    "ちぇ": "../その他/ちぇ.wav",
    "しぇ": "../その他/しぇ.wav",
    "じゃ": "../その他/じゃ.wav",
    "じゅ": "../その他/じゅ.wav",
    "じぇ": "../その他/じぇ.wav",
    "じょ": "../その他/じょ.wav",
    "てぃ": "../その他/てぃ.wav",
    "でぃ": "../その他/でぃ.wav",
    "とぅ": "../その他/とぅ.wav",
    "どぅ": "../その他/どぅ.wav",
    "、": "../その他/、.wav",
    "。": "../その他/、.wav"
}


def save(fileName: str, charArr: List[str], tone: List[int] = None) -> None:
    pitch = tone
    if pitch is not None:
        assert len(charArr) == len(pitch), "配列の長さが一致していない"
    x = None
    for i in range(len(charArr)):
        y = None
        if charArr[i] in VOICE_FILES:
            y = AudioSegment.from_wav(VOICE_FILES[charArr[i]])
            if pitch[i] is not None:
                newPitch = int(y.frame_rate * (2.0 ** (pitch[i] / 12)))
                y = y._spawn(y.raw_data, overrides={'frame_rate': newPitch})
            if x is None:
                x = y
            else:
                x = x + y
    if x is not None:
        x.export(fileName, format="wav")


def speak(charArr: List[str], tone: List[int] = None) -> None:
    pitch = tone
    if pitch is not None:
        assert len(charArr) == len(pitch), "配列の長さが一致していない"
    x = None
    for i in range(len(charArr)):
        y = None
        if charArr[i] in VOICE_FILES:
            y = AudioSegment.from_wav(VOICE_FILES[charArr[i]])
            if pitch is not None:
                newPitch = int(y.frame_rate * (2.0 ** (pitch[i] / 12)))
                y = y._spawn(y.raw_data, overrides={'frame_rate': newPitch})
            if x is None:
                x = y
            else:
                x = x + y
    if x is not None:
        play(x)


def intonation(pitchDic: Dict[int, int], pitchLength: int) -> List[int]:
    l = []
    for i in range(0, pitchLength):
        if i in pitchDic.keys():
            l.append(pitchDic[i])
        else:
            if i > 0:
                l.append(l[i - 1])
            else:
                l.append(1)
    return l


KATAKANA_HIRAGANA_CORRESPONDENCE_TABLE = {
    "ア": "あ",
    "イ": "い",
    "ウ": "う",
    "エ": "え",
    "オ": "お",
    "カ": "か",
    "キ": "き",
    "ク": "く",
    "ケ": "け",
    "コ": "こ",
    "サ": "さ",
    "シ": "し",
    "ス": "す",
    "セ": "せ",
    "ソ": "そ",
    "タ": "た",
    "チ": "ち",
    "ツ": "つ",
    "テ": "て",
    "ト": "と",
    "ナ": "な",
    "ニ": "に",
    "ヌ": "ぬ",
    "ネ": "ね",
    "ノ": "の",
    "ハ": "は",
    "ヒ": "ひ",
    "フ": "ふ",
    "ヘ": "へ",
    "ホ": "ほ",
    "マ": "ま",
    "ミ": "み",
    "ム": "む",
    "メ": "め",
    "モ": "も",
    "ヤ": "や",
    "ユ": "ゆ",
    "ヨ": "よ",
    "ラ": "ら",
    "リ": "り",
    "ル": "る",
    "レ": "れ",
    "ロ": "ろ",
    "ワ": "わ",
    "ヲ": "を",
    "ン": "ん",
    "ガ": "が",
    "ギ": "ぎ",
    "グ": "ぐ",
    "ゲ": "げ",
    "ゴ": "ご",
    "ザ": "ざ",
    "ジ": "じ",
    "ズ": "ず",
    "ゼ": "ぜ",
    "ゾ": "ぞ",
    "ダ": "だ",
    "ヂ": "ぢ",
    "ヅ": "づ",
    "デ": "で",
    "ド": "ど",
    "バ": "ば",
    "ビ": "び",
    "ブ": "ぶ",
    "ベ": "べ",
    "ボ": "ぼ",
    "パ": "ぱ",
    "ピ": "ぴ",
    "プ": "ぷ",
    "ペ": "ぺ",
    "ポ": "ぽ",
    "ャ": "ゃ",
    "ュ": "ゅ",
    "ョ": "ょ",
    "ァ": "ぁ",
    "ィ": "ぃ",
    "ゥ": "ぅ",
    "ェ": "ぇ",
    "ォ": "ぉ"
}


def katakanaToHiragana(text: str) -> str:
    s = ""
    for i in text:
        if i in KATAKANA_HIRAGANA_CORRESPONDENCE_TABLE:
            s += KATAKANA_HIRAGANA_CORRESPONDENCE_TABLE[i]
        else:
            s += i
    return s


VOWEL = {
    "あ": [
        "あ", "か", "さ", "た", "な",
        "は", "ま", "や", "ら", "わ",
        "が", "ざ", "ば", "ぱ",
        "きゃ", "しゃ", "じゃ", "ちゃ", "にゃ",
        "ひゃ", "ぴゃ", "みゃ", "ふぁ",
        "うぁ", "ゔぁ", "つぁ", "しぇ"
    ],
    "い": [
        "い", "き", "し", "ち", "に",
        "ひ", "み", "り",
        "ぎ", "じ", "び", "ぴ",
        "ふぃ", "うぃ", "ゔぃ",
        "つぃ", "てぃ"
    ],
    "う": [
        "う", "く", "す", "つ", "ぬ",
        "ふ", "む", "ゆ", "る",
        "ぐ", "ず", "ぶ", "ぷ",
        "きゅ", "しゅ", "じゅ", "ちゅ", "にゅ",
        "ひゅ", "ぴゅ", "みゅ",
        "りゅ", "とぅ", "どぅ"
    ],
    "え": [
        "え", "け", "せ", "て", "ね",
        "へ", "め", "れ"
                  "げ", "ぜ", "べ", "ぺ",
        "ふぇ", "うぇ", "ゔぇ", "つぇ",
        "ちぇ", "しぇ", "じぇ"
    ],
    "お": [
        "お", "こ", "そ", "と", "の",
        "ほ", "も", "よ", "ろ", "を",
        "ご", "ぞ", "ぼ", "ぽ",
        "きょ", "しょ", "じょ", "ちょ", "にょ",
        "ひょ", "ぴょ", "みょ", "りょ",
        "ふぉ", "うぉ", "ゔぉ", "つぉ"
    ]
}


def longtoneToVowel(texts: List[str]) -> List[str]:
    ts = []
    for i in range(0, len(texts)):
        cangeCher = False
        if texts[i] == "ー" and i > 0:
            for j in VOWEL.keys():
                if texts[i - 1] in VOWEL[j]:
                    ts.append(j)
                    cangeCher = True
        if not cangeCher:
            ts.append(texts[i])
    return ts


SPECIAL_CONVERSION_TABLE = {
    "〜": "ー",
    "ぁ": "あ",
    "ぃ": "い",
    "ぅ": "う",
    "ぇ": "え",
    "ぉ": "お"
}


def specialConverter(texts: List[str]) -> List[str]:
    l = []
    for i in texts:
        if i in SPECIAL_CONVERSION_TABLE.keys():
            l.append(SPECIAL_CONVERSION_TABLE[i])
        else:
            l.append(i)
    return l


def komojoConverter(texts: List[str]) -> List[str]:
    l = []
    for i in range(len(texts)):
        if i + 1 < len(texts):
            if texts[i + 1] in ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ", "ゃ", "ゅ", "ょ", "ゎ"]:
                if texts[i] + texts[i + 1] in VOICE_FILES.keys():
                    l.append(texts[i] + texts[i + 1])
                else:
                    l.append(texts[i])
            elif texts[i] in ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ", "ゃ", "ゅ", "ょ", "ゎ"]:
                if i - 1 >= 0:
                    if texts[i - 1] + texts[i] in VOICE_FILES.keys():
                        pass
                    else:
                        l.append(texts[i])
                else:
                    l.append(texts[i])
            else:
                l.append(texts[i])
        else:
            if texts[i] in ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ", "ゃ", "ゅ", "ょ", "ゎ"]:
                if i - 1 >= 0:
                    if texts[i - 1] + texts[i] in VOICE_FILES.keys():
                        pass
                    else:
                        l.append(texts[i])
                else:
                    l.append(texts[i])
            else:
                l.append(texts[i])
    return l


def scenario(text: str) -> List[str]:
    text = katakanaToHiragana(text)
    li = list(text)
    li = komojoConverter(li)
    li = specialConverter(li)
    li = longtoneToVowel(li)
    return li
