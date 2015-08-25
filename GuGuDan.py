__author__ = 'user'

#GuGuDan
# 3 * 3 행렬 생각해서 3step 증가
# 각 행마다 첫 열은 2, 5, 8단이 저장됨
for x in range(2, 9, 3):
    for y in range(1, 10):
        # 한 줄에 세 개의 단이 출력되어야함
        for z in range(0, 3):
            # 10단은 제외
            if (10 == (x + z)):
                break
            # 열마다 z값을 더해주면 원하는 구구단을 출력할 수 있음
            print("{0} * {1} = {2}  ".format((x + z), y, (x + z) * y), end=' ')
        print()
    print()