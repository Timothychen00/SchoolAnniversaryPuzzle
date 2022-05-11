from flask import Flask,request,abort
import os,random,re,pymongo
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FollowEvent,UnfollowEvent,ButtonsTemplate,MessageTemplateAction,TemplateSendMessage,MessageAction,QuickReply,QuickReplyButton
from debug_tool import message_event_debug

load_dotenv()
client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.linebot
collection=db.user

app=Flask(__name__)

line_bot_api = LineBotApi(os.environ['access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

image_src={
    "Q1-1":'https://i.imgur.com/ZF19eoH.png',
    "Q1-2":"https://i.imgur.com/yrSwadt.png",
    "Q2-1":"https://i.imgur.com/pQwv6er.jpg",
    "Q2-2":"https://i.imgur.com/W0A2uTx.jpg",
    "Q4":"https://i.imgur.com/zIfoBCv.png"
}

@app.route('/')
def home():
    return '1'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

"""
畢業多年後，你收到一封來自母校的邀請函。
打開一看，成功就要一百歲啦！為了慶祝建校百年，成功舉辦了夏日花火祭典，邀請校友們參加。想起那時在學校跟朋友一起幹的蠢事，我想和當年的那群好朋友一起參加，相當年阿，
我們可是號稱「成功七賤客」！但由於疫情緣故，不能太多人一起回到學校，所以我決定找到七賤客中，跟我最要好的朋友，一起去參加。
"""

def multi_replace(string,data=[[' ',''],[',',''],['\'',''],['\"','']]):
    for a,b in data:
        string.replace(a,b)
    return string

def reply_packed(token,text,quick_reply):
    if '，' in quick_reply:
        print(quick_reply)
        label=multi_replace(str(quick_reply.split('，')[0]))
        print(1)
    else:
        label=quick_reply
        print(2)
    print(label)
    line_bot_api.reply_message(token,TextSendMessage(text=text,quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=label,text=quick_reply))])))

msg_pack=[
    ["",'開始遊戲'],
    ["登登、你收到一封來自成功高中的信件。","點開查看"],
    ['打開信件之後你發現這是一封來組母校的邀請函','邀請函？'],
    ["對～因為成功就要100歲了！而為了慶祝建校百年，成功舉辦了夏日花火祭典，邀請所有的校友共同參與。","話說，想起當時在學校跟朋友一起幹的蠢事，好像跟當年的那群朋友一起參加阿！"],
    ["對啊記得當時你們還被稱為「成功七賤客」！，欸可是現在好像因為疫情，不能太多人一起回學校","對啊，所以我打算找到當時的七賤客中，跟我最要好的朋友，一起去參加"]
]

# pointer,try_times

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_event_debug(event)
    msg=event.message.text
    token=event.reply_token
    user_id=event.source.user_id

    times=collection.find_one({"type":'user'})
    times=times[user_id]
    if re.match("開始遊戲",msg):
        times[0]=1
    print(msg_pack[times[0]-1][1],msg)
    if re.match(msg_pack[times[0]-1][1],msg):
        reply_packed(token,msg_pack[times[0]][0],msg_pack[times[0]][1])
        collection.update({"type":'user'},{"$set":{str(user_id):[times[0]+1,times[1]]}})
    
@handler.add(FollowEvent)
def handle_follow(event):
    message_event_debug(event)
    result=collection.find_one({"type":'user'})
    print(result)
    user_id=event.source.user_id
    collection.update({"type":"user"},{"$set":{str(user_id):[0,0]}})

    button_template_message =ButtonsTemplate(thumbnail_image_url="https://i.imgur.com/64N29wq.png",
        title='來玩場遊戲吧～', 
        text='準備一下吧',
        image_size="cover",
        actions=[MessageTemplateAction(label='開始遊戲', text='開始遊戲'),]
    )
    line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text="歡迎追蹤～～～～～～～"),
        TextSendMessage(text="準備好了嗎，請點擊  “開始遊戲”"),
        TemplateSendMessage(alt_text="err",template=button_template_message)]
    )
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    user_id=event.source.user_id
    collection.update({"type":"user"},{"$unset":{str(user_id):""}})
    
    
if __name__=='__main__':
    app.run(debug=True,port=8080)