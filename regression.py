import argparse
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler


def load_dataset(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)

    raise ValueError("Unsupported file type. Please use a CSV or Excel file.")


def build_model(X: pd.DataFrame) -> Pipeline:
    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(max_iter=1000)),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Train a logistic regression model from a CSV or Excel dataset."
    )
    parser.add_argument("--file", help="Path to the dataset file.")
    parser.add_argument("--target", help="Name of the target column.")
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Fraction of data to reserve for testing. Default: 0.2",
    )
    args = parser.parse_args()

    file_path = args.file or input("Enter dataset file path: ").strip()
    target_column = args.target or input("Enter target column name: ").strip()
    test_size = args.test_size

    df = load_dataset(file_path)

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")

    df = df.dropna(subset=[target_column]).copy()
    X = df.drop(columns=[target_column])
    y = df[target_column]

    if y.nunique() != 2:
        raise ValueError(
            "Logistic regression in this script expects a binary target with exactly 2 classes."
        )

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=42, stratify=y_encoded
    )

    pipeline = build_model(X)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\nLogistic Regression Results")
    print("-" * 30)
    print(f"Dataset: {file_path}")
    print(f"Target column: {target_column}")
    print(f"Classes: {list(label_encoder.classes_)}")
    print(f"Accuracy: {accuracy:.4f}\n")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[str(label) for label in label_encoder.classes_],
        )
    )


if __name__ == "__main__":
    main()
