# 테스트 케이스 개수 입력
Test = int(input())

# 각 테스트 케이스 처리
for _ in range(Test):
    sen = input()  # 문장 입력
    words = sen.split()  # 단어별로 나누기
    reverse = [word[::-1] for word in words]  # 각 단어 뒤집기
    result = ' '.join(reverse)  # 단어들을 공백으로 결합
    print(result)  # 결과 출력
