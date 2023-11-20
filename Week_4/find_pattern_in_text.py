def rabin_karp(pattern, text):
    p = 10**9 + 7
    x = 263

    def poly_hash(s):
        hash_value = 0
        for char in reversed(s):
            hash_value = (hash_value * x + ord(char)) % p
        return hash_value

    def precompute_hashes(text, pattern_length):
        text_length = len(text)
        h = [0] * (text_length - pattern_length + 1)
        s = text[text_length - pattern_length:]
        h[-1] = poly_hash(s)
        y = pow(x, pattern_length, p)

        for i in range(text_length - pattern_length - 1, -1, -1):
            h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % p

        return h

    pattern_hash = poly_hash(pattern)
    hash_values = precompute_hashes(text, len(pattern))

    occurrences = []
    for i in range(len(hash_values)):
        if pattern_hash == hash_values[i] and text[i:i + len(pattern)] == pattern:
            occurrences.append(i)

    return occurrences


if __name__ == "__main__":
    pattern = input().strip()
    text = input().strip()

    result = rabin_karp(pattern, text)

    print(" ".join(map(str, result)))
