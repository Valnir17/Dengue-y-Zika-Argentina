### Importo la librería Pandas

import pandas as pd

### Cargo los archivos csv

df20182 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2018 - 2.csv")
df2018 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2018.csv")
df2019 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2019.csv")
df2020 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2020.csv")
df2021 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2021.csv")
df2022 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2022.csv")
df2023 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2023.csv")
df2024 = pd.read_csv(r"TP/Dengue-y-Zika-Argentina/Dengue, Zika 2024.csv")

### Primero tengo que convertir los id_depto y prov_id en string para poder modificarlos por zfill
### para que sea todo consistente

### Hago String a todos los id_depto y prov_id de 2018

df2018['id_depto'] = df2018['id_depto'].values.astype(str)
df2018["prov_id"] = df2018["prov_id"].map(str)

### Aplico el zfill

df2018['id_depto'] = df2018['id_depto'].str.zfill(5)
df2018["prov_id"] = df2018 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2018-2

df20182["id_depto"] = df20182["id_depto"].astype(str)
df20182["prov_id"] = df20182["prov_id"].astype(str)

### Aplico el zfill

df20182['id_depto'] = df20182['id_depto'].str.zfill(3)
df20182['prov_id'] = df20182['prov_id'].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2019


df2019["id_depto"] = df2019["id_depto"].astype(str)
df2019["prov_id"] = df2019["prov_id"].astype(str)

### Aplico el zfill

df2019['id_depto'] = df2019['id_depto'].str.zfill(5)
df2019["prov_id"] = df2019 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2020

df2020["id_depto"] = df2020["id_depto"].astype(str)
df2020["prov_id"] = df2020["prov_id"].astype(str)

### Aplico el zfill

df2020["id_depto"] = df2020 ["id_depto"].str.zfill(5)
df2020["prov_id"] = df2020 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2021

df2021["id_depto"] = df2021["id_depto"].astype(str)
df2021["prov_id"] = df2021["prov_id"].astype(str)

### Aplico el zfill

df2021["id_depto"] = df2021 ["id_depto"].str.zfill(5)
df2021["prov_id"] = df2021 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2022

df2022["id_depto"] = df2022["id_depto"].astype(str)
df2022["prov_id"] = df2022["prov_id"].astype(str)

### Aplico el zfill

df2022["id_depto"] = df2022 ["id_depto"].str.zfill(3)
df2022["prov_id"] = df2022 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2023

df2023["id_depto"] = df2023["id_depto"].astype(str)
df2023["prov_id"] = df2023["prov_id"].astype(str)

### Aplico el zfill

df2023["id_depto"] = df2023 ["id_depto"].str.zfill(5)
df2023["prov_id"] = df2023 ["prov_id"].str.zfill(2)

### Hago String a todos los id_depto y prov_id de 2024

df2024["id_depto"] = df2024["id_depto"].astype(str)
df2024["prov_id"] = df2024["prov_id"].astype(str)

### Aplico el zfill

df2024["id_depto"] = df2024 ["id_depto"].str.zfill(3)
df2024["prov_id"] = df2024 ["prov_id"].str.zfill(2)

### Concateno todos los dataframes en uno.

TablaCompleta = pd.concat([df20182, df2018, df2019, df2020, df2021, df2022, df2023, df2024])

# Encuentro dónde tiene una longitud de 3 caracteres
idcorto = TablaCompleta['id_depto'].str.len() == 3

# Junto los prov_id con el id_depto en las id_depto donde tiene una longitud de 3 caracteres
TablaCompleta.loc[idcorto, 'id_depto'] =  TablaCompleta.loc[idcorto, 'prov_id'] + TablaCompleta.loc[idcorto, 'id_depto']


###Ya tengo estandarizado el formato y unificados los TablaCompleta. Ahora lo siguiente sería el control de calidad.

info = TablaCompleta.info()
print(info)

### Elimino los elementos nulos

TablaCompleta.dropna(inplace=True)

info = TablaCompleta.info()
print(info)

### TablaCompleta.to_csv("TP/Dengue-y-Zika-Argentina/TablaCompleta.csv", index=False)       ### Esto sería casi lo último (tendría que hacer antes los otros df)   
