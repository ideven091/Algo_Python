class Arrays:
    def isSorted(self,arr):
        temp = arr[0]
        for i in range(1,len(arr)):
            if temp > arr[i]:
                return False
            temp = arr[i]
        return True

    

if __name__ == "__main__":
    a = Arrays()
    arr = [1,2,3,4,6,5]
    print(a.isSorted(arr))
