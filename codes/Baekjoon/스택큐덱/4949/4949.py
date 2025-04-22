# 4949 균형잡힌 세상

sentence = ""
# 문장 담는 리스트
lst = []
while True:
    sentence = input()
    # '.'이면 종료
    if sentence == '.':
        break
    lst.append(sentence)

# 문장 한 줄씩
for i in range(len(lst)):
    stack = []
    stack.clear()
    flag = 0
    # 한 문장의 단어를 훑는다.
    for j in range(len(lst[i])):
        # print(stack)
        # '('이면 스택에 추가
        if lst[i][j] == '(':
            stack.append('(')
        # '['이면 스택에 추가
        elif lst[i][j] == '[':
            stack.append('[')
        # ')'일 때
        elif lst[i][j] == ')':
            if len(stack) == 0:         # 스택이 비어 있으면 불균형 확정
                flag = 1
                break
            elif stack[-1] != '(':      # 마지막 요소가 '(' 아니면 불균형 확정
                flag = 1
                break
            elif stack[-1] == '(':      # 마지막 요소가 '('이면 그 요소 제거
                stack.pop()
        # ']'일 때
        elif lst[i][j] == ']':
            if len(stack) == 0:         # 스택이 비어 있으면 불균형 확정
                flag = 1
                break
            elif stack[-1] != '[':      # 마지막 요소가 '[' 아니면 불균형 확정
                flag = 1
                break
            elif stack[-1] == '[':      # 마지막 요소가 '['이면 그 요소 제거
                stack.pop()
    # 반복문을 끝까지 돌고(flag=0) 스택이 비어 있으면 균형
    if flag == 0 and len(stack) == 0:
        print("yes")
    # 도중에 flag=1이고 break한 경우 불균형
    else:
        print("no")