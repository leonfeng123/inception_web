#!/usr/bin/python
#-\*-coding: utf-8-\*-
import MySQLdb
sql='/*--user=checktest;--password=123456;--host=127.0.0.1;--execute=1;--port=3306;*/\
    inception_magic_start;\
    use checktest;\
    CREATE TABLE `v9_wap` (\
                    `siteid` int(11) unsigned NOT NULL auto_increment comment"aaa",\
                    `sitename` varchar(50) NOT NULL Default "" comment"aaa",\
                    `logo` varchar(50) NOT NULL Default "" comment"aaa",\
                    `domain` varchar(50) NOT NULL Default "" comment"aaa",\
                    `setting` int(11) NOT NULL Default 0 comment"aaa",\
                    PRIMARY KEY (`siteid`)\
                    ) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT="AAAA";\
    inception_magic_commit;'
try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='',port=6669)
        cur=conn.cursor()
        ret=cur.execute(sql)
        result=cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        print field_names
        for row in result:
                print row[0], "¦",row[1],"¦",row[2],"¦",row[3],"¦",row[4],"¦",
                row[5],"¦",row[6],"¦",row[7],"¦",row[8],"¦",row[9],"¦",row[10]
        cur.close()
        conn.close()
except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
