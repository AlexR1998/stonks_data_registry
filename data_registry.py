import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

input("Press Enter to start")
print("Procesando...")
term_path="C:\Program Files/MetaTrader 5 IC Markets (SC)/terminal64.exe"
from_date=datetime(2021,1,1)
to_date=datetime.now()
#Importar transacciones (financieras)

transc_path="C:/Users/USUARIO/Desktop/Stonks Investment Group/1. Sistema de Gestión Financiera/Cuentas Financieras"
op_path="C:/Users/USUARIO/Desktop/Stonks Investment Group/5. Central de Datos/Operaciones"
tr_path="C:/Users/USUARIO/Desktop/Stonks Investment Group/5. Central de Datos/Transacciones"

OrdERI=pd.read_excel(transc_path+"/Registro de Cuentas.xlsx",sheet_name="Orden ERI")
OrdESF=pd.read_excel(transc_path+"/Registro de Cuentas.xlsx",sheet_name="Orden ESF")
RegERI=pd.read_excel(transc_path+"/Registro de Cuentas.xlsx",sheet_name="Registro ERI")
RegESF=pd.read_excel(transc_path+"/Registro de Cuentas.xlsx",sheet_name="Registro ESF")

#Importar operaciones (trades)

mt5.initialize(term_path)
deals=mt5.history_deals_get(from_date,to_date)
c_trades=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
c_trades['time'] = pd.to_datetime(c_trades['time'], unit='s')

orders=mt5.orders_get()
if orders is None:
    print("No opened orders")
else:
    o_trades=pd.DataFrame(list(orders),columns=orders[0]._asdict().keys())
    o_trades['time_setup'] = pd.to_datetime(o_trades['time_setup'], unit='s')
mt5.shutdown()


#Exportar archivos de datos

OrdERI.to_csv(tr_path+'/AcOrder.txt',sep='\t',index=False)
OrdESF.to_csv(tr_path+'/OrdESF.txt',sep='\t',index=False)
RegERI.to_csv(tr_path+'/RegERI.txt',sep='\t',index=False)
RegESF.to_csv(tr_path+'/RegESF.txt',sep='\t',index=False)
o_trades.to_csv(op_path+'/opened_trades.txt',sep='\t',index=False)
c_trades.to_csv(op_path+'/closed_trades.txt',sep='\t',index=False)

print("Proceso Finalizado")

