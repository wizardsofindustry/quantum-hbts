""""Declares a Python object mapping to the ``rfc3161`` relation."""
import sqlalchemy

from .base import Relation


class RFC3161Timestamp(Relation):
    """Maintains information about document hashes that were securely time
    stamped using plain RFC 3161.
    """

    __tablename__ = 'rfc3161'

    #: A hex-encoded SHA-256 hash of the time stamped document.
    checksum = sqlalchemy.Column(
        sqlalchemy.String,
        name='checksum',
        primary_key=True,
        nullable=False
    )

    #: Specifies the hashing algorithm of `checksum`.
    algorithm = sqlalchemy.Column(
        sqlalchemy.String,
        name='algorithm',
        nullable=False,
        default='sha256'
    )

    #: The timestamp returned by the TSA.
    timestamp = sqlalchemy.Column(
        sqlalchemy.DateTime(timezone=True),
        name='timestamp',
        nullable=False
    )

    #: Identifies the Time Stamping Authority (TSA).
    tsa = sqlalchemy.Column(
        sqlalchemy.String,
        name='tsa',
        nullable=False
    )

    #: Hex-encoded SHA-256 hash of the TSA certificate in PEM encoding,
    #: used to verify the response.
    crt = sqlalchemy.Column(
        sqlalchemy.String,
        name='crt',
        nullable=False
    )

    #: The response of the TSA.
    tsr = sqlalchemy.Column(
        sqlalchemy.LargeBinary,
        name='tsr',
        nullable=False
    )


# pylint: skip-file
