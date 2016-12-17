
Corpus of data for fuzzing crypto parsers of various kinds.

asn1: ASN.1 data of all kinds, BER encoded
pkcs8: PKCS #8 private keys, BER encoded
cert: X.509 certificates, BER encoded
crl: X.509 CRLs, BER encoded
spki: X.509 subjectPublicKeyInfo structs, BER encoded
tls_client: TLS server flows (ie, testing a client)
tls_server: TLS client flows (ie, testing server)

All files should be named by their lowercase hex SHA-1 hash
of their contents. This allows easy deduplication.

The initial version is seeded from data from BoringSSL and OpenSSL.

PRs to add new corpus values will be accepted.

The goal is that any datums have a well defined format that can be
shared to test among multiple implementations. So corpus for modexp
and similar mathematical functions are not included yet.
