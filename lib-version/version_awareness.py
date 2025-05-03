import pkg_resources

class VersionUtil():
    def get_version(self):
        try:
            version_data = pkg_resources.resource_string('lib-version', 'VERSION')
            return version_data.decode("utf-8").strip()
        except:
            return "unknown"