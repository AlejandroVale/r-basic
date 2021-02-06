USERNAME = 'TEXMODA_JOBS'
PASSWORD = 'Texmoda1.'

from pyrfc import Connection
conn = Connection(ashost='172.16.100.146', sysnr='00',
                  #saprouter='190.60.219.67',
                  client='402', user=USERNAME, passwd=PASSWORD)
#conn.call('zmm_ws_get_material_movements', REQUTEXT=u'Hello SAP!')

#result = conn.call('ZMM_WS_GET_MATERIAL_MOVEMENTS', I_FECHA_INICIAL = '20200401',  I_FECHA_FINAL = '20200401')

options = [{ 'TEXT': "FCURR = 'USD'"}]
#pp = PrettyPrinter(indent=4)
ROWS_AT_A_TIME = 0
rowskips = 0

result = conn.call('RFC_READ_TABLE', \

QUERY_TABLE = 'TCURR', \
ROWSKIPS = rowskips, ROWCOUNT = ROWS_AT_A_TIME)


print(result['DATA'])