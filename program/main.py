# 言わせるテスト
import VoiceCore as vo

# 言わせる文字列
sce = vo.scenario("こんにちわ〜、すずきデス")

# 言葉のイントネーション
tone = vo.intonation({1: 3, 4: 4,  7: 1 , 8: 3, 10: 5, 11: 1}, len(sce) )

# 言わせる
vo.speak(sce, tone=tone)

# 保存する
vo.save("作品例/test.wav", sce, tone=tone)
