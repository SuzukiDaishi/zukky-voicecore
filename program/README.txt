VoiceKit(version1.10)

VoiceKitとは - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

僕のボイスロイドを作るためのpythonAPI及び声集のことです
pythonでライブラリを作った理由として、
このライブラリはもともとチャットボットを作成する為に作られました
それが最も簡単なのがPythonだったからです。
原則、漢字、外国語、などは未対応ですが
和布蕪などのライブラリに頼る事で解消できます。
このライブラリではpython3.5以上そしてpydubが動く環境が必須となります
以上の環境が満たされていれば基本的に動くと思います
このライブラリは基本的に深夜テンションで作られた代物ゆえ、
かなりバグが存在しています、発見された方は是非ご連絡下さい。

準備 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
python3.5以上
pydubをpipでインストール

(mac)
下記のサイトに従い
「Homebrew」「pyenv」「python3.5以上」「pip」をインストール
https://qiita.com/crankcube@github/items/15f06b32ec56736fc43a
下記のサイトに従い
「pydub」「ffmpeg」をインストール
https://qiita.com/itoru257/items/8af2902d8ce851ae74ea

(win)
知らないけど
最低限これがあれば動きます
「ffmpeg」「pydub」「python3.5以上」


プログラムのサンプル  - - - - - - - - - - - - - - - - - - - - - - - - - - - 

実行方法
	cd をこのディレクトリにして
	python main.py
	python main2.py
	python main3.py
	でそれぞれ実行

main.py
	基本的な使い方の説明

main2.py 
	和布蕪(形態素分解ライブラリ)との互換のやり方

main3.py 
	以上を踏まえた簡単なデモ

voiceCoreライブラリ説明 - - - - - - - - - - - - - - - - - - - - - - - - - 

関数: speak(charArr: List[str], tone List[int] = None) -> None
	- charArr: 言わせる文字の配列
	- [ tone ]: 言わせるイントネーション(抑揚は1~12(半音ずつで計12音))(charArrと配列長を合わせる)
指定された文字配列、音程配列を元に
50音のwavファイルを編集、結合させ発声させる関数


関数: save(fileName: str, charArr: List[str], tone: List[int] = None) -> None
	- fileName: 保存するファイル名
	- charArr: 言わせる文字の配列
	- [ tone ]: 言わせるイントネーション(抑揚は1~12(半音ずつで計12音))(charArrと配列長を合わせる)
指定された文字配列、音程配列を元に
50音のwavファイルを編集、結合させカレントディレクトリにwav形式で保存する関数

関数: scenario(text: str) -> List[str]
	- text: 最適なListに変換する文字列
文字列を文字ごとに分解し配列化
その際「きゃ」などは１文字として認識させ
speak関数、save関数などに最適化した文字配列を作製する関数
カタカナも可、「ー」も可

関数: intonation(pitchDic: Dict[int, int], pichLength: int ) -> List[int]
	- pitchDic: イントネーションの変更点の辞書
	- pichLength: 戻り値の配列長
イントネーションを安全に記述できる関数
pitchDic引数に{ 何文字目 : 変更後のピッチ }の形で指定
pichLength引数に戻り値の配列長

変数(private): VOICE_FILES: Dict[str, str]
キーに"あ"などの五十音
中身にwavファイルの場所が入っている

変数(private): KATAKANA_HIRAGANA_CORRESPONDENCE_TABLE: Dict[str, str]
カタカナとひらがなの変換表

変数(private): VOWEL: Dict[List[str]]
文字の母音の対応表

変数(private): SPECIAL_CONVERSION_TABLE: Dict[str]
特殊な変換表
左に替えたい文字
右に替えた後の文字

関数(private): katakanaToHiragana(text: str) -> str
	- text: 文字列
引数の文字列からカタカナのみをひらがなに変更する
その際KATAKANA_HIRAGANA_CORRESPONDENCE_TABLEを参照する

関数(private): longtoneToVowel(texts: List[str]) -> List[str]
	- texts: 文字列のリスト
引数の文字列のリストから
「ー」を前音の母音に変換する

関数(private): specialConverter(texts: List[str]) -> List[str] 
	- texts: 文字列のリスト
引数を対応表を元に変換できない文字を変換する

関数(private): komojoConverter(texts: List[str]) -> List[str] 
	- texts: 文字列のリスト
小文字を解釈、変換する

アップデートログ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

全体通しての方針 :
	安全かつ直感的な記述
	チャットボット系API, 形態素分解系APIとの互換を持たせる

version1.0
	 ボイスのみ

version1.1
	方針: とりあえず声が出せる
	VoiceCoreのPython用のライブラリを実装
	声をつなげる関数speakの実装

version1.2
	VoiceCoreのPython用のライブラリを実装
	speak関数の機能を「実際に鳴らす」に変更
	前のspeak関数はsave関数に変更

varsion1.3
	細かなバグの修正

varsion1.4
	方針: 抑揚がある
	一部音声の取り直し
	speak関数, save関数にデフォルト引数pitchを追加
	さらに、未実装関数scenarioを定義

varsion1.5
	scenario関数の実装
	および、細かなバグの修正

varsion1.6
	方針: MeCabとの互換をよくする
	scenario関数でカタカナが対応

varsion1.7
	ライブラリ名をvoiceおよびvoiceCoreからVoiceKitに変更
	longtoneToVowel関数で「ー」に対応

varsion1.8
	方針: pich引数の指定を簡単にする
	specialConverter関数でその他の文字の変換が可能
	intonation関数の定義のみ

varsion1.9
	intonation関数の実装
	いくつかの関数の引数名の変更
	未対応だった文字の対応
	バグの修正

varsion 1.10
	main.pyの他にmain2.py、main3.pyを作成、改良
	main.pyは基本的なVoiceCoreライブラリの使い方
	main2.pyは和布蕪との連携の仕方
	main3.pyは上を使った簡単なチャットボットのデモ
	scenario関数などのアルゴリズムの変更、改良
	これは高速化ではなく可読性、保守性に重点をおいたもの
	バグの修正
	現状のピッチシフトでは同時にスピードも変わってしまう
	ここからの目標としては、
	タイムストレッチ、ピッチシフトを個別に行う
	イントネーションの自動指定などに重きをおく
	などを頑張りたい

利用規約 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

僕に許可取って
