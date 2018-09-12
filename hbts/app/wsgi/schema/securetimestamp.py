"""The validation schema for ``#/components/schema/SecureTimestamp`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class SecureTimestamp(sq.schema.Schema):

    #: Specifies the protocol that was used to create the secure time
    #: stamp.
    protocol = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: Specifies the Time Stamping Authority (TSA) that handled the time
    #: stamping request.
    tsa = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
