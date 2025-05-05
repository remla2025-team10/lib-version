from importlib.resources import files

class VersionUtil():
    def __init__(self):
        try:
            # version_data = pkg_resources.resource_string('lib-version', 'VERSION')
            # return version_data.decode("utf-8").strip()
            self.__version__ = files("lib_version").joinpath("VERSION").read_text().strip()

        except:
            self.__version__ = "unknown"

    def get_version(self):
        return self.__version__