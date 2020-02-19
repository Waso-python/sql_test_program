select
    zakaz.cod_zakaz,
    zakaz.date_zakaz,
    ispolnitel.cod_isp,
    ispolnitel.isp_fio,
    zakaz.client_telefon,
    zakaz.client_name,
    device_type.cod_type,
    device_type.type_name,
    zakaz.device_name,
    zakaz.device_sn,
    status_zakaz.cod,
    status_zakaz.name,
    zakaz.price,
    zakaz.price_parts,
    zakaz.data_pay
from zakaz
   inner join status_zakaz on (zakaz.zakaz_status = status_zakaz.cod)
   inner join device_type on (zakaz.tip_device = device_type.cod_type)
   inner join ispolnitel on (zakaz.ispolnitel = ispolnitel.cod_isp)
order by zakaz.cod_zakaz