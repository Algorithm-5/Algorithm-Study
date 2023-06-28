import heapq


def solution(scoville, K):
    # 리스트를 힙으로
    heap = scoville
    heapq.heapify(heap)

    # 섞은 횟수
    mix_count = 0

    # 제일 작은 스코빌이 K보다 작을 때
    while heap[0] < K:
        # 남은 음식이 하나밖에 없을 때
        if len(heap) < 2:
            return -1

        # 실행
        mix = heapq.heappop(heap) + heapq.heappop(heap) * 2

        # 섞은 음식을 다시 힙에 집어넣음
        heapq.heappush(heap, mix)

        # 섞은 횟수 +1
        mix_count += 1

    # 최종 섞은 횟수 return
    return mix_count
