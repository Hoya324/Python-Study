import sys
def BEP():
    A, B, C = list(map(int, sys.stdin.readline().split()))
#A는 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등
#B는 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등
#C는 노트북 가격
    if C > B:
        X = A/(C-B)
        result = int(X+1)
    else:
        result = -1

    return result
        
print(BEP())
