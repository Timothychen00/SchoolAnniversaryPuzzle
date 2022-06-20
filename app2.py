from linked_list import *
from flask import Flask,request,abort
import os,random,re,pymongo
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FollowEvent,UnfollowEvent,ButtonsTemplate,MessageTemplateAction,TemplateSendMessage,MessageAction,QuickReply,QuickReplyButton,Sender
from debug_tool import message_event_debug

load_dotenv()
client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.linebot
collection=db.user

app=Flask(__name__)

line_bot_api = LineBotApi(os.environ['access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

image_src={
    "Q1-1":'https://i.imgur.com/CzIXYh6.png',
    "Q1-2":"https://i.imgur.com/qo0NMJR.png",
    "Q2-1":"https://i.imgur.com/cHEDvaZ.jpg",
    "Q2-2":"https://i.imgur.com/cKmaenR.jpg",
    "Q3":"https://i.imgur.com/Yhcf1k5.jpg",
    "Q4":"https://i.imgur.com/l4laPWH.png",
    'Q5-1-1':"https://i.imgur.com/l8gNHGU.png",
    'Q5-1-2':"https://i.imgur.com/HTwiphg.png",
    'Q5-2':"https://i.imgur.com/pIO57Bs.jpg",
    'Invitation':"https://i.imgur.com/Vt71aT4.jpg",
    '智能助理':"https://i.imgur.com/0U4kk7Q.jpg",
    '昱誠':'https://i.imgur.com/NnV48gW.jpg',
    '旁白':"https://i.imgur.com/pRIKYtn.jpg",
    '黃準':'https://i.imgur.com/avM3NFk.jpg',
    'Iteration':"https://i.imgur.com/eLtnjrO.jpg",
}

preview_src=image_src
sender={x:Sender(name=x,icon_url=image_src[x]) for x in ['智能助理','昱誠','黃準','旁白']}



@handler.add(MessageEvent,message=TextMessage)
def msg_process(event):
    userId=event.source.user_id
    msg=event.message.text
    
    __user=User(userId)
    __user.info()
    current_point=__user.load()
    temp=current_point.next[0].check(msg)
    if temp:
        current_point=temp
    
    current_point.info()

    
    
    

@handler.add(FollowEvent)
def handle_follow(event):
    message_event_debug(event)
    token=event.reply_token
    result=collection.find_one({"type":'user'})
    print(result)
    user_id=event.source.user_id
    
    profile=line_bot_api.get_profile(user_id)
    name=profile.display_name
    id=profile.user_id
    collection.update({"type":"user"},{"$set":{str(user_id):[[name],['main',0,0]]}})

    button_template_message =ButtonsTemplate(thumbnail_image_url="https://i.imgur.com/64N29wq.png",
        title='來玩場遊戲吧～', 
        text='準備一下吧',
        image_size="cover",
        actions=[MessageTemplateAction(label='開始遊戲', text='開始遊戲'),]
    )
    line_bot_api.reply_message(
        token,[
        TextSendMessage(text="歡迎追蹤～～～～～～～\n須知:這是一場解謎，主要的劇情會通過和機器人互動的過程進行，然後故事中會穿插謎題。然後如果有出現提示回覆的內容，請點擊，不要亂回（可能會造成劇情無法繼續）！！！！！！！\n如果在遊玩的過程中發生問題，可以嘗試將機器人封鎖，再解除封鎖來嘗試觸發",sender=sender['智能助理']),
        TextSendMessage(text="閱讀以上內容後，準備好，就請點擊  “開始遊戲” 享受這一場解密吧～～～",sender=sender['智能助理']),
        TemplateSendMessage(alt_text="err",template=button_template_message,sender=sender['智能助理'])]
    )
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    user_id=event.source.user_id
    collection.update({"type":"user"},{"$unset":{str(user_id):""}})

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

if __name__=='__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')