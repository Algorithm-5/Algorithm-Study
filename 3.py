import heapq


def solution(operations):
    answer = []
    heap = []

    for op in operations:
        # 첫 글자가 I이면 삽입
        if op[0] == "I":
            heapq.heappush(heap, int(op[2:]))

        # 아니면 삭제
        elif len(heap) > 0:
            # 문자열의 3번째 문자가 1이면 최댓값 삭제
            if op[2] == "1":
                heapq.nlargest(1, heap)[0]
                heap.remove(max(heap))

            # 아니면 최솟값 삭제
            else:
                heapq.heappop(heap)

    if len(heap) == 0:
        answer = [0, 0]
    else:
        # 최댓값, 최솟값 return
        answer = [max(heap), heap[0]]

    return answer
