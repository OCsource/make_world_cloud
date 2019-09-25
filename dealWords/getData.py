from make_world_cloud.dealWords import makeWorldCloud
from make_world_cloud.utils import readFile
from make_world_cloud.DataBase import DB

# 获取数据库数据并分析
def getDataBaseData(city_number):
    operation = DB.operateDB()
    results = operation.searchScenery(city_number)  # 查找城市86的所有景点
    for result in results:
        scenery_number = result[0]
        scenery_name = result[1]
        com = operation.sceneryComment(scenery_number)    # 查找景点的评论
        text = ''
        for row in com:
            text += row[0].decode('gbk') + '\n'
        if text != '':
            cn, numPic, newWords, pic_path = True, scenery_number, [scenery_name],"./resource/backPicture.jpg"
            cw = makeWorldCloud.makeCW(cn, numPic, newWords, text,pic_path)
            cw.main()
            del cw
            print(scenery_name + " : " + scenery_number + "词云制作成功")
        else:
            print(scenery_name + " : " + scenery_number + "词云制作失败")
        break

# 获取文本数据并分析
def getTextData(path):
    text = readFile.readFile(path)
    cn, numPic, newWords,pic_path = True, 111, ['****'],"./resource/backPicture.jpg"
    if text != '':
        cw = makeWorldCloud.makeCW(cn, numPic, newWords, text,pic_path)
        cw.main()
        print(path + "词云制作成功")
    else:
        print(path + "词云制作失败")