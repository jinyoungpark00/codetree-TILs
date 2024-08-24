import itertools

def count_beautiful_sequences(N, M, A, B):
    # 수열 B의 모든 순열 생성
    permutations_of_B = list(itertools.permutations(B))
    
    count = 0
    
    # 수열 A의 모든 길이 M인 연속 부분 수열을 추출
    for i in range(N - M + 1):
        sub_sequence = tuple(A[i:i+M])  # 부분 수열 추출
        
        # 추출된 부분 수열이 B의 순열 중 하나와 일치하는지 확인
        if sub_sequence in permutations_of_B:
            count += 1
    
    return count

# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
result = count_beautiful_sequences(N, M, A, B)
print(result)