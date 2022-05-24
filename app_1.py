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
sender=[Sender(name='FUCK you',icon_url='https://i.imgur.com/mFEklhs.png'),Sender(name='Hollyshit',icon_url='https://i.imgur.com/qqBEAUP.png')]

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

def multi_replace(string,data=[[' ',''],[',',''],['\'',''],['\"','']]):
    for a,b in data:
        string.replace(a,b)
    return string

def reply_packed(token,text,quick_reply,der=0):
    if quick_reply:#if exists
        if '，' in quick_reply:
            print(quick_reply)
            label=multi_replace(str(quick_reply.split('，')[0]))
            print(1)
        else:
            label=quick_reply
            print(2)
            print(label)
        print(type(text))
    
    if type(text) is list:#一連串
        data=[]
        for i in text:
            data.append(TextSendMessage(text=i))
        line_bot_api.reply_message(token,data)
    elif not quick_reply:
        line_bot_api.reply_message(token,TextSendMessage(text=text,sender=sender[der]))
    else:
        line_bot_api.reply_message(token,TextSendMessage(text=text,sender=sender[der],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=label,text=quick_reply))])))

msg_pack=[
    ["",'開始遊戲'],
    ["登登、你收到一封來自成功高中的信件。","點開查看"],
    ['打開信件之後是一封來組母校的邀請函','邀請函？'],
    ["對～因為成功就要100歲了！而為了慶祝建校百年，成功舉辦了夏日花火祭典，邀請所有的校友共同參與。","話說，想起當時在學校跟朋友一起幹的蠢事，好像跟當年的那群朋友一起參加阿！"],
    ["對啊記得當時你們還被稱為「成功七賤客」！，欸可是現在好像因為疫情，不能太多人一起回學校","對啊，所以我打算找到當時的七賤客中，跟我最要好的朋友（他是一個警察），一起去參加"],
    ['欸？可是你要怎麼知道誰才是警察呢？','嗯。。。助理，幫我搜索一下那天我們出去玩的照片。'],
    ['已搜索到照片（為了方便，我把大家編了一個號，從左到右分別是1-7）','嗯？好像有這回事'],
    ['試著想看看吧','在我的印象中，他好像是警察，這位好像是...嗯....律師？另外這兩位是老師吧！如果我沒記錯的話，還有兩個人跟我一樣是工程師」（自言自語）'],
    [[
        '喔喔對了，這是我憑印象會想起的線索，希望對妳有幫助。三條線索：',
        '1.最左邊和最右邊他們職業相同，但如果需要維護治安他們幫不上忙',
        '2.最矮的那個和最高的那個都不是工程師',
        '3.左邊數來第二個和右邊數來第二個的職業相同'
        '想到的話告訴我答案吧（記得答案是一位的數字）'],''],
    ['',''],
    ['（校慶當天）','哇，校園變了真多啊，不知道當年我們一起上課的教室現在在哪裡？'],
    ['',''],
    ['',''],
    ['(抵達了教室)','欸？這個座位表蠻特別的'],
    ['(停下來看了看)','仔細查看'],
    ['在看什麼，趕快進來啊啦','嗨～早啊好久不見'],
    ['你怎麼又遲到了！畢業十年怎麼還是跟當初一樣','我我我......好喘'],
    ['怎麼這麼喘，該不會睡過頭吧','沒有啦，～太久沒有回來學校，找教室花了億點時間。'],
    ['好啦，我其實有幫你買好飲料（在你原本的座位底下，但是你應該是不記得了啦）','哇～貼心欸，大熱天有飲料～'],
    ['但是不能這麼輕易讓你喝到，所以我簡單設計了一個小謎題，考考你吧。（我順便去上個廁所）','又來，好啦，我試試看啦'],
    [
    ['好啦找找你之前的座位吧，對了這是線索',
     'A已經知道那個座位的'
     "以下是兩個人的對話內容：",
     "A:我不知道這個座位",
     "B:我早就知道你不知道，但是我也不知道\n"
     "A:我現在知道這個座位了\n"
     "B:我也知道了"
    ],'嗯.....我思考一下'],
    ['' ''],
    ['（就在這時，門外傳來腳步聲）','昱誠，你也來了？'],
    ['（各種敘舊，此處省略10分鐘的對話）','話說，妳對生物的興趣果然還是跟當時一樣啊'],
    ['那當然，我可是當年生物社教學欸','也對啦，刮鬍泡中誕生的教學。那你現在的工作還習慣嗎'],
    ['嗯..雖然跟生物比較無關，但律師可以幫別人辯護，然後據理力爭，還蠻有趣的，而且還會碰到一些名字很特別的對手事務所',"是喔"],
    ['啊，給你一張之前拿到的另一個律師事務所的名片，它的商標和名字都還蠻特別的，是一種動物，考考你，還記不記得這是什麼動物？',"欸？我想想"],
    ['','']
]

image_src={
    "Q1-1":'https://i.imgur.com/ZF19eoH.png',
    "Q1-2":"https://i.imgur.com/yrSwadt.png",
    "Q2-1":"https://i.imgur.com/pQwv6er.jpg",
    "Q2-2":"https://i.imgur.com/W0A2uTx.jpg",
    "Q3":"https://i.imgur.com/3qQ7nsh.jpg",
    "Q4":"https://i.imgur.com/vJAqbQW.jpg",
    'invitation':"https://i.imgur.com/UoeKg0E.jpg"
}

question_pack=[(9,"3"),(12,'111'),(21,'A1')]
# pointer,try_times sender[0]

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_event_debug(event)
    msg=event.message.text
    token=event.reply_token
    user_id=event.source.user_id

    times=collection.find_one({"type":'user'})
    try_times=times[user_id][1]
    times=times[user_id][0]
   
    try:
        print(times)
        print(times,msg_pack[times-1][1],msg,re.match(msg_pack[times-1][1],msg))
    except:
        pass
    
    if re.match("開始遊戲",msg) and times==0:
        times=1
   
    if times==1 and re.match(msg_pack[times-1][1],msg):
        reply_packed(token,msg_pack[times][0],msg_pack[times][1],1)
        times+=1
    if times==2 and re.match(msg_pack[times-1][1],msg):
        line_bot_api.reply_message(token,[TextSendMessage(text=msg_pack[times][0],sender=sender[0]),ImageSendMessage(original_content_url=image_src['invitation'],preview_image_url=image_src['invitation'],sender=sender[0],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=msg_pack[times][1],text=msg_pack[times][1]))]))])
        times+=1
    if times<7 and re.match(msg_pack[times-1][1],msg):
        reply_packed(token,msg_pack[times][0],msg_pack[times][1],1)
        times+=1
    elif times==7 and re.match(msg_pack[times-1][1],msg):
        line_bot_api.reply_message(token,[ImageSendMessage(original_content_url=image_src['Q3'],preview_image_url=image_src['Q3'],sender=sender[0]),TextSendMessage(text=msg_pack[times][0],sender=sender[0],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=msg_pack[times][1][:7],text=msg_pack[times][1]))]))])
        times+=1
    elif times<9 and re.match(msg_pack[times-1][1],msg):
        reply_packed(token,msg_pack[times][0],msg_pack[times][1])
        times+=1
        try_times=0
    elif times==question_pack[0][0]:
        print('question')
        if msg!=question_pack[0][1]:
            if try_times<4:
                reply_packed(token,'好像不對喔',None)
            else:
                reply_packed(token,'你好像太笨了，你是不是需要一些提示',question_pack[0][1])
            try_times+=1
        else:
            reply_packed(token,'好像是欸，那需要我幫您把這件事列入您的行程規劃嗎？','當然')
            times+=1
    elif times==10 and re.match(msg_pack[times-1][1],msg):
        reply_packed(token,msg_pack[times][0],msg_pack[times][1])
        times+=1
    elif times==11 and re.match(msg_pack[times-1][1],msg):
        line_bot_api.reply_message(token,[ImageSendMessage(original_content_url=image_src['Q4'],sender=sender[0],preview_image_url=image_src['Q4']),TextSendMessage(text='這是公告欄裡貼著的，上面好像有些線索\n*記得答案是一間教室喔（三位數字）')])
        times+=1
        try_times=0
    elif times==question_pack[1][0]:
        print('question2')
        if msg!=question_pack[1][1]:
            if try_times<4:
                reply_packed(token,'好像不是這間教室欸',None)
            else:
                reply_packed(token,'你好像太笨了，你是不是需要一些提示',question_pack[1][1])
            try_times+=1
        else:
            reply_packed(token,'（經過了二十分鐘，終於找到了那個教室）','（慢慢的走了過去）')
            times+=1
    elif times<13 and re.match(msg_pack[times-1][1],msg):
        print(1)
        reply_packed(token,msg_pack[times][0],msg_pack[times][1])
        times+=1
    elif times==13 and re.match(msg_pack[times-1][1],msg):
        line_bot_api.reply_message(token,[TextSendMessage(text='(終於抵達了教室)',sender=sender[0]),ImageSendMessage(original_content_url=image_src['Q1-1'],sender=sender[0],preview_image_url=image_src['Q1-1'],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=msg_pack[times][1][:7],text=msg_pack[times][1]))]))])
        times+=1
    elif times==14 and re.match(msg_pack[times-1][1],msg):
        reply_packed(token,msg_pack[times][0],msg_pack[times][1])
        times+=1
    elif times==15 and re.match(msg_pack[times-1][1],msg):
        line_bot_api.reply_message(token,[ImageSendMessage(original_content_url=image_src['Q1-2'],sender=sender[0],preview_image_url=image_src['Q1-2'],quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=msg_pack[times][1][:7],text=msg_pack[times][1]))])),TextSendMessage(text='黃準：在看什麼啦，趕快進來吧',quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label=msg_pack[times][1][:7],text=msg_pack[times][1]))]))])
        times+=1
        try_times=0
    elif times==21:
        print('question3')
        if msg!=question_pack[2][1]:
            if try_times<6:
                reply_packed(token,'這個座位好像空空的',None)
            else:
                reply_packed(token,'（還是把每個座位都看一遍好了）',question_pack[2][1])
            try_times+=1
        else:
            reply_packed(token,'找到了飲料','好喝')
            times+=1
    elif times<27 and re.match(msg_pack[times-1][1],msg):
        print(1)
        reply_packed(token,msg_pack[times][0],msg_pack[times][1])
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
        TextSendMessage(text="歡迎追蹤～～～～～～～",sender=sender[1]),
        TextSendMessage(text="準備好了嗎，請點擊  “開始遊戲”",sender=sender[1]),
        TemplateSendMessage(alt_text="err",template=button_template_message,sender=sender[1])]
    )
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    user_id=event.source.user_id
    collection.update({"type":"user"},{"$unset":{str(user_id):""}})
    
if __name__=='__main__':
    app.run(debug=True,port=8080)