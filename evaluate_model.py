from sklearn.metrics import classification_report, roc_auc_score


def evaluate_models(models, X_test, y_test):

    for name, model in models.items():

        print("\n=======================")
        print(name)
        print("=======================")

        preds = model.predict(X_test)

        print(classification_report(y_test, preds))

        try:
            probs = model.predict_proba(X_test)[:,1]
            auc = roc_auc_score(y_test, probs)
            print("ROC AUC:", auc)
        except:
            print("ROC AUC unavailable")