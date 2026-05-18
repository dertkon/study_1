
class Logger:
    instance = None
    log_list = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def log(self, message: str):
        self.log_list.append(message)

    def get_logs(self) -> list:
        return self.log_list


logger1 = Logger()
logger2 = Logger()

logger1.log('message1')
logger2.log('message2')

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["message1", "message2"]
