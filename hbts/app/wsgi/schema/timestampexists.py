"""The validation schema for ``#/components/schema/TimestampExists`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class TimestampExists(sq.schema.Schema):

    #: A code identifying the error condition.
    code = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: Error message targeted at the end-user.
    message = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: A message providing a more detailed explanation of the reasons why
    #: the service is not available.
    detail = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: A hint indicating on how to resolve the situation.
    hint = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
