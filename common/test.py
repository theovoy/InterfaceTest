import functools
import logging
import time


class Demo:
    def logger(level):
        def decorator(func):
            def wrapper(*args,**kwargs):
                logging.info(level+':'+'开始报数')
                print(level+':'+'开始报数')
                func(*args,**kwargs)
            return wrapper
        return decorator
    def cal_runtime(func):
        def cal(*args, **kwargs):
            local_time = time.time()
            print(local_time)
            func(*args, **kwargs)
            t = time.time() - local_time
            print(time.time())
            print(t)
        return cal
    @cal_runtime
    def merge(self, nums1, m, nums2, n):  # 合并有序数组
        i = len(nums1) - 1
        p1, p2 = m - n - 1, n - 1
        while (p2 >= 0):
            if p1 < 0 or nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
                i -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
                i -= 1
        print(nums1)
    @cal_runtime
    def removeDuplicates(self, nums):  # 删除重复元素
        i = j = 1
        n = len(nums)
        while j < n:
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        print(nums, i)
        return i

    def rep(self, str1, str2):
        i = 0
        len1 = len(str1)
        len2 = len(str2)
        j = i + len2 - 1
        while i < (len1 - len2 + 1):
            if str1[i:j] == str2:
                str1 = str1[:i] + str1[j + 1:]
            else:
                i += 1
            # str1=str1.replace(str2,'')
        return str1
    def quickSort(self,list):
        if len(list)<2:
           return list
        mid = list[0]
        left = [i for i in list[1:] if i <= mid]
        right = [i for i in list[1:] if i > mid]
        return self.quickSort(left) + [mid] + self.quickSort(right)

    def bubbleSort(self,list):
        for i in range(1,len(list)):
            for j in range(0,len(list)-i):
                if list[j]>list[j+1]:
                    list[j],list[j+1]=list[j+1],list[j]
        return list
    def contStr(self,str1):
        dic={}
        for i in range(len(str1)):
            if str1[i] not in dic:
                dic[str1[i]]=1
            else:
                dic[str1[i]]+=1
        strr=''
        for key in dic:

            strr=strr+key+str(dic[key])

        print(strr)




    @cal_runtime
    def strhandle(self, str):
        s = str[:0] + str[3:]
        return s
    @logger('warning')
    def p(self,n):
        for i in range(1,n):
            print(i)


if __name__ == "__main__":
    demo = Demo()
    #demo.p(8)
    #demo.merge([1,2,4,6,7,0,0,0],8,[4,5,6],3)
    #demo.removeDuplicates([1,1,2,4,6,7])
    # print(demo.rep('abababcabcd','ab'))
    #print(demo.strhandle('abdka'))
    #print(demo.bubbleSort([1,2,4,64,4,3,23,1]))
    list=[1,3,8,4,1,1,2,3,9,4,1]
    #list.sort()
    #sum=0
    #for i in range(0,len(list)):
    #    sum=sum+list[i]
    #print(sum)
    #demo.contStr('qjkwqjehqhhhhqw')
    str='-'
    str1=str.join('abcdfg')
    print(str1)
    li=iter(list)
    print(next(li))
    print(next(li))

