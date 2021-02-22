from pyhive import hive
conn = hive.Connection(host='10.28.3.43', port=10000).cursor()
conn.execute('select * from cdm.cdm_mid_today_actual limit 10;')
for result in conn.fetchall():
    print(result)