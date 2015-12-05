from turtle import *
import t

a = ['도쿄가 수도인 나라는?', '만리장성이 있는 나라는?', '세계에서 가장 땅이 넓은 나라는?',
     '유럽의 장화라고 불리는 나라는?', '옥토버페스트 축제가 열리는 나라는?',
     '2016년 하계 올림픽이 열리는 나라는?', '2018년 동계올림픽이 열리는 나라는?',
     '2008년 기준 커피 생산량이 가장 많은 나라는?', '산타클로스의 고향은?',
     '4대 문명 중 아프리카에서 발생한 문명을 가진 나라는?']
answer = ['일본', '중국', '러시아', '이탈리아', '독일', '브라질', '대한민국', '브라질', '핀란드', '이집트']
i = 0
cnt = 0
position = [(0, 0), (220, 50), (340, -120), (290, -120), (170, -70), (0, -70)]

while i < len(a):
    print(a[i])
    s = input()
    if s == answer[i]:
        print("정답")
        left(180)
        begin_fill()
        color("red")
        penup()
        goto(position[i][0], position[i][1])
        pendown()
        circle(50)
        end_fill()
    else:
        cnt += 1
        if cnt > 2:
            break
    i += 1
