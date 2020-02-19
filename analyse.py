
import datetime, fdb, json, csv


import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

dsn = 'localhost:c:/db/ks2.fdb'
con = fdb.connect(dsn, user='sysdba', password='masterkey', charset='UTF8')

def db_analysis():
    with open("zakaz_view_lite.sql") as file:
        SQL_QUERY = file.read()
    cur = con.cursor()
    # Выполняем запрос
    cur.execute(SQL_QUERY)
    result = cur.fetchall()
    #print(result)
    with open("список.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Date", "Cod_isp", "Isp_fio", "Client_tel", "Client_name", "Cod_type", "Type_name","Device_name", "Device_sn", "Status_cod", "Status_name", "Price", "Price_parts", "Date_pay"])
        for items in result:
            csv.writer(file).writerow(items)
    return result


def read_csv():
    fixed_df = pd.read_csv('список.csv', sep=',',parse_dates=['Date'],  error_bad_lines=False, encoding = "windows-1251")

    return fixed_df


db_analysis()

df = read_csv()
print(df)



