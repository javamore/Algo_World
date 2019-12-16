"""
For a given array A of n *distinct* numbers, find all triples (x,y,z) 
   s.t. x + y = z. (x, y, z are distinct numbers)

   e.g.,
   
   find([1, 4, 2, 3, 5]) returns [(1,3,4), (1,2,3), (1,4,5), (2,3,5)]

   similar to twosum(unique pairs), differnce is this one you need to find the sum by yourself

"""

def find(a):
    a.sort()
    result = []
    for pivot, pivot_val in enumerate(a):
        left, right = 0, len(a)-1

        # do partion  
        while left < right:
            # eliminate duplications, using while loop to jump the same elements, a[left] == a[left-1] or a[right] == a[right-1]
            while left < right and a[left] == a[left - 1]:
                left += 1 
            while left < right and a[right] == a[right - 1]:
                right -= 1   
            # found the sum or "z"
            if right != pivot and left != pivot and a[left] + a[right] == pivot_val:
                result.append((a[left],a[right],pivot_val))
                left += 1
                right -= 1

            elif a[left] + a[right] > pivot_val:
                right -= 1
            else:
                left += 1          
    return result

if __name__ == "__main__":

    print(find([1, 4, 2, 3, 5]))
    print(find([-5, -2, -3, 3, 5, 2]))
    print(find([-2,-2,1,1,-1,0]))
    
'''     import sys, time
    sys.setrecursionlimit(100000)
    n = 100
    while n <= 8000:
        a = list(range(n))
        t = time.time()
        find(a)
        print(n, time.time() - t)
        n *= 2 '''
