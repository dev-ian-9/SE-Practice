from enum import Enum

class runtime(Enum):
    DEBUG = 0
    LIVE = 1

# Runtime Level
runtimeLevel = runtime.DEBUG  # 0 -- DEBUG; 1 -- LIVE
#runtimeLevel = runtime.LIVE  # 0 -- DEBUG; 1 -- LIVE

try:
    # Python packages
    import os
    import pandas as pd
    import json
    import numpy as np
    import re
    import warnings

    # Local packages
    from constants import *
    from logger import logging, exit_log, CURRENTDATETIME
    from funcTimer import funcTimer
    
except Exception as e:
    if runtimeLevel.DEBUG:
        raise
    else:
        logging.info(f'Import failed: {e}')
        input('Press [Enter] key to exit.')


def fill_postal_code(postalCodeDf : pd.DataFrame, df : pd.DataFrame) -> pd.DataFrame():
    for i, dfRow in df.iterrows():
        # print(dfRow[MCD_PREFECTURE])
        # print(dfRow[MCD_CITY])
        # tempDf = postalCodeDf.loc[postalCodeDf[JP_PREFECTURE].str.lower() == str(dfRow[MCD_PREFECTURE]).lower()]
        # tempDf = postalCodeDf.loc[postalCodeDf[JP_PREFECTURE].str.contains(str(dfRow[MCD_PREFECTURE]).lower().strip())]
        
        targetPrefecture = str(dfRow[MCD_PREFECTURE]).lower().strip()
        filtered_df = postalCodeDf[postalCodeDf[JP_PREFECTURE].str.lower().str.contains(targetPrefecture)]
        # print(filtered_df)
        # print("^^ BY PREFECTURE ^^")
        
        targetCity = str(dfRow[MCD_CITY]).lower().strip()
        filtered_df = postalCodeDf[postalCodeDf[JP_CITY].str.lower().str.contains(targetCity)]
        # print(filtered_df)
        # print("^^ BY CITY ^^")
        
        targetTown = str(dfRow[MCD_TOWN]).lower().strip()
        filtered_df = postalCodeDf[postalCodeDf[JP_TOWN].str.lower().str.contains(targetTown)]
        #print(filtered_df)
        #print("^^ BY TOWN ^^")
        
        if i % 100 == 0:
            print(f"Processed Data: {i}")
            
        # Skip if filter is empty
        if filtered_df.empty:
            df.at[i, MCD_POSTALCODE] = "DATA NOT FOUND"
            continue
        
        # Skip if filter more than 1 row
        elif filtered_df.shape[0] > 1:
            df.at[i, MCD_POSTALCODE] = "COULD NOT RESOLVE"
            continue
    
        else:
            data = filtered_df.iloc[0]
            postalCodeData = data[JP_POSTALCODE]
            df.at[i, MCD_POSTALCODE] = postalCodeData
            # print(df.at[i, MCD_POSTALCODE])
            
    return df


def add_ku_string(df : pd.DataFrame) -> pd.DataFrame():
    for i, row in df.iterrows():
        
        if "-" in row[MCD_CITY]:
            continue
        
        df.at[i, MCD_CITY] = row[MCD_CITY] + "-ku"
        
    return df
    
    
def get_town(df : pd.DataFrame) -> pd.DataFrame():
    for i, row in df.iterrows():
        
        addr1 = str.split(row[MCD_ADDRESS], ",")[0]
        addr2 = str.split(row[MCD_ADDRESS], ",")[1]
        
        if "cho" in addr1:
            town = addr1    
            
        elif "cho" in addr2:
            town = addr2  
            
        else:
            town = addr1
    
        # Remove all "cho"
        town = town.strip().split("cho")[0]
        
        # Remove all spaces
        town = town.replace(" ", "")
        
        # Remove all numbers and dashes
        res = re.sub(r'[\d-]+', '', town).strip()
        
        df.at[i, MCD_TOWN] = res
        
    return df

    
def main():
    logging.info("Getting Postal Code - Dataframe..")
    postalCodeDf = pd.read_excel(MAIN_EXCEL, JPCODELIST_SHEET)
    postalCodeDf = postalCodeDf[[
        JP_POSTALCODE,
        JP_AREA,
        JP_PREFECTURE,
        JP_CITY,
        JP_TOWN
    ]]
    logging.info("Postal Code - Dataframe DONE!")
    
    logging.info("Getting McDonalds - Dataframe..")
    mcdonaldsDf = pd.read_excel(MAIN_EXCEL, MCDONALDS_SHEET)
    mcdonaldsDf = mcdonaldsDf[[
        MCD_POSTALCODE,
        MCD_ADDRESS,
        MCD_PREFECTURE,
        MCD_CITY
    ]]
    logging.info("McDonalds Data - Dataframe DONE!")
    
    
    resDf = pd.DataFrame()
    # resDf = add_ku_string(mcdonaldsDf)
    resDf = get_town(mcdonaldsDf)
    resDf = fill_postal_code(postalCodeDf, resDf)
    
    # resDf[MCD_POSTALCODE] = resDf[MCD_POSTALCODE].astype('int32')
    print(resDf)
    resDf.to_excel("GetPostalCode\Test-112.xlsx")
    
    
if __name__ == '__main__':
    warnings.simplefilter(action='ignore', category=FutureWarning)
    main()
    logging.info('Script executed successfully!')