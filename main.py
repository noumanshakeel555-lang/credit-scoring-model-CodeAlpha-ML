from src.preprocess import load_and_preprocess_data
from src.train import train_models
from src.evaluate_model import evaluate_models


def main():

    path = "data/credit_data.csv"

    X_train, X_test, y_train, y_test = load_and_preprocess_data(path)

    models = train_models(X_train, y_train)

    evaluate_models(models, X_test, y_test)


if __name__ == "__main__":
    main()