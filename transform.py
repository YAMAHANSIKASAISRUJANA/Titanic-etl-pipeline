
def transform(df):
    df = df.copy()
    df["age"] = df["age"].fillna(df["age"].median())
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df = df.drop(columns=["deck", "embark_town"])
    df["sex"] = df["sex"].map({"male": 0, "female": 1})
    print(f"Transformed shape: {df.shape}")
    return df
