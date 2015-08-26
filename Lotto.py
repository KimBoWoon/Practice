__author__ = 'user'

# 랜덤한 숫자를 뽑기위해 랜덤모듈을 가져온다
import random

class Lotto:
    # 여섯개의 숫자를 담을 리스트
    lotto = []
    # 보너스 숫자
    bonus = 0

    # 여섯개의 숫자를 뽑아내는 함수
    def randomPick(self):
        # 동일한 숫자없이 여섯개의 숫자를 뽑아냄
        while True:
            # 1 ~ 45 사이의 랜덤한 숫자를 하나 뽑는다
            num = random.randint(1, 45)
            # 만약 뽑은 숫자가 리스트에 존재하면 다시 숫자를 뽑고
            # 없으면 리스트에 추가한다
            if (num in self.lotto):
                continue
            else:
                self.lotto.append(num)

            # 여섯개를 뽑았으면 반복 종료
            if (len(self.lotto) == 6):
                break

    def pickBonus(self):
        # 보너스 숫자를 뽑는다
        # 보너스도 중복이 되면 안된다
        while True:
            # 1 ~ 45 사이의 랜덤한 숫자를 하나 뽑는다
            num = random.randint(1, 45)
            # 만약 뽑은 숫자가 리스트에 존재하면 다시 숫자를 뽑고
            # 없으면 리스트에 추가한다
            if (num in self.lotto):
                continue
            else:
                self.bonus = num
                break

    def printLotto(self):
        # 보기좋게 오름차순 정렬
        self.lotto.sort()
        # 뽑힌 로또 숫자 출력
        print('오늘의 당첨번호!!!')
        print(self.lotto)
        print('뽀나스 번호는!!')
        print(self.bonus)

lotto = Lotto()

lotto.randomPick()
lotto.pickBonus()
lotto.printLotto()