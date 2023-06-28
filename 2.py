import heapq


def solution(jobs):
    # 작업을 요청 시간 순으로 정렬
    jobs.sort()
    n = len(jobs)
    current_time, total_time = 0, 0
    heap = []

    while jobs or heap:
        # 현재 시간 이전에 요청된 작업이 있으면 우선순위 큐에 추가
        while jobs and jobs[0][0] <= current_time:
            start_time, required_time = jobs.pop(0)

            # 우선순위 큐는 작업을 시작할 시간이 빠른 순서대로 정렬
            heapq.heappush(heap, (required_time, start_time))

        # 우선순위 큐가 비어있지 않으면 작업 수행
        if heap:
            required_time, start_time = heapq.heappop(heap)
            current_time += required_time
            total_time += current_time - start_time
        else:
            current_time = jobs[0][0]

    # 작업 처리시간 평균 return
    return total_time // n
