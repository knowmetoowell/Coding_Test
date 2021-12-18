import heapq

def solution(operations):
    answer = [0]*2
    heap_list = []
    
    for i in range(len(operations)):
        a = operations[i].split(" ")
        if a[0] == "I":
            heapq.heappush(heap_list, int(a[1]))
        else:
            if heap_list:
                if a[1] == "-1":
                    heapq.heappop(heap_list)
                else:
                    max_heap_list =[]    
                    for number in heap_list:
                        heapq.heappush(max_heap_list, (-number, number))
                    heapq.heappop(max_heap_list)
                    heap_list = []
                    while (len(max_heap_list)>0):
                        heapq.heappush(heap_list, heapq.heappop(max_heap_list)[1])
    
    if (len(heap_list)>0):
        answer[0] =max(heap_list)
        answer[1] =heapq.heappop(heap_list)
    
    return answer


# oper = ["I 16", "D 1"]
oper = ["I 16","I -5643","D -1","D 1","D 1","D -1","D -1","D -1","D -1"]
print(solution(oper))