import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_preprocess_data(path):

    df = pd.read_csv(path)

    # safety check
    if df.isnull().sum().sum() > 0:
        df = df.fillna(df.median(numeric_only=True))

    X = df.drop("creditworthy", axis=1)
    y = df["creditworthy"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test