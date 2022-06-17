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

question_pack={
    "main":{11:[("3",'main'),('4','test')],19:'75',24:'111',28:"D5",32:'無尾熊',34:'恐龍'}
    }

# id:[sender,type,data,reply]
msg_pack={
    "main":{
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
        '好吧，至少你願意自己思考','有1位律師，2位老師，1位警察跟包含主人在內的3位工程師',
        '三條線索：\n'
        '1.最左邊和最右邊他們職業不相同，但如果需要維護治安他們幫不上忙\n'
        '2.最矮的那個和最高的那個都不是工程師\n'
        '3.左邊數來第二個和右邊數來第二個的職業相同\n\n（請回答一位數字）'],None],
    11:['智能助理',[],''],
    12:['智能助理',['要我幫你把這件事列入行程嗎?'],'好啊！'],
    13:['旁白',['校慶當天'],'啊，~好懷念的地方啊~這個孔子像居然還在啊!'],
    14:['旁白',['走下司令台旁的樓梯，面前是一個操場'],'...過了這麼久，操場怎麼還是這麼小啊。欸？那個奇妙的裝飾是什麼？'],
    15:['旁白',['你看到了一個寫著100的銅製立牌'],'看來是為了紀念100年校慶才特別製作的吧，畢竟這麼重要的年份確實要好好留下紀錄。等等，這個位置不就是我們七賤客埋時光膠囊的地方嗎？'],
    16:['旁白',['趁著周遭的人都忙於搭建等等校慶要營業的攤位，你將當年的時光膠囊挖了出來，將盒子稍作清洗之後看清了它的全貌(圖)','Q5-1-2'],'這盒蓋上面，居然鑲了一個錶？我們當年到底是怎麼找到這個盒子的？嗯，怎麼打不開啊。'],
    17:['旁白',['你發現盒子被一個鎖給鎖住了，看來只有想出密碼才能解開','Q5-2'],'糟糕，當年埋這盒子的人不是我，我根本不知道密碼啊!欸，錶的旁邊有刻字，這說不定是密碼的線索!'],
    18:['旁白',['嘗試尋找密碼吧（數字）'],None],
    19:['旁白',[],''],
    20:['旁白',['主角解出密碼打開了盒子，盒中裝了七件外貌各異的物品，有些甚至還不完整','Q5-1-1'],'雖然盒子開是開了，但我沒有寫信，也忘記當初為什麼要放一只少一條鞋帶的球鞋啊...'],
    21:['智能助理',['主人，您是不是忘記您回來了原因了?'],'當然記得!我約了，黃準要一起......啊啊啊啊啊!剛剛解密碼解得太入迷，我是不是已經遲到了？'],
    22:['智能助理',['您已經遲到5分鐘了。'],'可....可是，我不知道我們以前一起上課的那個教室在哪裡，助理，幫我找出學校的平面圖。'],
    23:['智能助理',['搜尋到圖片','Q4','(請輸入那間教室)'],None],
    24:['智能助理',[],''],
    25:['智能助理',['要我幫你開導航嗎?'],'都遲到了你還有興致開玩笑啊!'],
    26:['旁白',['在教室外你瞟了一眼那個座位表','Q1-1','Q1-2'],'嗯...這個座位表？好像蠻特殊的？'],
    27:[['旁白','黃準'],['走進教室，你看到一臉不爽的黃準','「你很慢欸！到底在幹嘛，我幫你買了一杯飲料，但你這麼晚來，我把他放在你之前上學時坐的位置，提示在這，想喝就自己找吧」\n\n提示:在A已經知道列數（橫列），B已經知道行數（直行）的前提下，嘗試推出作為的座標代號\n\n以下是他們兩個的對法內容\nA:我不知道這個座位\nB:我早知道你不知道\n但是我也不知道\nA:我現在知道這個座位了\nB:我也知道了\n（請找出你上學時的位置)'],None],
    28:['旁白',[],''],
    29:[['旁白','昱誠'],['就在這時，門口處傳來腳步聲','你也回來了?'],'這個聲音...難道是昱誠?'],
    30:['黃準',['哇!好久不見了!'],'對啊對啊，最近過得如何？是不是幫強尼戴普辯護去啦？'],
    31:['昱誠',['哪有那麼厲害啊!啊，給你們一人一張我律師事務所的名片，它的商標是我們共同的回憶喔。考考你們，還記不記得這是什麼動物？','Q2-1','（動物名稱是中文）'],None],
    32:['昱誠',[],''],
    33:['昱誠',['那這個呢？','Q2-2','（動物名稱是中文）'],None],
    34:['昱誠',[],''],
    35:['昱誠',['哎唷不錯喔，你還記得'],'當然啊，那次我們班遊去動物園，你在無尾熊區待了快半小時，一直說無尾熊有多可愛多可愛，聽到耳朵都快長繭了。'],
    36:[['黃準','昱誠'],['恐龍也很簡單啊，我記得你最喜歡的電影就是侏儸紀系列','真不錯，你們的記憶真不錯'],"未完待續"],
    37:['智能助理',['------------------------------------------\n','謝謝您參與本次的體驗，可以的話幫我填寫以下的遊玩回饋表單，讓我們知道哪裡可以改進，謝謝:\nhttps://reurl.cc/VDWdG6','特別鳴謝:\n林恆睿,林銘陞,胡廷鋒,高偉傑,陳澤榮,游承旻,黃存謙,蒲拓海,BiBi','\n-----------------------\n 順便工商一下，我們的團隊～～～～Iteration~～～～～～～～：\nFB:https://www.facebook.com/IterationStudio2022\n\nIG:https://www.instagram.com/iteration_2022/','Iteration'],None]
    },
    'test':{
        11:['智能助理',[''],''],
        12:['智能助理',['哈，這是第二個結局'],'喔好唷'],
        13:['只能助理',['1'],'2'],
    }
}


msg_type={
    "main":{
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
    12:['text'],
    13:['text'],
    14:['text'],
    15:['text'],
    16:['text','img'],
    17:['text','img'],
    18:['text'],
    19:[],
    20:['text','img'],
    21:['text'],
    22:['text'],
    23:['text','img','text'],
    24:[],
    25:['text'],
    26:['text','img','img'],
    27:['text','text'],
    28:[],
    29:['text','text'],
    30:['text'],
    31:['text','img','text'],
    32:[],
    33:['text','img','text'],
    34:[],
    35:['text'],
    36:['text','text'],
    37:['text','text','text','text','img'],
    },
    'test':{
        12:['text'],
        13:['text']
    }
}
