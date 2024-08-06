from model import Model
from qtip import random_hadamard_transform, bitshift_trellis, generate_codes_1mad, quantize_with_trellis

def integrate_qtip(model):
    weights = model.get_weights()
    transformed_weights = random_hadamard_transform(weights)
    trellis = bitshift_trellis(transformed_weights)
    codes = generate_codes_1mad(transformed_weights)  # or use generate_codes_3inst
    quantized_weights = quantize_with_trellis(transformed_weights, trellis, codes)
    model.set_weights(quantized_weights)
    return model

if __name__ == "__main__":
    initial_weights = np.random.randn(10, 10)  # Placeholder for actual model weights
    model = Model(initial_weights)
    quantized_model = integrate_qtip(model)
    print("Original weights:")
    print(initial_weights)
    print("Quantized weights:")
    print(quantized_model.get_weights())
