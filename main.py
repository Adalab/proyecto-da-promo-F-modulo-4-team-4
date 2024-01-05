#%%
import pandas as pd
import os 
import sys
#%%
os.getcwd()
#%%
sys.path.append("../")
#%%
os.getcwd()
#%%
from src import soporte as sp
# %%
df = sp.leer_csv('../finanzas-hotel-bookings.csv')

# %%
sp.exploracion_csv(df)
# %%
sp.eliminacion_duplicados(df)
# %%
lista_columnas_eliminar = ['0', 'company']
sp.eliminar_columas(df, lista_columnas_eliminar)
# %%
lista_columnas_redondear=["lead_time", "stays_in_week_nights", "stays_in_weekend_nights"]
sp.redondeo(df, lista_columnas_redondear)

# %%
dicc_fechas= {"1": "January", "2":"February", "3": "March"}
sp.cambiar_datos(df,'arrival_date_month', dicc_fechas)
# %%
dicc_yes_no = {0: "no", 1: "yes"}
sp.cambiar_datos(df, 'is_repeated_guest', dicc_yes_no)
# %%
lista_columnas_nan = ['hotel',
    'is_canceled',
    'arrival_date_month',
    'meal',
    'country',
    'market_segment',
    'distribution_channel',
    'reserved_room_type',
    'assigned_room_type',
    'customer_type',
    'reservation_status',
    'is_repeated_guest']
sp.cambiar_undefined(df, lista_columnas_nan)
# %%
sp.fecha(df, 'reservation_status_date')
# %%
pd.to_csv('df_final.csv')

# %%
df.to_csv('df_final.csv')
# %%
