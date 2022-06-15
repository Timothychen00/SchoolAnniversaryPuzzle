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
    def __init__(self,msg):
        self.length=1
        self.head=Node(id=0,msg=msg)
        self.tail=self.head

    def append(self,msg,quick_reply,sender):
        self.tail.next=Node(id=self.length,msg=msg,quick_reply=quick_reply,sender=sender)
        self.length+=1
        self.tail=self.tail.next
        self.tail.next=None

    def find_one(self,key,value):
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
        self.next=None#connection point不一定只有一個 可能會有很多個
        self.quick_reply=quick_reply
        self.sender=sender
        self.degree=None

    def info(self):
        print('-'*20)
        print('id:',self.id)
        print('self:',self)
        print('msg:',self.msg)
        print('quick_reply',self.quick_reply)
        print('query:',self.query)
        print('next:',self.next)
        
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
        
# class DB():
#     def __init__(self):
#         client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#         db = self.client.linebot
#         collection=self.db.user
#         document=self.collection.find_one({'type':'user'})
        
    # def get_userdata

        
__linkedlist=LinkedList('hh')

__linkedlist.append('哈哈1','hh','智能助理')
__linkedlist.append('哈哈2','hh','智能助理')


__linkedlist.info()
# 
    
    
__linkedlist.find_one('query',None).info()

print(type(__linkedlist))









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



__user=User('Uf7f4867b3a62ac1bf05a26c54ddd3b2e')
__user.info()