
import pandas as pd

class EncodedFeature():
    
    def __init__(self):
        pass
    
    def encode_onehot(self, origin_df, onehot_encode_columnName , dropOriginal=False):
        """
        This function generate one_hot_encoded columns
        Example
        -------
        >>> from KETIPreDataTransformation.featureExtension.encodedFeatureExtension import EncodedFeature
        >>> EF = EncodedFeature()
        >>> df_generated = EF.encode_onehot(original_df, columnNameList)

        original_df: pandas.DataFrame
            original Input DataFrame
        columnNameList: list of str
            List of columns to one-hot-encode
        dropOriginal : bool, default = False
            When set to True, it drops original column features (leaves only one-hot-encoded features) 
        Returns:
            extended_df (pandas.DataFrame), New dataFrmae with one-hot-encoded features
        """ 
        extended_df = origin_df.copy()
        dummies = pd.get_dummies(extended_df[onehot_encode_columnName].astype(str), prefix = onehot_encode_columnName)
        
        if dropOriginal==True:
            extended_df = extended_df.drop(columns=onehot_encode_columnName)    
        extended_df = pd.concat([extended_df, dummies], axis=1)
        return extended_df
  