#%%
def solution(gems):
    start, end = 0, 0
    check = len(set(gems))
    shortest = len(gems)+1
    gem_dict = {}
    answer = []
    while end < len(gems):
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1
        end +=1

        if len(gem_dict) == check:
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start +=1
                elif shortest > end-start:
                    shortest = end-start
                    answer = [start+1, end]
                    break
                else:
                    break
    
    return answer



        

#%%
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
#%%
print(gems[0:4])
#%%
my_set = set(gems)
li = list(my_set)
li2 = list(my_set)
print(li)
print(li.sort())
print(li2)
# %%
li.remove(값)