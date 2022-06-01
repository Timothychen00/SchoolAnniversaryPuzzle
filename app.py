from flask import Flask,request,abort
import os,random,re,pymongo
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FollowEvent,UnfollowEvent,ButtonsTemplate,MessageTemplateAction,TemplateSendMessage,MessageAction,QuickReply,QuickReplyButton,Sender
from debug_tool import message_event_debug
from data import *

load_dotenv()
client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASSWORD']+"@cluster0.wvaw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.linebot
collection=db.user

app=Flask(__name__)

line_bot_api = LineBotApi(os.environ['access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

sender={x:Sender(name=x,icon_url=image_src[x]) for x in ['智能助理','昱誠','黃準','旁白']}

def send(token,type,data,sender_name,reply=None):
    print('==send==')
    msg=[]
    type_length=len(type)
    type_range=range(type_length)
    label=reply
    if reply:
        if len(reply)>6:
            if '，' in reply:
                label=reply.split('，')[0]

    print(sender_name)
    if not isinstance(sender_name, list):
        sender_name=[str(sender_name) for i in range(type_length)]

    for i in type_range:
        print('i:',i)
        if type[i]=='text':
            if i==type_length-1 and reply:
                print(1)
                msg.append(TextSendMessage(text=data[i],sender=sender[sender_name[i]],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=label,text=reply))])))
            else:
                print(2)
                msg.append(TextSendMessage(text=data[i],sender=sender[sender_name[i]]))

        elif type[i]=='img':
            print("-------------\n",data[i])
            if i==type_length-1 and reply:
                print(3)
                msg.append(ImageSendMessage(original_content_url=image_src[data[i]],sender=sender[sender_name[i]],preview_image_url=preview_src[data[i]],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=label,text=reply))])))
            else:
                print(4)
                msg.append(ImageSendMessage(original_content_url=image_src[data[i]],sender=sender[sender_name[i]],preview_image_url=preview_src[data[i]]))
        print(token,len(msg))
        print(token,msg)
    line_bot_api.reply_message(token,msg)

@handler.add(MessageEvent,message=TextMessage)
def msg_process(event):
    print('-'*20)
    token=event.reply_token
    msg=event.message.text
    user_id=event.source.user_id

    times=collection.find_one({"type":'user'})
    try_times=times[user_id][1]
    times=times[user_id][0]
    
    if times==0 and re.match("開始遊戲",msg):
        times+=1

    if times in question_pack:
        not (question_pack[times] in msg)
        if not (question_pack[times] in msg):
            if try_times<6:
                send(token,['text'],['好像不是欸'],msg_pack[times][0],None)
            else:
                send(token,['text'],['你是不是太笨了，需要幫助嗎'],msg_pack[times][0],question_pack[times])
            try_times+=1
        else:
            print('correct')
            try_times=0
            times+=1
    print('times:',times)
    if times not in question_pack:
        #正常情況
        print('required:',msg_pack[times-1][2],'|msg:',msg)
        if msg_pack[times-1][2]:
            print(re.match(msg_pack[times-1][2],msg))
        if re.match(msg_pack[times-1][2],msg):
            send(token,msg_type[times],msg_pack[times][1],msg_pack[times][0],msg_pack[times][2])
            times+=1

    collection.update({"type":'user'},{"$set":{str(user_id):[times,try_times]}})

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
        TextSendMessage(text="歡迎追蹤～～～～～～～\n須知:這是一場解謎，主要的劇情會通過和機器人互動的過程進行，然後故事中會穿插謎題。然後如果有出現提示回覆的內容，請點擊，不要亂回（可能會造成劇情無法繼續）！！！！！！！\n如果在遊玩的過程中發生問題，可以嘗試將機器人封鎖，再解除封鎖來嘗試觸發",sender=sender['智能助理']),
        TextSendMessage(text="閱讀以上內容後，準備好，就請點擊  “開始遊戲” 享受這一場解密吧～～～",sender=sender['智能助理']),
        TemplateSendMessage(alt_text="err",template=button_template_message,sender=sender['智能助理'])]
    )
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    user_id=event.source.user_id
    collection.update({"type":"user"},{"$unset":{str(user_id):""}})

@app.route('/')
def home():
    return '1'

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