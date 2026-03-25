```
#!/bin/sh
set -e

# Check if we're running with or without a certificate.
if [ "$USE_CERTIFICATE" = "true" ]; then
    # Sign the container image using Cosign with specified certificate
    cosign sign --key ./certs/key.pem $IMAGE_NAME:$IMAGE_TAG
else
    # Sign the container image using Cosign with default key (if available)
    cosign sign $IMAGE_NAME:$IMAGE_TAG
fi

# Output signature to a file for verification purposes
cosign verify --certificate-expiry 30d -output ./signature.txt $IMAGE_NAME:$IMAGE_TAG

exec "$@"
```