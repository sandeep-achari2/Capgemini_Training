def main():
    n=int(input())
    while n>0:
        n1,n2=map(int,input().split())
        dict={}
        listt=[]
        for i in range(n1):
            name,age,hobbies,favourate_chocolate=input().split()
            age=int()
            dict[name]=[age,hobbies,favourate_chocolate]
        for i in range(n2):
            name=input()
            listt.append(name)
    
        for i in listt:
            if i in dict:
                print(f'{dict[name][0]},{dict[name][1]},{dict[name][2]}')
    n-=1
    
main()
        