from client import ConvolutionalViterbi

def main():
    print("=== Testing Convolutional Viterbi Codec ===")
    conv = ConvolutionalViterbi()
    bits = [1, 0, 1, 1, 0]
    encoded = conv.encode(bits)
    print("Encoded transmission stream:", encoded)

    # Inject channel noise
    encoded[3] ^= 1
    decoded = conv.decode(encoded)
    print("Decoded bit stream:          ", decoded)
    assert decoded[:len(bits)] == bits
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
