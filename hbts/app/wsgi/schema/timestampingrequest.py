"""The validation schema for ``#/components/schema/TimestampingRequest`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class TimestampingRequest(sq.schema.Schema):

    #: A SHA-256 hash of the document for which a secure time stamp must
    #: be generated.
    checksum = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
