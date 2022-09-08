def find_k(ls, n):
    for i in range(n):
        if(ls[i] < ls[i+1]):
            pass
        else:
            print("value of k:",i)
            return i

def find_sum(l , n, s):
    k = find_k(l , n)
    new_list = []
    new_list = l[k+1:]+ l[0:k+1]
    print(new_list)
    i = 0
    j = n-1
    while i < j:
        if (new_list[i]+ new_list[j]== s):
            print("sum exist")
            return
        elif( new_list[i]+new_list[j] < s):
            i = i + 1
        else:
            j = j - 1
      

if __name__ == '__main__':
    ls = [11,15,16,2,3,5,6,8]
    s = 16
    n = len(ls)
    find_sum(ls,n , s)