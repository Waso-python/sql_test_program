import datetime, fdb, json, csv
from app.models import User, db
from flask_login import current_user
from config import Config

dsn = Config.KSDB
con = fdb.connect(dsn, user='sysdba', password='masterkey', charset='UTF8')


def get_table1(user, first_date, last_date, status):
    first_date=first_date
    last_date= last_date
    name = user
    status = status
    #db.session.query(User).filter(User.username == name).all()
    if status:
        if current_user.user_group == 1:
            SQL_QUERY = "select zakaz.cod_zakaz, zakaz.date_zakaz, device_type.type_name, " \
                        "ispolnitel.isp_fio, zakaz.device_name, zakaz.client_name, zakaz.client_name, " \
                        "zakaz.client_telefon, zakaz.opisanie_zakaz, zakaz.defects, zakaz.price," \
                        " zakaz.zakaz_status, status_zakaz.name, zakaz.data_pay from zakaz " \
                        "inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp)" \
                        " inner join device_type on (zakaz.tip_device = device_type.cod_type) " \
                        "inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod)" \
                        " where  (     (zakaz.date_zakaz between '{0}' and '{1}') " \
                        "and status_zakaz.name like '{2}') " \
                        "order by zakaz.cod_zakaz desc ".format(first_date, last_date,status)
        else:
            SQL_QUERY = "select zakaz.cod_zakaz, zakaz.date_zakaz, device_type.type_name, " \
                        "ispolnitel.isp_fio, zakaz.device_name, zakaz.client_name, zakaz.client_name," \
                        " zakaz.client_telefon, zakaz.opisanie_zakaz, zakaz.defects, zakaz.price," \
                        " zakaz.zakaz_status, status_zakaz.name, zakaz.data_pay from zakaz " \
                        "inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp) " \
                        "inner join device_type on (zakaz.tip_device = device_type.cod_type) " \
                        "inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod) " \
                        "where  (     (zakaz.date_zakaz between '{0}' and '{1}') " \
                        "and ispolnitel.isp_fio = '{2}' and zakaz.zakaz_status not in (4,5,6) " \
                        "and status_zakaz.name like '{3}' ) " \
                        "order by zakaz.cod_zakaz desc ".format(first_date,last_date,name,status)
    else:
        if current_user.user_group == 1:
            SQL_QUERY = "select zakaz.cod_zakaz, zakaz.date_zakaz, device_type.type_name, " \
                        "ispolnitel.isp_fio, zakaz.device_name, zakaz.client_name, zakaz.client_name, " \
                        "zakaz.client_telefon, zakaz.opisanie_zakaz, zakaz.defects, zakaz.price, zakaz.zakaz_status, status_zakaz.name, zakaz.data_pay " \
                        "from zakaz inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp) " \
                        "inner join device_type on (zakaz.tip_device = device_type.cod_type) " \
                        "inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod) " \
                        "where  (     (zakaz.date_zakaz between '{0}' and '{1}') ) " \
                        "order by zakaz.cod_zakaz desc ".format(
                first_date, last_date)
        else:
            SQL_QUERY = "select zakaz.cod_zakaz, zakaz.date_zakaz, device_type.type_name," \
                        " ispolnitel.isp_fio, zakaz.device_name, zakaz.client_name, zakaz.client_name, " \
                        "zakaz.client_telefon, zakaz.opisanie_zakaz, zakaz.defects, zakaz.price, " \
                        "zakaz.zakaz_status, status_zakaz.name, zakaz.data_pay " \
                        "from zakaz inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp) " \
                        "inner join device_type on (zakaz.tip_device = device_type.cod_type) " \
                        "inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod) " \
                        "where  (     (zakaz.date_zakaz between '{0}' and '{1}') and ispolnitel.isp_fio = '{2}' " \
                        "and zakaz.zakaz_status not in (4,5,6) ) order by zakaz.cod_zakaz desc ".format(first_date, last_date, name)

    # Соединение

    # Объект курсора
    cur = con.cursor()

    # Выполняем запрос

    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    #for s in result:
     #   print(s)
    return result


def get_table_detail(codz):
    # Соединение
    SQL_QUERY = "select \n    zakaz.cod_zakaz,\n    zakaz.date_zakaz,\n    device_type.type_name,\n    ispolnitel.isp_fio,\n    zakaz.device_name,\n    zakaz.client_name,\n    zakaz.client_name,\n    zakaz.client_telefon,\n    zakaz.opisanie_zakaz,\n    zakaz.defects,\n    zakaz.price,\n    zakaz.zakaz_status,\n    status_zakaz.name,\n    zakaz.data_pay,  zakaz.COMMENT_ISP_ZAKAZ  from zakaz   inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp)\n   inner join device_type on (zakaz.tip_device = device_type.cod_type)\n   inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod)\nwhere \n  zakaz.cod_zakaz = {}".format(codz)
    # Объект курсора
    cur = con.cursor()
    con.begin()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchone()
    print(result)

    return result

def get_all_status():
    SQL_QUERY = "select status_zakaz.cod, status_zakaz.name from status_zakaz"
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    t = {}
    for s in result:
        t.update({s[0]:s[1]})
    ls = []
    for key,value in t.items():
        ls.append([key, value])


    return ls


def get_table_detail_comment(codz):
    with open("sql\get_table_detail_comment.sql") as file:
        SQL_QUERY = file.read()
    cur = con.cursor()
    # Выполняем запрос
    SQL_QUERY = SQL_QUERY.format(codz)
    cur.execute(SQL_QUERY)
    result = cur.fetchall()

    return result




def get_all_user():
    SQL_QUERY = "select cod_isp, isp_fio from ispolnitel where active = 1"
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    t = {}
    for s in result:
        t.update({s[0]: s[1]})
    ls = []
    for key, value in t.items():
        ls.append([key, value])

    return ls


def get_order_status(user, first_date, last_date):
    first_date = first_date
    last_date = last_date
    name = user
    # db.session.query(User).filter(User.username == name).all()

    if current_user.user_group == 1:
        SQL_QUERY = "select distinct(status_zakaz.name) from status_zakaz inner join zakaz on (status_zakaz.cod = zakaz.zakaz_status) where  (     (zakaz.date_zakaz between '{0}' and '{1}') ) order by zakaz.cod_zakaz desc ".format(first_date, last_date)
    else:
        SQL_QUERY = "select distinct(status_zakaz.name) from status_zakaz inner join zakaz on (status_zakaz.cod = zakaz.zakaz_status) inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp) where  (     (zakaz.date_zakaz between '{0}' and '{1}') and ispolnitel.isp_fio = '{2}' and zakaz.zakaz_status not in (4,5,6) ) order by zakaz.cod_zakaz desc ".format(first_date, last_date, name)

    # Соединение

    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()

    return result

def get_table_detail_info(tel):
    # Соединение
    SQL_QUERY = "select \n    zakaz.cod_zakaz,\n    zakaz.date_zakaz,\n    device_type.type_name,\n    ispolnitel.isp_fio,\n    zakaz.device_name,\n    zakaz.client_name,\n    zakaz.client_name,\n    zakaz.client_telefon,\n    zakaz.opisanie_zakaz,\n    zakaz.defects,\n    zakaz.price,\n    zakaz.zakaz_status,\n    status_zakaz.name,\n    zakaz.data_pay,\n zakaz.COMMENT_ISP_ZAKAZ\n from zakaz\n   inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp)\n   inner join device_type on (zakaz.tip_device = device_type.cod_type)\n   inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod)\nwhere \n  zakaz.CLIENT_TELEFON like {}".format(tel)
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()

    return result


def get_table_detail_material(codz):
    # Соединение
    SQL_QUERY = "select zakaz_rashod.zr_cod, zakaz_rashod.zrvid, zakaz_rashod.zr_zcod, zakaz_rashod.zr_name,  zr_vid.zrv_name,  zakaz_rashod.zr_price from zakaz_rashod   inner join zr_vid on (zakaz_rashod.zrvid = zr_vid.cod) where \n  zakaz_rashod.zr_zcod = {}".format(codz)
    # Объект курсора

    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    sum = 0
    for s in result:
        sum+=s[5]

    return result


def get_table_detail_material_sum(codz):
    # Соединение
    SQL_QUERY = "select zakaz_rashod.zr_cod, zakaz_rashod.zrvid, zakaz_rashod.zr_zcod, zakaz_rashod.zr_name,  zr_vid.zrv_name,  zakaz_rashod.zr_price from zakaz_rashod   inner join zr_vid on (zakaz_rashod.zrvid = zr_vid.cod) where \n  zakaz_rashod.zr_zcod = {}".format(codz)
    # Объект курсора

    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    sum = 0
    for s in result:
        sum+=s[5]

    return sum


def get_table_detail_sms(codz):
    # Соединение
    SQL_QUERY = "select sms_call.sc_cod, sms_call.sc_zakaz, sms_call.sc_date, sms_call.sc_vid, sms_call.sc_result, sms_call.sc_complete, scvid.scv_name, sms_call.time_now from sms_call inner join scvid on (sms_call.sc_vid = scvid.cod) where \n  sms_call.sc_zakaz = {}".format(codz)
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()

    return result

def get_tip_device():
    # Соединение
    SQL_QUERY = "select device_type.cod_type,device_type.type_name from device_type"
    # Объект курсора
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()

    return result


def change_comment(s):
    print(s[0])
    SQL_QUERY = f"update zakaz set zakaz.comment_isp_zakaz = '{s[0]}' where zakaz.cod_zakaz = {s[1]}"
    cur = con.cursor()
    cur.execute(SQL_QUERY)
    con.commit()

    return print(SQL_QUERY)


def add_comment(s):
    f = open(r'sql\add_comment.sql', 'r')
    SQL_QUERY = f.read().format(s[4],str(s[0]),s[3],s[2],s[1])
    SQL_QUERY2 = "update zakaz set ispolnitel = {}, zakaz_status = {} where cod_zakaz = {}".format(s[1],s[2],s[4])
    cur2 = con.cursor()
    cur = con.cursor()
    cur.execute(SQL_QUERY)
    con.commit()
    cur2.execute(SQL_QUERY2)
    con.commit()

    return print(SQL_QUERY)


def add_price(s):
    SQL_QUERY2 = "update zakaz set price = {} where cod_zakaz = {}".format(s[0], s[1])
    cur2 = con.cursor()

    cur2.execute(SQL_QUERY2)

    con.commit()

def add_zakaz(zakaz):
    return zakaz




