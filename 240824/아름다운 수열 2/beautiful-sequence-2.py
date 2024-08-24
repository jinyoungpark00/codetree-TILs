from collections import Counter

def count_beautiful_sequences(N, M, A, B):
    # 수열 B의 빈도를 계산
    b_counter = Counter(B)
    
    # 수열 A에서 길이 M인 연속 부분 수열들의 빈도를 확인하며 비교
    a_counter = Counter(A[:M])  # 처음 M개의 숫자로 부분 수열 빈도 계산
    count = 0
    
    # 첫 부분 수열이 아름다운 수열인지 확인
    if a_counter == b_counter:
        count += 1
    
    # 슬라이딩 윈도우 방식으로 이후의 부분 수열 처리
    for i in range(M, N):
        # 윈도우를 한 칸 오른쪽으로 이동: 맨 앞의 숫자를 제거하고, 새로 들어오는 숫자를 추가
        a_counter[A[i-M]] -= 1
        if a_counter[A[i-M]] == 0:
            del a_counter[A[i-M]]  # 빈도가 0인 숫자는 제거
        
        a_counter[A[i]] += 1
        
        # 현재 윈도우의 빈도와 B의 빈도가 동일한지 확인
        if a_counter == b_counter:
            count += 1
    
    return count

# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
result = count_beautiful_sequences(N, M, A, B)
print(result)