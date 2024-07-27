a, b, c = map(int, input().split())

mult = a * b * c

def get_sum(mult):
    if mult < 10:
        return mult
    
    return get_sum(mult // 10) + mult % 10

print(get_sum(mult))