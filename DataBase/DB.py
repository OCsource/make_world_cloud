from make_world_cloud.utils import logUtil
import pymysql

logger = logUtil.getLogger(0)

class operateDB:
    def __init__(self):
        self.__dbName = 'qunar'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'

    # 查询景点
    # 参数：城市编号
    # 返回：成功景点编号以及景点名称的二维元组，失败false
    def searchScenery(self, city_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT scenery_number,scenery_name FROM scenery_table WHERE city_number = '%s';" % (city_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error(city_number + ":景点查找失败")
            return False
        finally:
            db.close()

    # 查找景点评论
    # 参数：景点编号
    # 返回：成功评论的一个二维元组，失败false
    def sceneryComment(self,scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT comment FROM comment_table WHERE scenery_number = '%s';" % (scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error("评论查找失败")
            return False
        finally:
            db.close()

    # 插入景点标签
    # 参数：景点编号，景点对应的标签列表
    def insertLabel(self,scenery_number,words):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        for word in words:
            sql = "INSERT INTO scenery_words(scenery_number,word) VALUES('%s', '%s');" % (scenery_number, word)
            try:
                cs.execute(sql)
                db.commit()
            except:
                db.rollback()
                logger.error(scenery_number + ":景点的"+ word +"插入失败")
        db.close()

    # 查找标签
    # 参数：景点编号
    # 返回：成功标签的一个二维元组，失败false
    def searchLabel(self,scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        # 记得改回来scenery_words
        sql = "SELECT word FROM newWords WHERE scenery_number = '%s';" % (scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            db.commit()
            return result
        except:
            db.rollback()
            logger.error(scenery_number + ":景点的标签查找失败")
            return False
        finally:
            db.close()