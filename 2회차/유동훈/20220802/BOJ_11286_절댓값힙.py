# https://www.acmicpc.net/problem/11286
# 절댓값 힙

# 풀이
import sys
import heapq
input = sys.stdin.readline #시간초과 때문에

N = int(input())
arr = []

for i in range(N): # N번만큼 반복
    x = int(input())
    if x!=0:
        heapq.heappush(arr, (abs(x),x)) #힙에 원소를 추가할 때 튜플형태로 넣어주면
                                        #튜플의 첫 번째 원소를 기준으로 최소 힙을 구성하게 된다.(우선순위, 값)
    else:
        if len(arr) == 0:#배열이 비어있으면 0을 출력
            print(0)
        else:
            print(heapq.heappop(arr)[1])
            #root node 위치에 있는 값 삭제하고 출력
            # 실제값은 튜플의 두번째 자리에 저장되어 있어 [1] 인덱싱을 통해 접근