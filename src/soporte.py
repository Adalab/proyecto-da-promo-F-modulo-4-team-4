#%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#en soporte encotramos las funciones desglosados

#%% 
def leer_csv(fichero):
    df = pd.read_csv(fichero, index_col = 0)
    return df
#%%
def exploracion_csv(dataframe):
    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())
    print("Los valores que tenemos para las columnas numéricas son: ")
    dataframe_numericas = dataframe.select_dtypes(exclude='O')
    try:
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas categóricas son: ")
        display(dataframe_categoricas.describe(include = "O").T)
    except:
        print('No hay columnas categóricas')
    try:
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas numéricas son: ")
        display(dataframe_numericas.describe().T)
    except:
        print('No hay columnas numéricas')


#%%
def eliminacion_duplicados(dataframe):
    dataframe.drop_duplicates(inplace = True)
    return dataframe

#%%
def eliminar_columas(dataframe, columna):
    dataframe.drop(columna, axis=1, inplace=True)
    return dataframe

#%%    
def redondeo(dataframe, columna):
    dataframe[columna]= dataframe[columna].round(0)
    return dataframe

#%% 
def cambiar_datos(dataframe, columna, diccionario):
    dataframe[columna] = dataframe[columna].replace(diccionario)
    return dataframe

#%% 
def cambiar_undefined(dataframe, columna):
    dataframe[columna] = dataframe[columna].fillna("Undefined")
    return dataframe

#%% 
def fecha(dataframe, columna):
    dataframe[columna].str.replace('00:00:00', '')
    dataframe[columna] = pd.to_datetime(dataframe[columna], errors='coerce')
    return dataframe
#había fechas que no existen (30/02) y lo hemos transformado a nulos (NaT)


#%% 

