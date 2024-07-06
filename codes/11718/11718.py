# 11718 그대로 출력하기
import sys

while True:
    try:
        print(input())
    except EOFError:
        break