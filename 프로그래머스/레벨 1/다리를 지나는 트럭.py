def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    curr_weight = 0
    time = 0
    while truck_weights:
        time += 1
        ar = bridge.pop(0)
        curr_weight -= ar
        if curr_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            curr_weight += truck
    
    while curr_weight > 0:
        time += 1
        ar = bridge.pop(0)
        curr_weight -= ar
    return time