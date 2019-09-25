from imageio import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
from make_world_cloud.DataBase import DB

# 制作词云的类
class makeCW:
    # 构造函数
    # 参数：是否启用中文分词（true or false），图片编号一般为相应的景点编号，指定的词语（不会被分割的词语，数组），文本值（要分析的文本内容）
    def __init__(self,cn,numPic,newWords,text):
        self.isCN = cn # 默认启用中文分词
        self.text = text
        self.count = Counter()
        self.number = numPic
        self.pic_path = "./resource/backPicture.jpg"      # 设置背景图片路径
        self.font_path = './resource/simkai.ttf'     # 为matplotlib设置中文字体路径，没有这个字体的话中文会乱码
        self.stopwords_path = './resource/stop_words.txt'      # 停用词词表
        self.save_img_path_1 = "./savePicture/" + str(numPic) + "default.png"      # 保存的图片1(只按照背景图片形状)
        self.save_img_path_2 = "./savePicture/" + str(numPic) + "ByImg.png"       # 保存的图片2(颜色按照背景图片颜色布局生成)
        self.operate = DB.operateDB()

        self.my_words_list = newWords#['东方威尼斯水城']     # 在结巴的词库中添加新词

        self.back_coloring = imread(self.pic_path)     # 设置背景图片

        # 设置词云属性
        if self.isCN:
            self.wc = WordCloud(font_path=self.font_path,  # 设置字体
                           background_color="white",  # 背景颜色
                           max_words=2000,  # 词云显示的最大词数
                           mask=self.back_coloring,  # 设置背景图片
                           max_font_size=100,  # 字体最大值
                           random_state=42,
                           width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                           )
        else:
            self.wc = WordCloud()

    # 添加自己的词库分词
    # 参数：要自定义的词语数组
    def add_word(self,list):
        for items in list:
            jieba.add_word(items)

    # 结巴分词
    # 参数：要分词的文本内容（非文本地址）
    # 返回：分好词之后的文本列表以空格分开
    def jiebaCutText(self,text):
        myWordList = []
        segList = jieba.cut(text)
        buff = []
        buff.append(self.my_words_list[0])
        with open(self.stopwords_path, 'r', encoding='utf8') as f:
            for row in f:
                el = row[:-1]
                buff.append(el)
        stopWords = buff
        for word in segList:
            if word not in stopWords and len(word) > 1 and not word.isdigit() and not word.count('.') == 1:
                myWordList.append(word)
        self.countWords(myWordList)
        return ' '.join(myWordList)

    # 统计词频
    # 参数：分词的列表
    def countWords(self,myWordList):
        for w in myWordList:
            if(len(w) > 1 and w != '\r\n'):
                self.count[w] += 1

    # 词云区
    # 原始词云
    def makeOriginalCW(self):
        plt.figure()
        plt.imshow(self.wc)
        plt.axis("off")
        # 显示
        # plt.show()
        # 将图片存到本地
        self.wc.to_file(self.save_img_path_1)

    # 添加了图片的词云
    def makePictureCW(self):
        image_colors = ImageColorGenerator(self.back_coloring) # 从背景图片生成颜色值
        plt.imshow(self.wc.recolor(color_func=image_colors))
        plt.axis("off")
        plt.figure()
        plt.imshow(self.back_coloring)
        plt.axis("off")
        # 显示
        # plt.show()
        # 将图片存到本地
        self.wc.to_file(self.save_img_path_2)

    # 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
    def main(self):
        myText = self.jiebaCutText(self.text)
        tempList = []
        for (k,v) in self.count.most_common(10):
            tempList.append(k)
        self.operate.insertLabel(self.number, tempList)

        self.wc.generate(myText)
        # self.makeOriginalCW()   # 原始词云
        self.makePictureCW()  # 图片词云

    def __str__(self):
        return 'mcw -- ing'