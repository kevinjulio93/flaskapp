import os
import MySQLdb

from ConfigParser import SafeConfigParser

env = SafeConfigParser(os.environ)
env.read('env')

db = MySQLdb.connect(host="localhost", user="root", passwd='252601993')
db_name = str(env.get('PRODUCTION', 'database_name'))

c = db.cursor()
c.execute('create database if not exists ' + db_name)
print 'Database created: ' + db_name
db.close()