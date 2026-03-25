```
# Use the Sigstore and Cosign for signing container images
FROM golang:latest as builder

WORKDIR /go/src/github.com/example/sigstore-cosign
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN make build-static && mv bin/cosign ./cosign

# Final image with just the binary and its runtime dependencies
FROM alpine:latest
COPY --from=builder /go/src/github.com/example/sigstore-cosign/cosign /usr/local/bin/
```