
Corpus of data for fuzzing crypto parsers of various kinds.

* asn1: ASN.1 data of all kinds, BER encoded
* cert: X.509 certificates, BER encoded
* crl: X.509 CRLs, BER encoded
* ocsp: OCSP responses, BER encoded
* pkcs1: PKCS v1.5 encryption padding
* pkcs8: PKCS #8 private keys, BER encoded
* spki: X.509 subjectPublicKeyInfo structs, BER encoded
* tls_client: TLS server flows (ie, testing a client)
* tls_server: TLS client flows (ie, testing server)
* x509_dn: X.509 DistinguishedNames

All files should be named by their lowercase hex SHA-1 hash
of their contents. This allows easy deduplication.

The initial version is seeded from corpus data from BoringSSL and
OpenSSL, some reference inputs, plus corpus data generated by OSS-Fuzz
while running the Botan fuzzers.

PRs to add new corpus values will be accepted.

The goal is that any datums have a well defined format that can be
shared to test among multiple implementations. So corpus for modexp
and similar mathematical functions are not included yet, but should be.