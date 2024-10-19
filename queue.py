#10845. 큐

from collections import deque 
import sys 
input = sys.stdin.readline  # 입력 속도 최적화를 위해 사용

q = deque()  # deque를 사용해 큐를 초기화

for _ in range(int(input())):  # 입력된 명령의 수만큼 반복
    command = input().split()  # 명령어와 값을 분리

    if command[0] == 'push':  # 'push' 명령이면 정수를 큐에 추가
        q.append(command[1])
    elif command[0] == 'pop':  # 'pop' 명령이면 큐의 앞에서 값을 제거하고 출력
        print(q.popleft() if q else -1)  # 큐가 비어있으면 -1을 출력
    elif command[0] == 'size':  # 'size' 명령이면 큐의 크기를 출력
        print(len(q))
    elif command[0] == 'empty':  # 'empty' 명령이면 큐가 비었는지 확인
        print(0 if q else 1)  # 비었으면 1, 아니면 0을 출력
    elif command[0] == 'front':  # 'front' 명령이면 큐의 앞에 있는 값을 출력
        print(q[0] if q else -1)  # 큐가 비어있으면 -1을 출력
    elif command[0] == 'back':  # 'back' 명령이면 큐의 뒤에 있는 값을 출력
        print(q[-1] if q else -1)  # 큐가 비어있으면 -1을 출력
