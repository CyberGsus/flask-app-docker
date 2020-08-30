from logging import Formatter, LogRecord, INFO, getLogger, StreamHandler
from sys import stderr


class MyLogFormat(Formatter):
    colors = dict(
        zip(
            (
                "black",
                "red",
                "green",
                "yellow",
                "blue",
                "magenta",
                "cyan",
                "white",
                "orange",
            ),
            [*range(8), 214],
        )
    )
    colors_logging = {
        "WARNING": colors["yellow"],
        "INFO": colors["green"],
        "DEBUG": colors["blue"],
        "CRITICAL": colors["red"],
        "ERROR": colors["orange"],
    }

    sequences = {
        "reset": "\x1b[m",
        "color": "\x1b[38;5;{}m",
        "bold": "\x1b[1m",
        "under": "\x1b[4m",
    }

    ansi = {str(v): f"\x1b[38;5;{v}m" for v in range(256)}

    def format(self, record: LogRecord):
        seq = {
            k: (v.format(self.colors_logging[record.levelname]) if k == "color" else v)
            for k, v in self.sequences.items()
        }
        dkt = {}
        dkt.update(seq)
        dkt.update(
            {k: self.sequences["color"].format(v) for k, v in self.colors.items()}
        )
        dkt.update({"asctime": self.formatTime(record)})
        dkt.update(record.__dict__)
        dkt.update(self.ansi)
        dkt.update({"message": record.getMessage() % dkt})

        return seq["reset"] + (self._fmt % dkt) + seq["reset"]


def get_formatter():

    return MyLogFormat(
        "%(color)s%(name)s %(bold)s%(255)s[%(color)s%(levelname)s%(255)s]%(reset)s %(message)s"
    )


def default_handler():
    h = StreamHandler(stderr)
    h.setFormatter(get_formatter())
    return h


def setup_logger(name, log_level=INFO):
    l = getLogger(name)
    l.addHandler(default_handler())
    l.setLevel(log_level)
    f = get_formatter()
    return l
