import subprocess


class Colorcodes(object):
    """
    Provides ANSI terminal color codes which are gathered via the ``tput``
    utility. That way, they are portable. If there occurs any error with
    ``tput``, all codes are initialized as an empty string.
    The provides fields are listed below.
    Control:
    - bold
    - reset
    Colors:
    - blue
    - green
    - orange
    - red
    :license: MIT
    """

    def __init__(self):
        try:
            self.bold = subprocess.check_output("tput bold".split())
            self.reset = subprocess.check_output("tput sgr0".split())

            self.blue = subprocess.check_output("tput setaf 4".split())
            self.green = subprocess.check_output("tput setaf 2".split())
            self.orange = subprocess.check_output("tput setaf 3".split())
            self.red = subprocess.check_output("tput setaf 1".split())
        except subprocess.CalledProcessError as e:
            self.bold = ""
            self.reset = ""

            self.blue = ""
            self.green = ""
            self.orange = ""
            self.red = ""


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


if __name__ == "__main__":
    print(Colorcodes().blue)
    print(bcolors.OKBLUE + "hello" + bcolors.ENDC)
    print(Colorcodes().orange)
    print(Colorcodes().red)
