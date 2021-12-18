import heapq
def scoville_return(a, b):
    sco = a+(b*2)

    return sco

def solution(scoville, K):
    sco = 0
    
    heapq.heapify(scoville)
    cnt = 0
    while(scoville[0]<K):
        try:
            sco=heapq.heappop(scoville)
            heapq.heappush(scoville, scoville_return(sco, heapq.heappop(scoville)))
            cnt+=1
        except:
            cnt = -1
            break
            
    return cnt


        





    

scoville = [1, 2, 3, 9, 10, 12]
a = solution(scoville, 7)

print(a)

