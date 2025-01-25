

def isMatc(s,p) :

    s_len = 0
    if s == p:
        return True

    for i in range(len(p)-2):
        s_len += 1
        if s[s_len-1] != p[i]:
            if p[i] == ".":
                continue
            elif p[i] == "*":
                if i != 0 and s[s_len-1] == p[i-1]:
                    temp = s_len
                    while True:
                        s_len += 1
                        if s[temp-1] != s[i]:
                            break
                        if(i < len(s)):
                            i+= 1
                        else:
                            break
                elif p[i-1] == ".":
                    continue
                else:
                    return False

            else:
                return False
    print( "s_len = ",s_len,"len(s)",len(s))
    if s_len == len(s)-1:
        return True
    return False



s = "HHHHlll"
p = "H*l*"

dogru = isMatc(s,p)

if  dogru:
    print("dogru")
else:
    print("not dogru")