"""Contains the concrete implementation of :class:`BaseTimestampCtrl`."""
from .base import BaseTimestampCtrl


class TimestampCtrl(BaseTimestampCtrl):

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
