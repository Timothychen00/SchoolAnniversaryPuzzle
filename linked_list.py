class LinkedList():
    def __init__(self,msg):
        self.length=1
        self.head=Node(id=0,msg=msg)
        self.tail=self.head
    def append(self,msg):
        self.tail.next=Node(id=self.length,msg=msg)
        self.length+=1
        self.tail=self.tail.next
        self.tail.next=None
    def info(self):
        print('='*20)
        print('length',self.length)
        print('head',self.head)
        print('tail',self.tail)
        print('tail.next',self.tail.next)
    def search(self):
        pass
    def show_all(self):
        pointer=self.head
        for _ in range(self.length):
            pointer.info()
            pointer=pointer.next

class Node():
    def __init__(self,id=0,msg=None,quick_reply=None,query=None,next=None):
        self.id=id
        self.msg=msg
        self.quick_reply=quick_reply
        self.query=query
        self.next=None
    def info(self):
        print('-'*20)
        print('id:',self.id)
        print('self:',self)
        print('msg:',self.msg)
        print('quick_reply',self.quick_reply)
        print('query:',self.query)
        print('next:',self.next)

__linkedlist=LinkedList('hh')
__linkedlist.append('哈哈1')
__linkedlist.append('哈哈2')
__linkedlist.show_all()
# __linkedlist.head.info()
# __linkedlist.head.next.info()
# __linkedlist.head.next.next.info()
# __linkedlist.info()

    