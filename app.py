from flask import Flask,request,abort
import os,random
from dotenv import load_dotenv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
)

load_dotenv()
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
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    img=random.choice(list(image_src.values()))
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text))
        ImageSendMessage(original_content_url=img,preview_image_url=img)
    )
if __name__=='__main__':
    app.run(debug=True,port=8080)