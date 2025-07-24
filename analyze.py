from malScanAI.features import extract_features_from_ghidra
from malScanAI.model_loader import load_model
from malScanAI.predictor import predict


def main():
    print("[+] Extracting features from Ghidra...")
    feature_vector = extract_features_from_ghidra()

    print("[+] Loading model...")
    model = load_model("model/classifier.pkl")

    print("[+] Predicting malware type...")
    prediction = predict(model, feature_vector)
    print(f"[!] Prediction: {prediction}")


if __name__ == "__main__":
    main()


# malScanAI/features.py
def extract_features_from_ghidra():
    # Placeholder logic, assumes you have GhidraBridge active and the currentProgram context
