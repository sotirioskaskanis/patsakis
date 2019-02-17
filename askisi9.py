
#sinartiseis
def maxSequence(list):
    #dexete mia lista
    #epistrefi thn ipolista me to megisto athrisma kathos kai to athrisma auto
    sum = 0
    size = len(list)
    max = 0
    for i in range(0, size + 1):

        for j in range(size, i - 1, -1):
            print(list[i:j])
            for k in list[i:j]:
                sum = sum + k
            if sum >= max:
                maxList = list[i:j]
                max = sum

            sum = 0

    return max,maxList

#kirios programa

myList=[-2,1,-3,4,-1,2,3,1,-10,3]

max,maxList=maxSequence(myList)
print(max,':',maxList)