from heapq import __all__
import sys
from heapq import *


filei = open(sys.argv[1],"r")
#filei = open("/home/nathan/testApp4.txt","r" )

freqdict = dict()
def freqcount(file):
    totalcount = 0.0
    # @type file file
    stringList = file.readlines()
    iterstring = iter(stringList)
    # @type iter itersting
    for string in stringList:
        string = iterstring.next()
        for char in string:
            current = freqdict.get(char,0)
            freqdict[char] = current + 1
            totalcount += 1
    for k,v in freqdict.iteritems():
        v /= totalcount
        freqdict[k] = v
def treebuild(dict):
    list = []
    nodel = None
    noder = None
    # @type dict dict
    for k,v in dict.iteritems():
        list.append((v,k,nodel,noder))
    print list
    heap = []
    for item in list:
        heappush(heap,item)
    print heap
    heap.sort()
    while ( heap[0][0] != 1.0) :
        tempList = []
        count =0
        for item in heap:

         #   if heap. >= 2:
         #       tuple2= item[count+1]
         #   if tuple1[0] == tuple2[0]:
         #       tempList.append((v1+v2,k1.join(k2),tuple1,tuple2))
         #   if tuple1[0] > tuple2[0]: #smaller value to the Right
         #       tempList.append((v1+v2,k1.join(k2),tuple2,tuple1))
         #   if tuple1[0] < tuple2[0]:#smaller value to the Right
         #      tempList.append((v1+v2,k1.join(k2),tuple1,tuple2))
            #print tuple1
         #   heap = tempList
         #   heap.sort()
         #   print heap
         #   count+=1
def main():
    freqcount(filei)
    print freqdict
    treebuild(freqdict)

main()