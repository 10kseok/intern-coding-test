def solution_1st(arr: list) -> list:
    '''
    정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
    ex) input : [4,3,2,1] output : [4,3,2]
        input : [10]      output : [-1]
    
    ## 제한 조건
    1. arr 길이는 1 이상
    2. 중복 x
    '''
    n = len(arr)
    if n < 1 or len(set(arr)) != n:
        raise Exception("제한 조건 위반")
    if n == 1:
        return [-1]
    
    min_value, min_idx = float('inf'), 0
    for idx in range(len(arr)):
        if min_value > arr[idx]:
            min_value = arr[idx]
            min_idx = idx
            
    return arr[:min_idx] + arr[min_idx + 1:]

def solution_2nd(s: str) -> str:
    '''
    입력된 문자열을 큰 것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수
    s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주
    ex) input : "Zbcdefg" output : "gfedcbZ"

    ## 제한 사항
    1. str은 길이 1 이상인 문자열입니다.
    '''
    return ''.join(sorted(s, reverse=True))
    
if __name__=="__main__":
    assert solution_1st([4, 3, 2, 1]) == [4, 3, 2], "오답입니다."
    assert solution_1st([10]) == [-1], "오답입니다."
    assert solution_1st([1, 214, 54363, 2144, 12]) == [214, 54363, 2144, 12], "오답입니다."
    try: solution_1st([10, 10]); assert False, "제한 조건에서 벗어나는 데이터입니다."
    except: pass 
    try: solution_1st([]); assert False, "제한 조건에서 벗어나는 데이터입니다."
    except: pass 
    print("1번 문제: 주어진 테스트 케이스 모두 통과입니다.")
    
    assert solution_2nd("Zbcdefg") == "gfedcbZ", "오답입니다."
    assert solution_2nd("ABC") == "CBA", "오답입니다."
    assert solution_2nd("abc") == "cba", "오답입니다."
    assert solution_2nd("abcABC") == "cbaCBA", "오답입니다."
    print("2번 문제: 주어진 테스트 케이스 모두 통과입니다.")

