---

**将数据库的评论分析后展示排名**
---
入口函数：main.py

包说明：

DataBase：连接数据库

dealWords：处理评论

resource：存放一些停用词或字体等文件

savePictrue：存放制作的词云信息

logs：存放日志

utils：工具

---
**技术栈**
---

python(python3.7 x64)：有一定的python基础，https://www.runoob.com/python/python-tutorial.html

imageio：从本地文件中读取图片和写入图片，也可以从网络上读取图片写入本地文件中，https://blog.csdn.net/weixin_36279318/article/details/77446605

jieba：用于分词，https://blog.csdn.net/qq_34337272/article/details/79554772

wordcloud：制作词云的库，可以看https://zhuanlan.zhihu.com/p/28477688

matplotlib：用于绘制图形，很好用的一个包就是内容有点多，推荐直接看官方文档https://matplotlib.org/

---
**包的层次结构**
---

make_word_cloud ---- DataBase ---- DB.py
                  
                  ---- dealWords ---- makeWorldCloud.py
                                
                                 ---- getData.py
                  
                  ---- resource ---- simsun.ttf
                  
                                ---- stop_words.txt
                   
                  ---- logs ---- DB_log.log
                            
                  ---- utils ---- logUtil.py
                  
                             ----  readFile.py
                            
                  ---- savePicture ---- 
                  
                  ---- main.py
                  
                  ----README.md
       
---
**依赖包**
---

jieba： 用于分词

wordcloud：用于制作词云

matplotlib：绘图使用