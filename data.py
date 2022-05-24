image_src={
    "Q1-1":'https://i.imgur.com/RpSsKQf.png',
    "Q1-2":"https://i.imgur.com/OG1J0sY.png",
    "Q2-1":"https://i.imgur.com/cHEDvaZ.jpg",
    "Q2-2":"https://i.imgur.com/cKmaenR.jpg",
    "Q3":"https://i.imgur.com/Yhcf1k5.jpg",
    "Q4":"https://i.imgur.com/KMkDkwV.jpg",
    'Invitation':"https://i.imgur.com/Vt71aT4.jpg",
    '智能助理':"https://i.imgur.com/mFEklhs.png",
    '蘇昱誠':'https://i.imgur.com/NnV48gW.jpg',
}
preview_src=image_src

question_pack={11:"3",19:'111',21:'A1'}

# id:[sender,type,data,reply]
msg_pack={
    0:['智能助理',[],'開始遊戲'],
    1:['智能助理',["叮咚!你收到一封來自母校的邀請函(附圖)"],'邀請函？是關於什麼的？'],
    2:['智能助理',['成功100年校慶的邀請函','Invitation'],'100年校慶，...這麼重要的慶典，他會回來嗎...（喃喃自語）'],
    3:['智能助理',['嗯?主人您說什麼?'],'沒什麼，只是想到了當年的某個遺憾。阿，這麼重要的慶典，我一定要結伴回去!'],
    4:['智能助理',['您要找「成功七賤客」，對吧?'],'沒錯!'],
    5:['智能助理',['主人，為了您的健康著想，現在疫情嚴峻，我建議您找一位同行就好。'],'有道理，那我找跟我最要好的朋友吧!（他是一位警察）'],
    6:['智能助理',['欸？可是你要怎麼知道誰才是警察呢？'],'嗯…助理，幫我搜尋那天我們出去玩的照片'],
    7:['智能助理',['已搜索到照片（從左到右分別是編號1-編號7）'],'好勒！讓我來看一看。'],
    8:['智能助理',['Q3','啊哈哈！我知道誰才是警察了！'],'真假？快跟我說'],
    9:['智能助理',['主人，近期的身體檢查顯示，您的智力下降了4%，再不動動腦會變笨喔'],'......那至少給點提示吧'],
    10:['智能助理',[
        '好吧，至少你願意自己思考','有1位律師，2位老師，1位警察跟包含我在內的3位工程師',
        '三條線索：\n'
        '1.最左邊和最右邊他們職業相同，但如果需要維護治安他們幫不上忙\n'
        '2.最矮的那個和最高的那個都不是工程師\n'
        '3.左邊數來第二個和右邊數來第二個的職業相同'],None],
    11:['智能助理',[],''],
    12:['智能助理',['要我幫你把這件事列入行程嗎?'],'好啊！'],
    13:[],
}

msg_type={
    1:['text'],
    2:['text','img'],
    3:['text'],
    4:['text'],
    5:['text'],
    6:['text'],
    7:['text'],
    8:['img','text'],
    9:['text'],
    10:['text','text','text'],
    11:[],
    12:['text']
}
