def heapify(i,n,arr,swaps):
    small=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]<arr[small]:
        small=left
    if right<n and arr[right]<arr[small]:
        small=right
    if small!=i:
        arr[i],arr[small]=arr[small],arr[i]
        swaps.append((i, small))
        heapify(small,n,arr, swaps)
        
def heap_func(arr,n):
    swapped=[]
    for i in range(n//2,-1,-1):
        heapify(i,n,arr,swapped)
    print(len(swapped))
    for i in swapped:
        print(i[0]," ",i[1])
n=int(input())
li=list(map(int,input().split()))
heap_func(li,n)
        