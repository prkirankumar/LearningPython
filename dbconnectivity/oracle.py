import cx_Oracle

#connection = cx_Oracle.connect("kiran/kiran@localhost/orcl")
print(cx_Oracle.clientversion())

dsn = cx_Oracle.makedsn(
    'localhost', 
    '1521', 
    service_name='orcl'
)
conn = cx_Oracle.connect(
    user='kiran', 
    password='kiarn', 
    dsn=dsn
)
c = conn.cursor()
