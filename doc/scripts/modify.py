#!/usr/bin/python
#-\*-coding: utf-8-\*-
import MySQLdb
sql='/*--user=checktest;--password=123456;--host=127.0.0.1;--execute=1;--enable-remote-backup;--port=3306;*/\
    inception_magic_start;\
    use checktest;\
    INSERT INTO v9_wap(siteid,sitename,logo,domain,setting) VALUES ("21","aa","bb","cc","1100");\
    delete from   v9_wap where siteid=11;\
    update  v9_wap set sitename="haha" where siteid=10;\
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
