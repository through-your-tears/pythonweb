import cgi
import html
import psycopg2


form = cgi.FieldStorage()
name = form.getvalue('field-name')
name = html.escape(name)
sec_name = form.getvalue('field-sec-name')
sec_name = html.escape(sec_name)
kurs = int(form.getvalue('field-kurs'))
fakultet = form.getvalue('field-fac')
fakultet = html.escape(fakultet)

conn = psycopg2.connect(
    dbname='python_web',
    user='user',
    password='password',
    host='localhost'
)
with conn.cursor() as cursor:
    conn.autocommit = True
    values = [(name, sec_name, kurs, fakultet)]
    insert = sql.SQL('INSERT INTO form (name, sec_name, kurs, fac) VALUES {}').format(sql.SQL(',').join(map(
        sql.Literal), values))
    cursor.execute(insert)
conn.close()


