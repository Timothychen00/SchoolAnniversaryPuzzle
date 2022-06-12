class LinkedList():
    def __init__(self,msg):
        self.length=1
        self.head=Node(id=0,msg=msg)
        self.tail=self.head

    def append(self,msg,quick_reply,sender):
        self.tail.next=Node(id=self.length,msg=msg,quick_reply=quick_reply,sender=sender)
        self.length+=1
        self.tail=self.tail.next
        self.tail.next=None

    def find(self,id):
        pointer=self.head
        for _ in range(id):
            pointer=pointer.next
        return pointer

    def info(self):
        print('head',self.head)
        print('tail',self.tail)
        print('length',self.length)
        print('tree')
        pointer=self.head
        for _ in range(self.length):
            pointer.info()
            pointer=pointer.next

class Node():
    def __init__(self,id=0,msg=None,quick_reply=None,query=None,next=None,sender=None):
        self.id=id
        self.msg=msg
        self.quick_reply=quick_reply
        self.query=query
        self.next=None
        self.quick_reply=quick_reply
        self.sender=sender
    def info(self):
        print('-'*20)
        print('id:',self.id)
        print('self:',self)
        print('msg:',self.msg)
        print('quick_reply',self.quick_reply)
        print('query:',self.query)
        print('next:',self.next)
        
        
        
        
__linkedlist=LinkedList('hh')
__linkedlist.append('哈哈1','hh','智能助理')
__linkedlist.append('哈哈2','hh','智能助理')

# __linkedlist.find(0).info()
# __linkedlist.info()

# __linkedlist.show_all()
# __linkedlist.head.info()
# __linkedlist.head.next.info()
__linkedlist.head.next.next.info()
# __linkedlist.info()

    