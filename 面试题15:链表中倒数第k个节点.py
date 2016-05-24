# coding:utf-8

# 面试题15:链表中倒数第k个节点

class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p

class Linklist(object):
    def __init__(self):
        self.head = 0
    def initlist(self, data):
        self.head = Node(data[0])
        hNode = self.head # 链表头指针
        p = self.head
        for i in data[1: ]:
            node = Node(i)
            p.next = node
            p = p.next
        return hNode
    def printlist(self, hNode):
        p = hNode
        while p.next != 0:
            print p.data
            p = p.next
    def findKthToTail(self, hNode, k): # k表示这是倒数第几个节点
        # 先设置flag1和flag2
        flag1 = flag2 = hNode
        # 让 flag2 向右先移动k-1个位置
        for i in range(k-1):
            flag2 = flag2.next
        while flag2.next != 0:
            flag1 = flag1.next
            flag2 = flag2.next
        print flag1.data

l = Linklist()
hNode = l.initlist(data=[1,2,3,4,5,6,7])
l.findKthToTail(hNode, 3)