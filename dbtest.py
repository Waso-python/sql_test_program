import fdb

con = fdb.connect(dsn='192.168.1.70:c:/db/ks2.fdb', user='sysdba', password='masterkey', charset='UTF8')

def get_table_detail(codz):
    # Соединение
    SQL_QUERY = "select \n    zakaz.cod_zakaz,\n    zakaz.date_zakaz,\n    device_type.type_name,\n    ispolnitel.isp_fio,\n    zakaz.device_name,\n    zakaz.client_name,\n    zakaz.client_name,\n    zakaz.client_telefon,\n    zakaz.opisanie_zakaz,\n    zakaz.defects,\n    zakaz.price,\n    zakaz.zakaz_status,\n    status_zakaz.name,\n    zakaz.data_pay,  zakaz.COMMENT_ISP_ZAKAZ  from zakaz   inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp)\n   inner join device_type on (zakaz.tip_device = device_type.cod_type)\n   inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod)\nwhere \n  zakaz.cod_zakaz = {}".format(codz)
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchone()
    print(result)

    return result