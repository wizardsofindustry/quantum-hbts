""""Declares a Python object mapping to the ``rfc3161`` relation."""
import sqlalchemy

from .base import Relation


class RFC3161Timestamp(Relation):
    """Maintains information about document hashes that were securely time
    stamped using plain RFC 3161.
    """

    __tablename__ = 'rfc3161'

    #: A SHA-256 hash of ``(document, signed)``
    checksum = sqlalchemy.Column(
        sqlalchemy.LargeBinary,
        name='checksum',
        nullable=False
    )

    #: A hex-encoded SHA-256 hash of the time stamped document.
    document = sqlalchemy.Column(
        sqlalchemy.String,
        name='document',
        primary_key=True,
        nullable=False
    )

    #: Specifies the hashing algorithm of `document`.
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

    #: The response of the TSA.
    signed = sqlalchemy.Column(
        sqlalchemy.LargeBinary,
        name='signed',
        nullable=False
    )


# pylint: skip-file
