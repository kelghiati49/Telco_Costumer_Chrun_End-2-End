import pandas as pd 

def preprocess_data(df : pd.DataFrame, target_col : str = "Chrun") -> pd.DataFrame:

    """
    Basic Cleaning for Telco Chruns :
    -Trim Column names
    -drop obvious ID cols
    - fix TotalCharges to numeric
    - map target Chrun to 0/1 if needed
    - simple NA handling
    
    """
    # tidy headers 
    df.columns = df.columns.str.strip() #remove leading / trailing whitespace

    # drop ids if present
    for col in ["customerID", "CustomerID", "customer_id"] :
        if col in df.columns :
            df = df.drop(columns = [col])

    # Target to 0/1 if it's Yes/No 
    if target_col in df.columns and df[target_col].dtype == "object":
        df[target_col] = df[target_col].str.strip().map({"No":0,"Yes":1})
    
    # TotalCharges often has blanks in this dataset -> coerce to float
    if "TotalCharges" in df.columns :
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors = "coerce")

    # SeniorCitizen should be 0/1 ints if present
    if "SeniorCitizen" in df.columns :
        df["SeniorCitizen"] = df["SeniorCitizen"].fillna(0).astype(int)

    # Simple NA strategy :
    # - numeric : fill with 0
    # - other :leave to encoders to handle (get_dummies ignores NaN safetly)
    num_cols = df.select_dtypes(include = ["number"]).columns
    df[num_cols] = df[num_cols].fillna(0)

    return df