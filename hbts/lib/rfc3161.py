import hashlib

import dsnparse
import rfc3161ng


class BaseTimestampAuthority:
    """The base class for all Time Stamp Authority (TSA) APIs."""

    @property
    def domain(self):
        return dsnparse.parse(self.url).host

    def __init__(self):
        self.tsa = rfc3161ng.RemoteTimestamper(self.url,
            certificate=str.encode(self.crt),
            hashname=self.digest)

    def timestamp(self, digest, algorithm='sha256'):
        """Contact the remote Time Stamp Authority (TSA) to create a secure
        time stamp for `digest`.
        """
        tsr = self.tsa.timestamp(digest=digest)
        checksum = hashlib.sha256(digest)
        checksum.update(bytes(tsr))
        return {
            'checksum': checksum.digest(),
            'document': digest,
            'algorithm': algorithm,
            'timestamp': rfc3161ng.get_timestamp(tsr),
            'tsa': self.domain,
            'signed': bytes(tsr)
        }


class ComodoTimestampAuthority(BaseTimestampAuthority):
    """Retrieves a secure timestamp from Comodo CA."""
    digest = 'sha256'
    crt = (
        "-----BEGIN CERTIFICATE-----\n"
        "MIIEnDCCA4SgAwIBAgIQTrCHj8wkNTay2Mn3vzlVdzANBgkqhkiG9w0BAQsFADCB\n"
        "lTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAlVUMRcwFQYDVQQHEw5TYWx0IExha2Ug\n"
        "Q2l0eTEeMBwGA1UEChMVVGhlIFVTRVJUUlVTVCBOZXR3b3JrMSEwHwYDVQQLExho\n"
        "dHRwOi8vd3d3LnVzZXJ0cnVzdC5jb20xHTAbBgNVBAMTFFVUTi1VU0VSRmlyc3Qt\n"
        "T2JqZWN0MB4XDTE1MTIzMTAwMDAwMFoXDTE5MDcwOTE4NDAzNlowgYYxCzAJBgNV\n"
        "BAYTAkdCMRswGQYDVQQIExJHcmVhdGVyIE1hbmNoZXN0ZXIxEDAOBgNVBAcTB1Nh\n"
        "bGZvcmQxGjAYBgNVBAoTEUNPTU9ETyBDQSBMaW1pdGVkMSwwKgYDVQQDEyNDT01P\n"
        "RE8gU0hBLTI1NiBUaW1lIFN0YW1waW5nIFNpZ25lcjCCASIwDQYJKoZIhvcNAQEB\n"
        "BQADggEPADCCAQoCggEBAM68dLdwgE9e8z+Yqi7L1BIBIzVpCyK85v0JbCjkExKs\n"
        "u7ot5dXdIu5ztiz40qRx50kleKslt5AQoJuLdybdQOpBo/2IzXKmiTtQVxx6JSQi\n"
        "AlFANWeKMWkN5TlzSTmblQGFUvIrFImaTgSkvECuOabdQALgOnX+PX1VlFvxTiR8\n"
        "yLhYGcrA2r5YE5rmHOfRwTvwXY9JCCGe0PO+1tRmT1xyNnvDgtOYCJSvq0RPGMcU\n"
        "2haxHjIOEjjAtTx27HVQACAEERntxv/fTv4IgScxT3F0bgMMcCeBVWqaQ5Kkf9v9\n"
        "P8UXHkG7zuinf4yV+f1/+GGIiQA+/wsB2/3VtaTkkRECAwEAAaOB9DCB8TAfBgNV\n"
        "HSMEGDAWgBTa7WR0FJwUPKvdmam9WyhNizzJ2DAdBgNVHQ4EFgQUfb+R16dsWkdm\n"
        "RHuQ1I6QckGPF8IwDgYDVR0PAQH/BAQDAgbAMAwGA1UdEwEB/wQCMAAwFgYDVR0l\n"
        "AQH/BAwwCgYIKwYBBQUHAwgwQgYDVR0fBDswOTA3oDWgM4YxaHR0cDovL2NybC51\n"
        "c2VydHJ1c3QuY29tL1VUTi1VU0VSRmlyc3QtT2JqZWN0LmNybDA1BggrBgEFBQcB\n"
        "AQQpMCcwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnVzZXJ0cnVzdC5jb20wDQYJ\n"
        "KoZIhvcNAQELBQADggEBAFCw9d9frTPcw1NYWLzCE3V7IB1Uyro/UD+6ivRrCWPA\n"
        "W12L1nUac72L/0fxFdxRFiMZMuZukk3Rxi5aHohCFMly5dcIUIpq9WRAVq4k42GX\n"
        "FULwLEiug+Y1PItbwo+ujsw0UjTg+/7K/bEkaNGkESMQBv2ywiQnx9fpShyPPz7P\n"
        "7et1eWyOX/chtlDmJaHNZpQSbL/bs66H2GgDciACwn7alPNyBzxX6FUk5wWgHcSB\n"
        "AYJLHz8PnTOb8E/MndaFgc/L5/1K6ZK49w1ycy3pd/lvjyh6Ph69CIbcjR4RX/db\n"
        "u4d2xp5MVGHQZ9uThNoxhwOS55/j6c9aVsho4FJJlFw=\n"
        "-----END CERTIFICATE-----\n"
    )
    url = "http://timestamp.comodoca.com/authenticode"
