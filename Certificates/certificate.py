from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import datetime


#--------CA CERTIFICATE------#
# Generate CA key
ca_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)


# Create issuer (CA)
ca_subject = ca_issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CA"),
    x509.NameAttribute(NameOID.COMMON_NAME, "ca.com"),
])

#Generate CA certificate
ca_certificate = x509.CertificateBuilder().subject_name(
    ca_subject
).issuer_name(
    ca_issuer
).public_key(
    ca_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc)
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("localhost")]),
    critical=False,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256())

# Write our certificate out to disk.
with open("./certs/ca_certificate.pem", "wb") as f:
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))



#------Pantheon Certificate----#

# Generate Pantheon key
pantheon_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create subject (Pantheon)
pantheon_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "Israel"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Center"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Rishon Letsion"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Pantheon"),
    x509.NameAttribute(NameOID.COMMON_NAME, "pantheon.arcimedes.idf.il"),
])

#Generate CA certificate
ca_cert = x509.CertificateBuilder().subject_name(
    pantheon_subject
).issuer_name(
    ca_issuer
).public_key(
    pantheon_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc)
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("localhost")]),
    critical=False,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256())

