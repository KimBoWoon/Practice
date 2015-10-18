__author__ = '보운'

import random

english = [
    "I have an appointment with E.C".upper(),
    "A million girls would kill for this job".upper(),
    "It sounds like a great opportunity".upper(),
    "What makes you think i'm not interested in fashion?".upper(),
    "She's not supposed to be here until 9".upper(),
    "I want the driver to drop me off at 9:30 and pick me up at 9:45 sharp".upper(),
    "I wonder if she's lost any of that weight yet".upper(),
    "She's hopeless and totally wrong for it".upper(),
    "I am going to have to do that myself".upper(),
    "How is it that you know who she is and i didn't".upper(),
    "You pick up her coffee order on the way".upper(),
    "I'm almost there".upper(),
    "Is there some reason that my coffee isn't here".upper(),
    "Has she died or something".upper(),
    "If mess up my head is on the chopping block".upper(),
    "It's on it's way".upper(),
    "Calls roll to voice mail".upper(),
    "You are chained to that desk".upper(),
    "She's not available".upper(),
    "You get coffee and you run errands".upper(),
    "I'm in charge of the schedule".upper(),
    "Deal with it".upper(),
    "That's what i meant".upper(),
    "That's not what i asked you".upper(),
    "I couldn't have been clearer".upper(),
    "Make sure we have pier59 at 8a.m tomorrow".upper(),
    "Get him on the phone".upper(),
    "Leave it".upper(),
    "Do you have some prior commitment".upper(),
    "I'm about to walk in".upper(),
    "The phone is going to be ringing off the hock".upper(),
    "Miranda's pushed the run-through up a half an hour".upper(),
    "must have been".upper(),
    "i've seen all this before".upper(),
    "Why is it so impossible to put together a decent run-through".upper(),
    "It should work".upper(),
    "it's a tough call".upper(),
    "It's just that both those belts look exactly the same to me".upper(),
    "You think this has nothing to do with you".upper(),
    "You should've seen the look she gave me".upper(),
    "That is why those girls are so skinny".upper()
]
korean = [
    '에밀리 찰튼과 약속이 되어있는데요',
    '수 백만 여자들이 목숨걸고 이자리를 노리죠',
    '정말 좋은 기회 같다',
    '어째서 제가 패션에 관심이 없다고 생각해요?',
    '그녀는 9시 전에는 출근하지 않는데',
    '운전사 한테 9시 30분에 나를 내려주고 정확히 9:45분에 데리러 오라고 해',
    '그녀가 살이 좀 빠졌는지 궁금하내',
    '그녀는 영 별로이고 정말 안 맞아요',
    '내가 직접해야겠어',
    '어떻게 너는 그녀가 누군지 아는데 나는 모르지?',
    '오는길에 커피 좀 사와',
    '거의 다 왔어요',
    '내 커피가 없는 이유는 뭐야',
    '(사러가서) 죽었니?',
    '니가 일을 망치면 내 머리가 도마에 올라가',
    '지금 진행중이에요',
    '전화가 음성메일로 넘어가',
    '절대 자리에 붙어있어',
    '(그녀는) 안계십니다',
    '넌 커피타고 잔심부름해',
    '난 그녀의 스케쥴을 관리해',
    '알아서 처리해',
    '내 말이 그말이야',
    '그건 내가 요구한게 아니야',
    '내가 분명 말했을 탠데',
    '내일 아침 8시에 pier59를 사용할 수 있게해놔',
    '전화로 그를 연결해',
    '냅둬',
    '더 급한 일 있니?',
    '막 들어가고 있어요',
    '끊임없이 전화가 걸려 올꺼야',
    '미란다가 최종 리허설을 30분 앞당겼어',
    '틀림없이 새것이 형편없겠군',
    '이런건 전에 다 봤어',
    '어째서 리허설을 무난하게 끝내는게 불가능하니?',
    '그건 괜찮을꺼에요',
    '결정하기 힘들어요',
    '제 눈에는 벨트들이 똑같아 보여요',
    '넌 이게 너와 아무상관없는거라 생각하는구나',
    '그 여자가 나한테 지은 표정을 봤어야해',
    '그래서 그 여자들이 마르나봐'
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
