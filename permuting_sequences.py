def permute(list):
    if not list:
        return [list]
    else:
        res = []
        for i in range(len(list)):
            rest = list[:i] + list[i+1:]
            for x  in permute(rest):
                res.append(list[i:i+1] + x)
        return res


def subset(list,size):
    if size == 0 or  not list:
        return [list[:0]]
    else:
        result = []
        for i in range(len(list)):
            pick = list[i:i+1]
            rest = list[:i] + list[i+1:]
            for  x  in subset(rest,size-1):
                result.append(pick + x )
        return  result


def  combo(list,size):
    if  size == 0 or not size:
        return [list[:0]]
    else:
        result = []
        for i in range(0,(len(list) - size) + 1 ):
            pick = list[i:i+1]
            rest = list[i+1:]
            for x  in combo(rest,size -1):
                result.append(pick + x)
        return  result



print(permute([1,2,3]))
print(permute("arman"))
print(len(permute("arman")))


print(combo([1,2,3],3))
print(combo("aro",3))
print(combo("aro",2))
print(combo("aro",4))
print(combo((1,2,3,4),3))
for i in range(0,6):
    print(combo("help",i))


print(subset([1,2,3,4],2))
print(subset("Arman",6))
for i in range(0,6):
    print(i,subset("arman",i))
