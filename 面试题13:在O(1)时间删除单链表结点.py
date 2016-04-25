#coding:utf-8

# 面试题13:在O(1)时间删除单链表节点

# 初始化单链表
class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0
    def initlist(self, data):
        self.head = Node(data[0])
        p = self.head
        if data[0] == 'd':
            self.target = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
            if i == 'd':
                self.target = p
        return self.head, self.target # 生成完单链表返回头结点指针,目标删除指针

data = ['a','b','c','d','e']
l = LinkList()
listHead, deleteNode = l.initlist(data) # 头结点指针

def DeleteNode(listHead, deleteNode):
    if listHead == deleteNode: # 要删除节点是头结点
        listHead = listHead.next
    elif deleteNode.next == None: # 要删除节点为尾节点
        preNode = listHead
        while True:
            if preNode.next == deleteNode:
                preNode.next = None
            else:
                preNode = preNode.next
    else: # 要删除节点是中间节点
        deleteNode.data = deleteNode.next.data
        deleteNode.next = deleteNode.next.next
