# author: Arthur Gu
# date: 2018.12.7

alphabets = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1,
    't': 0.1,
    'm': -4,
    'q': -3,
    'd': -2,
    'z': -1,
    'j': -0.1,
}


def alphabet_war(fight):

    fight_sum = 0
    padded_fight = 'a' + fight + 'a'
    for i, letter in enumerate(padded_fight[1:-1], start=1):
        left = padded_fight[i-1]
        right = padded_fight[i+1]
        # 只对非牧师的派系字母做检查
        if letter in alphabets and int(alphabets[letter]) != 0:
            transformed = False
            right_value = alphabets.get(right, -1)
            left_value = alphabets.get(left, -1)
            letter_value = alphabets[letter]
            # 如果左右出现了牧师
            if int(right_value) == 0 or int(left_value) == 0:
                # 如果左右是双方牧师则不转化
                if int(right_value) == 0 and int(left_value) == 0 and left != right:
                    transformed = False
                # 否则若牧师与当前字母是同一方则不转化，否则转化
                else:
                    priest_value = right_value if int(right_value) == 0 else left_value
                    transformed = bool(priest_value * letter_value < 0)
            fight_sum += -letter_value if transformed else letter_value
    # 判定战斗结果，左派为正方，右派为负方
    result = "Let's fight again!"
    if fight_sum > 0:
        result = "Left side wins!"
    elif fight_sum < 0:
        result = "Right side wins!"
    return result

if __name__ == '__main__':
    print(alphabet_war("wololooooo"))
