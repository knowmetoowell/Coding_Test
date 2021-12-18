def solution(numbers):
    answer = []
    
    point=len(numbers)
    
    for i in range(point):
        for j in range(i+1, point):
            answer.append(numbers[i]+numbers[j])

    my_set= set(answer)
    li = list(my_set)
    li.sort()
    
    return li

https://programmers.co.kr/learn/courses/30/lessons/68644