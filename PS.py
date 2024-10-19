#9012. 괄호

for _ in range(int(input())):
    s = input()  # 괄호 문자열 입력
    stack = 0  # 괄호의 균형 확인
    valid = True  # 올바른 문자열인지 여부

    for char in s:  # 문자열의 각 문자를 순회
        if char == '(':  # 여는 괄호일 경우
            stack += 1  # 스택 증가
        elif char == ')':  # 닫는 괄호일 경우
            stack -= 1  # 스택 감소
        if stack < 0:  # 만약 스택이 음수가 되면
            valid = False  # 올바른 문자열이 아님
            break

    # 스택이 0이고 유효하면 "YES", 그렇지 않으면 "NO"를 출력
    if valid and stack == 0:
        print("YES")
    else:
        print("NO")
