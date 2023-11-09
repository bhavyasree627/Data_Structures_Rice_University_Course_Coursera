import heapq
def assign_threads(n,times):
    res=[]
    initial=[(0,i)for i in range(n)]
    for i in times:
        time,thread=heapq.heappop(initial)
        res.append((thread,time))
        heapq.heappush(initial,(i+time,thread))
    return res

n,m=map(int,input().split())
li=list(map(int,input().split())) 
answer=assign_threads(n,li)
for i in answer:
    print(i[0]," ",i[1])