# DAF: Directories and Files

import os


class DAF:

    @classmethod
    def mkdir(cls, directory: str):
        if not os.path.exists(directory):
            os.mkdir(directory)

        return cls
