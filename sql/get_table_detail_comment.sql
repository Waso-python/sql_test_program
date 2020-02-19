select
    komment_table.kt_date,
    ispolnitel.isp_fio,
    status_zakaz.name,
    komment_table.kt_komment,
    ispolnitel1.isp_fio
from komment_table
   inner join status_zakaz on (komment_table.kt_status = status_zakaz.cod)
   inner join ispolnitel on (komment_table.kt_isp = ispolnitel.cod_isp)
   inner join ispolnitel ispolnitel1 on (komment_table.kt_new_isp = ispolnitel1.cod_isp)
where komment_table.kt_codz = {}
