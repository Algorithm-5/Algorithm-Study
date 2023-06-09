def solution(nums):
    return min(len(nums) / 2, len({i : 1 for i in nums})) 
    # 리스트에 있는 값들을 딕셔너리로 변환 (중복되는 요소는 제거되고 {num : 1} 형태로 저장된다)
    # N/2마리의 폰켓몬 중 가장 많은 종류의 폰켓몬은 N/2 종류와 딕셔너리의 크기(폰켓몬 종류의 수) 중 작은 값이다.
    # --> 딕셔너리의 크기가 N/2 마리를 넘을 수 있는 경우 때문에 상한을 N/2 으로 해줌
