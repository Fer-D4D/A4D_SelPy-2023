from Team.Fer.core.common_iv import TinyCore


class CreateAccount(TinyCore):

    def __init__(self, working_driver):
        super(CreateAccount, self).__init__()
        self.MAIN_DRIVER = working_driver
