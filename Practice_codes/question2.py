
def main():
    n=int(input())
    lst=[]
    dictt={}
    for i in range(n):
        t=int(input())
        lst.append(t)
    for i in lst:
        if i in dictt:
            dictt[i]+=1
        else:
            dictt[i]=1
    sorted_lst=dict(sorted(dictt.items()))
    for i  in sorted_lst:
        print(i,sorted_lst[i])
main()

def main():
    