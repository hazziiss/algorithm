import sys
T = int(input())
name_dict = {}

for t in range(T) :
    name, in_out = sys.stdin.readline().split()

    if in_out == 'enter' :
        name_dict[name] = 'enter'
    else :
        del name_dict[name]    
name_dict_re = sorted(name_dict, reverse=True)   
print(*name_dict_re,sep='\n') 
