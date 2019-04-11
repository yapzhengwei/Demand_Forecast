def normalization(df, method='full_standardization', offset=0, numeric_cols=None, window=0, key_col=None):
    
    import pandas as pd
    import numpy as np
    
    if method == 'full_standardization':
        fulldf = df.copy(deep=True)
        fulldf[numeric_cols] = (fulldf[numeric_cols] - np.mean(fulldf[numeric_cols])) / np.std(fulldf[numeric_cols])
        return fulldf
            
    if method == 'long_term_average':
        fulldf = df.copy(deep=True) 
        fulldf[numeric_cols] = fulldf.groupby(key_col)[numeric_cols].apply(lambda x: x/x.rolling(window=window, min_periods=1).mean().shift(offset))
        return fulldf

    if method == 'standardization':
        fulldf = df.copy(deep=True) 
        fulldf[numeric_cols] = fulldf.groupby(key_col)[numeric_cols].apply(lambda x: (x-x.rolling(window=window, min_periods=1).mean().shift(offset))/x.rolling(window=window, min_periods=1).std().shift(offset))
        return fulldf