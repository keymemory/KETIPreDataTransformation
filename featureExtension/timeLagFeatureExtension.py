#mylist = list(df_features.select_dtypes(include=['object']).columns)
class TimeLagFeature():
    
    def __init__(self):
        pass
    
    def extendTimeLagFeatures(self, origin_df, columnNameList, n_lags, deleteFirstLagDuration= False):
        """
        This function generate time-lags-Features and extend original dataframe
        Example
        -------
        >>> from KETIPreDataTransformation.featureExtension.timeLagFeatureExtension import class TimeLagFeature
        >>> TLF = TimeLagFeature()
        >>> lag = 100
        >>> columnNameList=['value']
        >>> df_generated = TLF.extendTimeLagFeatures(df, columnNameList, lag, deleteFirstLagDuration=True)

        
        original_df: pandas.DataFrame
            original Input DataFrame
        columnNameList: list of str
            List of columns to extend lag features
        n_lags: int
            number of lags to be extend
        deleteFirstLagDuration : bool, default = False
            When set to True, it deletes the NaN row data that was inevitably created to generate lag data.
        Returns:
            extended_df (pandas.DataFrame), New dataFrmae with lag features
            (ex originalFeatureName = "value", n_lags = 2 -> added features: "value_lag1", "value_lag2")
        """ 
        
        extended_df = origin_df.copy()
        for columnName in columnNameList:
            for n in range(0, n_lags):
                lag = n+1
                extended_df[f"{columnName}_lag{lag}"] = extended_df[[columnName]].shift(lag)
        if deleteFirstLagDuration==True:
            extended_df = extended_df.iloc[n_lags:]
            
        return extended_df
