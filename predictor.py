def predict(model, features):
    # Convert dict to a fixed-length feature vector
    # This is a placeholder; in reality, you need a consistent order/encoding
    import numpy as np
    vector = np.array([features.get(k, 0) for k in sorted(features.keys())]).reshape(1, -1)
    return model.predict(vector)[0]
