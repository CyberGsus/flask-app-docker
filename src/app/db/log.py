from pymongo import monitoring
from ..log import setup_logger
from logging import DEBUG

logger = setup_logger("db:mongo", DEBUG)


def log(event, type="started"):
    color_fmt = {"started": "%(117)s", "succeeded": "%(118)s", "failed": "%(203)s"}
    log_type = {"started": "debug", "succeeded": "info", "failed": "error"}
    getattr(logger, log_type[type])(
        "Command %(bold)s{0.command_name}%(reset)s with request id {0.request_id} {2}{1}%(reset)s".format(
            event, type, color_fmt[type]
        )
        + (
            " on server {0.connection_id}".format(event)
            if type == "started"
            else " in {0.duration_micros} microseconds".format(event)
        )
    )


class CommandLogger(monitoring.CommandListener):
    def started(self, event):
        log(event, "started")

    def succeeded(self, event):
        log(event, "succeeded")

    def failed(self, event):
        log(event, "failed")


monitoring.register(CommandLogger())