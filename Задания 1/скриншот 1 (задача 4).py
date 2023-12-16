
s = [1, 2, 3, 4, 5, 7]
def useless(s):
    if len(s) > 0:
        max_num = max(s)
        return max_num / len(s)
    else:
        return None

print(useless(s))
    
    