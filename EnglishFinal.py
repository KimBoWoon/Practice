__author__ = '보운'

import random

english = [
    "I'll Guard it with my life".upper(),
    "Please you must be in desperate need of hard liquor".upper(),
    "Did you mention my good looks and my killer charm".upper(),
    "Why don't you send it over".upper(),
    "Tell them i wanna move the preview up to today at 12:30".upper(),
    "We're not expected until tuesday".upper(),
    "I see your point".upper(),
    "This is the dress we have designed specifically and exclusively for you".upper(),
    "Have emily give you the key".upper(),
    "My sell phone didn't work".upper(),
    "I'm Picking up for miranda priestly".upper(),
    "It's deadly".upper(),
    "In her way".upper(),
    "You deal with it".upper(),
    "Her opinion is the only one that matters".upper(),
    "I've already messengered your outfit over to the shoot".upper(),
    "I would like you to deliver the book to my home tonight".upper(),
    "You do exactly what i'm about".upper(),
    "This is of the utmost importance".upper(),
    "Emily does it all the time".upper(),
    "I rushed out of an investment committee meeting".upper(),
    "It really wasn't that big a deal".upper(),
    "It shouldn't be a problem, should it? And you can do anything, right".upper(),
    "The book better be here no later than 3".upper(),
    "I've been on hold".upper(),
    "I was wondering if you could make the impossible possible".upper(),
    "Not a chance".upper(),
    "I think it makes a difference".upper(),
    "I'm on this new diet".upper(),
    "When I feel like i'm about to faint i eat a cube of cheese".upper(),
    "It's definitely working".upper(),
    "I'm just one stomach flue away from my goal weight".upper(),
    "Stop fidgeting".upper(),
    "just deal with it you have to be here".upper(),
    "I plan my whole year around this".upper(),
    "you're a vision".upper(),
    "Thank god i saved your job".upper(),
    "Turns out i'm not as nice at you thought".upper(),
    "It weren't for the stupid boyfriend i'd have to whisk you away right here and now".upper(),
    "Do you actually say things like that to people".upper(),
    "Give my best to the boyfriend".upper(),
    "I kept trying to leave".upper(),
    "I didn't have a choice".upper(),
    "Can we at least talk about this".upper(),
    "Paris is the most important week of my entire year".upper(),
    "I need the best possible team with me".upper(),
    "If you don't go i'll assume you're not serious about your future".upper(),
    "The decision's yours".upper(),
    "Emily would die, her whole life is about paris she hasn't eaten in weeks".upper(),
    "i've got so muck to deal with".upper()
]
korean = [
    '목숨걸고 지킨다.',
    '그녀 밑에서 일하려면 독한술이 절대 필요할꺼에요',
    '내 멋진 모습과 살인 미소에 대해 썻나요',
    '나한테 그걸 보내봐요',
    '오늘 12시30분으로 프리뷰 시간 당기고 싶다고 전해',
    '화요일 까지는 예상 못했는데',
    '무슨 말인지 알겠다',
    '이건 특히 당신을 위해 우리가 특별히 디자인한 드레스에요',
    '에밀리한테 키를 받아',
    '휴대폰이 안됐어',
    '미란다 심부름으로 가지러왔어요',
    '죽여줘요(아주 위험해요)',
    '그녀 방식으로',
    '당신이 처리해요',
    '그녀 의견은 절대적으로 중요해',
    '촬영장에 당신 의상을 보내놨어요',
    '나는 너가 우리집에 책을 가져다 놓았으면 좋겠어',
    '내 말대로 해야되',
    '이거 가장 중요해',
    '에밀리도 항상 그래요',
    '난 투자 회의에서 급히 달려왔다고',
    '그렇게 큰일 아니였어요',
    '우리가 출판계에 있는 모든 사람을 알고 있으니 그리 문제될 것도 없지 않니? 그리고 넌 뭐든지 할 수 있잖니, 그렇지',
    '그 책은 늦어도 세시까지 와야할꺼야',
    '쭉 기다리고 있어요',
    '불가능 한것도 어떻게든 가능하게 안될까요',
    '절대 안돼요',
    '생각이 달라질꺼에요',
    '나 다이어트중이거든',
    '현기증 올 때 쯔음 치즈 한조각 먹어',
    '확실히 효과가 있내요',
    '토 한번만 하면 목표 제중 달성이야',
    '건들거리좀마 (안절부절, 초조)',
    '그만 포기해 여기서 해야할일이나해',
    '일년내내 이날만을 손꼽았거든요',
    '당신 아름답내요',
    '일자리를 구해준 보람이 있내요',
    '난 당신이 생각한 것처럼 그렇게 멋진 사람이 아니에요',
    '남자친구는 어디에다 때 놓고 여기서 배회 하고 있지?',
    '아무여자 한테나 그렇게 말하죠',
    '남자친구에게 안부전해줘요',
    '계속 나오려고 했는데',
    '어쩔수없었어',
    '우리얘기 좀 하면 안될까',
    '파리행은 내 일년에서 가장 중요한 일이야',
    '가능한 최상한 팀으로 준비해',
    '네가 안간다면 니 미래가 심각해 질텐데',
    '결정은 네 몫이야',
    '에밀리 죽을꺼에요 파리에 얼마나 가고싶어 했는데 몇주나 굶었어요',
    '지금도 해야할일이 태산인데'
]
r = random.Random()
cnt = 1

while True:
    rNum = r.randint(0, len(korean) - 1)
    print(cnt)
    print(korean[rNum])

    string = input('>> ')

    if string.upper() == english[rNum]:
        print('정답')
    else:
        print('오답')
        print(english[rNum].title())

    cnt += 1
