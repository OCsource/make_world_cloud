from make_world_cloud.dealWords import getData
from make_world_cloud.DataBase import DB

operation = DB.operateDB()

def main():
    getData.getDataBaseData('86')               # 制作城市编号为86的景点词云
    # getData.getTextData('../resource/***.txt')  # 制作该txt的词云
    print('转化完成！')

if __name__ == '__main__':
    main()