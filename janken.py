import random

cp_hands = ["グー", "チョキ", "パー"]

win = int(0)
lose = int(0)
draw = int(0)
count = int(0)

name = input("あなたの名前を入力：")
print("🎮 じゃんけんゲーム開始！（3勝で終了）\n")

while win < 3 and lose < 3:
    print("じゃんけん ポン！\n")

    ur_hands = input(f"{name}の手を入力（グー、チョキ、パー）：")

    if ur_hands not in cp_hands:
        print("無効な入力です。（グー・チョキ・パー で入力）")
        continue
    
    computer = random.choice(cp_hands)
    print("コンピュータの手：", computer)
    print()

    if ur_hands == computer:
        print("あいこ！もう一回！\n")
        draw += 1
        count += 1
        
    elif (ur_hands == "グー" and computer == "チョキ") or \
         (ur_hands == "チョキ" and computer == "パー") or \
         (ur_hands == "パー" and computer == "グー"):
        print("あなたの勝ち！\n")
        win += 1
        count += 1

    else:
        print("あなたの負け…\n")
        lose += 1
        count += 1
        

#結果表示
print("ゲーム終了！\n")
if win == 3:
    print(f"🎉 3勝達成！{name}の勝ち！\n")
elif lose == 3:
    print(f"😢 3敗しました…{name}の負け。\n")

result = input("結果を表示しますか？(y/n) ")
print()
if result == "y":
    print("-" * 30)
    print()
    print(f"戦績\n 勝ち：{win}回 / 負け：{lose}回 / 引き分け：{draw}回\n")
    print(f"勝率\n {(win / count) * 100:.1f}%\n")
    print(f"負率\n {(lose / count) * 100:.1f}%\n")
    print(f"引分率\n {(draw / count) * 100:.1f}%\n")
    print("-" * 30)

elif result == "n":
    print("お疲れさまでした！")

else:
    print("エラー")