n,c = map(int,input().split())
houses = [int(input()) for _ in range(n)]

houses.sort()
c -= 2

def binary_search(houses,c,start,end,dist):
    if c == 0:
        return dist
    
    mid = (start + end) // 2

    c -= 1

    dist = min(dist,houses[mid] - houses[start], houses[end] - houses[mid])
    
    if houses[mid] - houses[start] > houses[end] - houses[mid]:
        return binary_search(houses,c,start,mid-1,dist)
    
    else:
        return binary_search(houses,c,mid+1,end,dist)

print(binary_search(houses,c,0,n-1,1e9))



