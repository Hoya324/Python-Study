def solution(phone_book):
    answer = True
    hash_map = {} # 빈 딕셔너리 생성
    for phone_number in phone_book: # 해쉬맵 초기화
        hash_map[phone_number] = 1
    for phone_number in phone_book: # 
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: # 본인을 제외한 접두사가 있는지 판단
                answer = False
    return answer