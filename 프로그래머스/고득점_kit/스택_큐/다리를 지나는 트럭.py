from collections import deque

import collections

DUMMY_TRUCK = 0


class Bridge(object):
    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return "Bridge({}/{} : [{}])".format(
            self._current_weight, self._max_weight, list(self._queue)
        )


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


# 내 풀이
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # bridge_length 대가 다리에 올라갈 수 있음
    # weight 이하까지 무게 가능
    # truck_weights 대기 트럭 배열
    times = 1
    truck_weights = deque(truck_weights)  # deque로 변경
    A = deque()
    A.append([bridge_length, truck_weights.popleft()])  # (다리 길이, 트럭 무게)

    while A:
        times += 1
        bridge_weight = 0
        # 다리 길이 - 1, 다 못지나 갔으면 총 무게를 더함
        for i in range(len(A)):
            A[i][0] -= 1
            if A[i][0] == 0:
                A.pop()
            else:
                bridge_weight += A[i][1]

        # 대기 트럭이 없으면 스킵
        if not truck_weights:
            continue
        # 다리에 더 올라갈 수 있으면 올라감
        if bridge_weight + truck_weights[0] <= weight and len(A) + 1 <= bridge_length:
            A.appendleft([bridge_length, truck_weights.popleft()])

    answer = times
    return answer
