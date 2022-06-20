import os,random,re,pymongo
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
    def __init__(self,name=None,id=0,msg=None,quick_reply=None,sender=None,query=None):
        self.length=1
        self.name=name
        self.color=None
        self.head=Node(id=id,msg=msg,branch=self.name,quick_reply=quick_reply,sender=sender,query=None)
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
        queue=[]
        queue.append(self.head)
        # if self.head.__dict__[key]==value:
        #     return self.head
        while queue:
            pointer=queue[-1]
            if pointer.__dict__[key]==value:
                return pointer
            queue.pop()
            queue.extend(pointer.next)
        return None

    def info(self):
        print('self',self)
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
    def __init__(self,id=0,msg=None,quick_reply=None,query=None,sender=None,next=None,branch=None):
        self.id=id
        self.msg=msg
        self.quick_reply=quick_reply
        self.query=query#請求的內容
        self.next=None#connection point不一定只有一個 可能會有很多個
        self.sender=sender
        self.isVisit={}#userid
        self.branch=branch#這個點所在的主要分支

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

    def check(self,msg):
        if not (self.query) or re.search(self.query,msg):
            #send message
            return self
        return None

# class AndGate():
#     def __init__(self,*lists):
#         self.children=lists
#         self.next=None
#         for i in self.children:
#             if i.tail.isVisit:
#                 pass

#branch1
# (self,name=None,id=0,msg=None,quick_reply=None,sender=None,query=None):
__linkedlist=LinkedList('main',0,'叮咚!你收到一封來自母校的邀請函(附圖)','邀請函？是關於什麼的？','智能助理','開始遊戲')
__linkedlist.append('哈哈2','hh','智能助理')
__linkedlist.info()

#branch2
__linkedlist2=LinkedList('pp','branch2')
__linkedlist2.append('陳澤榮好欸','確實','智能助理')


branches={'main':__linkedlist,'branch2':__linkedlist2}#用於存放不同的分支

class User():
    client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.linebot
    collection=db.user

    def __init__(self,userId,event):
        self.user=self.collection.find_one({'type':'user'})[userId]
        self.userId=userId
        self.name=self.user[0][0]
        self.branch=self.user[1][0]
        self.position=self.user[1][1]
        self.current_point=None
        self.event=event

    def info(self):
        print('-'*20)
        print('obj:',self)
        print('name',self.name)
        print('userId',self.userId)
        print('branch',self.branch)
        print('position',self.position)

    def load(self):
        print('\n'*15)
        self.current_point=branches[self.branch].find_one(self.position)
        return self.current_point
    
    def walk(self):
        next=self.current_point.next[0]
        if not (next.query) or re.search(next.query,self.event.message.text):
            self.current_point=next
            return next
        return None
    
    
    def reply(self):
        pass

__linkedlist.head.next[0].connect(__linkedlist2.head)
print('\n'*10)
__linkedlist2.info()
print('\n'*10)
__linkedlist.info()
print('\n'*10)
# __linkedlist.find_one(2).info()
print(__linkedlist.find_one(0))