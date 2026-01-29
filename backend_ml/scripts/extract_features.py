import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # Count dots
    features.append(url.count('.'))

    # Check HTTPS
    features.append(1 if url.startswith("https") else 0)

    # Special characters count
    features.append(len(re.findall(r'[@\-_%]', url)))

    # Suspicious words
    suspicious_words = ['login', 'secure', 'bank', 'verify']
    features.append(
        sum(word in url.lower() for word in suspicious_words)
    )

    return features


if __name__ == "__main__":
    test_url = "https://secure-login.bank.com"
    print(extract_features(test_url))
