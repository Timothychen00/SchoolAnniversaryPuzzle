import os,random,re,pymongo
from numpy import packbits
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FollowEvent,UnfollowEvent,ButtonsTemplate,MessageTemplateAction,TemplateSendMessage,MessageAction,QuickReply,QuickReplyButton,Sender
from flask import Flask,request,abort

load_dotenv()
client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.linebot
collection=db.user
class LinkedList():
    def __init__(self,msg,name=None,id=0):
        self.length=1
        self.name=name
        self.head=Node(id=id,msg=msg,branch=self.name)
        self.tail=self.head

    def append(self,msg,quick_reply,sender):
        if not self.tail.next:
            self.tail.next=[]
        self.tail.next.append(Node(id=self.length,msg=msg,quick_reply=quick_reply,sender=sender,branch=self.name))
        self.length+=1
        self.tail=self.tail.next[0]
        self.tail.next=[]

    def insert_after(self,id,msg,quick_reply,sender):
        node=self.find_one(id)
        next=node.next
        node.next=Node(id=self.length,msg=msg,quick_reply=quick_reply,sender=sender,branch=self.name)
        node.next.next=next
        self.length+=1

    def find_one(self,value,key='id'):
        pointer=self.head
        length=self.length
        for _ in range(length):
            if value==pointer.__dict__[key]:
                return pointer
            pointer=pointer.next
        return None

    def info(self):
        print('head:',self.head)
        print('tail:',self.tail)
        print('length:',self.length)
        print('tree:')
        queue=[]
        # print(self.head)
        queue.append(self.head)
        while queue:
            print('current_queue:',queue)
            pointer=queue[-1]
            pointer.info()
            queue.pop()
            queue.extend(pointer.next)
        
    def switch(self):
        pass


class Node():
    def __init__(self,id=0,msg=None,quick_reply=None,query=None,next=None,sender=None,branch=None):
        self.id=id
        self.msg=msg
        self.quick_reply=quick_reply
        self.query=query#請求的內容
        self.next=None#connection point不一定只有一個 可能會有很多個
        self.quick_reply=quick_reply
        self.sender=sender
        self.degree=None
        self.isVisit={}#userid
        self.branch=branch

    def info(self):
        print('-'*20)
        print('id:',self.branch,self.id)
        print('self:',self)
        print('msg:',self.msg)
        print('quick_reply',self.quick_reply)
        print('query:',self.query)
        print('next:',self.next)
        
    def connect(self,*nodes):
        print('nextnext:::',self.next)
        if self.next:
            self.next.extend(nodes)
        else:
            self.next=[]
            self.next.extend(nodes)
        print(self.next)
    
    def tag(self,user_id):
        self.isVisit.add(user_id)
        
    def walk(self,id):
        if self.next:
            if len(self.next)==1:
                self=self.next[0]
            
            

# class AndGate():
#     def __init__(self,*lists):
#         self.children=lists
#         self.next=None
#         for i in self.children:
#             if i.tail.isVisit:
#                 pass

        
__linkedlist=LinkedList('hh','\033[94mbranch1\033[0m')

__linkedlist.append('哈哈1','hh','智能助理')
__linkedlist.append('哈哈2','hh','智能助理')


__linkedlist.info()
# 
print(__linkedlist.head)
    
# __linkedlist.find_one('query',None).info()

# print(type(__linkedlist))
# __linkedlist.insert_after(1,'哈哈哈3','hh','智能助理')

# __linkedlist.find_one(3).connect(4,Node('哈哈哈4'),'hh','智能助理')

branches=[__linkedlist]
class User():
    client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.linebot
    collection=db.user

    def __init__(self,userId):
        self.user=self.collection.find_one({'type':'user'})[userId]
        self.userId=userId
        self.name=self.user[0][0]
        self.branch=self.user[1][0]
        self.position=self.user[1][1]

    def info(self):
        print('-'*20)
        print('obj:',self)
        print('name',self.name)
        print('userId',self.userId)
        print('branch',self.branch)
        print('position',self.position)

    def load(self):
        branches[self.branch].find_one(self.position).tag(self.userId)
        return branches[self.branch].find_one(self.position)



__linkedlist2=LinkedList('pp','\033[92mbranch2\033[0m')
__linkedlist2.append('pp1','hh','智能助理')
__linkedlist2.append('陳澤榮好帥','確實','智能助理')
__linkedlist2.append('陳澤榮好帥2','確實','智能助理')
__linkedlist2.append('陳澤榮好帥3','確實','智能助理')

__linkedlist.head.next[0].connect(__linkedlist2.head)
print('\n'*10)
__linkedlist2.info()
print('\n'*10)
__linkedlist.info()



# __linkedlist.find(0).info()
# __linkedlist.info()

# __linkedlist.show_all()
# __linkedlist.head.info()
# __linkedlist.head.next.info()
# __linkedlist.head.next.next.info()
# __linkedlist.info()


# __linkedlist.info()
# __linkedlist.find(1).info()
# __linkedlist.find(id,1).info()



