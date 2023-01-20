def solution(babbling):
    answer = 0
    for i in babbling :
        for j in range(4) : 
            if i.startswith('aya') :
                i = i.replace('aya','',1)
            elif i.startswith('ye') :
                i = i.replace('ye','',1)
            elif i.startswith('woo') :
                i = i.replace('woo','',1)
            elif i.startswith('ma') :
                i = i.replace('ma','',1)
        if len(i) == 0 :
            answer += 1

    return answer