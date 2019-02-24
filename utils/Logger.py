class Logger:

    @staticmethod
    def _log(level, message):
        print("{0}: {1}".format(level, message))

    @staticmethod
    def error(message):
        Logger._log("ERROR", message)

    @staticmethod
    def warning(message):
        Logger._log("WARNING", message)

    @staticmethod
    def info(message):
        Logger._log("INFO", message)

    @staticmethod
    def debug(message):
        Logger._log("DEBUG", message)
