# チャットボット
from typing import List
import random
import VoiceCore as vo
import MeCab

# 簡単なボットのクラス - - - - - - - - - - - - - - - - - - -

class Bot :
	""" 
	ボットのクラス
	検索方法は "AND" "OR" "MATCH" "DEFAULT" の四つ
	"""
	
	def __init__(self) :
		self.answers = []
		
	def set(self, querys: List[str], reply: str, at: str = "OR") -> None :
		""" 応答の作成 """
		""" querys: 質問(複数), reply: 応答(単数), at: 検索方法 """
		t = {	"querys": querys, "replys": [reply], "type": at }
		self.answers.append(t)
	
	def set_random(self, querys: List[str], replys: List[str], at: str = "OR") -> None :
		""" 応答の作成 (応答は複数の中からランダム) """
		""" querys: 質問(複数), reply: 応答(複数), at: 検索方法 """
		t = {	"querys": querys, "replys": replys, "type": at }
		self.answers.append(t)
		
	
	def response(self, query: str) -> str :
		""" query: 質問, return: 応答 """
		retxar = None
		default = None
		for i in self.answers :
			if i["type"] == "AND" :
				b = True
				for j in i["querys"] :
					if j not in query :
						b = False
						break
				if b :
					retxar = i["replys"] 
					break
			elif i["type"] == "OR" :
				b = False 
				for j in i["querys"] :
					if j in query :
						b = True
						break
				if b :
					retxar = i["replys"] 
					break
			elif i["type"] == "MATCH" :
				b = False 
				for j in i["querys"] :
					if j == query :
						b = True
						break 
				if b :
					retxar = i["replys"] 
					break
			elif i["type"] == "DEFAULT" :
				retxar = i["replys"]
				
		if retxar!=None :
			return random.choice(retxar)
		else :
			return None
			
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 喋らせる関数 - - - - - - - - - - - - - - - - - - - - - - - - - - -

def speak(text: str) -> None :
	t = MeCab.Tagger("-Oyomi")
	sce = t.parse(text)
	sce = vo.scenario(sce)
	vo.speak(sce)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #


bot = Bot()
bot.set(None, "はろー", at="DEFAULT")
bot.set(["おはよう", "こんちわ", "おやすみ"], "おきてえぇ", at="OR")
bot.set(["バーチャルのじゃロリ狐娘ユーチューバーおじさん"], "のじゃー", at="MATCH")
bot.set_random(["はい", "どーも"], ["ふぁっきゅ", "ふぁっきゅー"], at="AND")

print("テキストを入力して下さい ( control + C で終了 ) ")

while True :
	s = input("> ")
	r = bot.response(s)
	if r!= None : 
		print("\t\t\t"+r+" <")
		speak(r)
		
