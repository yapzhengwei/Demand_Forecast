def normalization(df, method='full_standardization',offset = 0,numeric_cols=None,window=0,key_col=None):
    
    import pandas as pd
    import numpy as np
    
    if method == 'full_standardization':
        fulldf = df.copy(deep=True)
        for col in numeric_cols:
            fulldf[col] = (fulldf[col]-np.mean(fulldf[col]))/np.std(fulldf[col])
        return fulldf
            
    if method == 'long_term_average':
        fulldf = None 
        for key in df[key_col].unique():
            key_df=df.loc[df[key_col] == key,numeric_cols]
            mean_df = key_df.rolling(window=window,min_periods=1).mean().shift(offset)
            norm_df = key_df/mean_df
            df1 = pd.concat([df[df[key_col] == key].drop(columns=numeric_cols),norm_df],axis=1,sort=False)
            fulldf = df1 if fulldf is None else fulldf.append(df1,sort=False,ignore_index=True)
        return fulldf

    
    if method == 'standardization':
        fulldf = None 
        for key in df[key_col].unique():
            key_df=df.loc[df[key_col] == key,numeric_cols]
            mean_df = key_df.rolling(window=window,min_periods=1).mean().shift(offset)
            std_df =  key_df[numeric_cols].rolling(window=window,min_periods=1).std().shift(offset)
            norm_df = (key_df-mean_df)/std_df
            df1 = pd.concat([df[df[key_col] == key].drop(columns=numeric_cols),norm_df],axis=1,sort=False)
            fulldf = df1 if fulldf is None else fulldf.append(df1,sort=False,ignore_index=True)
        return fulldf