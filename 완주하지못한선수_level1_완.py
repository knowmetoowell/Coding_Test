def solution(participant, completion):
    
    import collections
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]

    


participant = ['dd','cc','aa', 'cc']
completion = ['cc','dd','aa']


