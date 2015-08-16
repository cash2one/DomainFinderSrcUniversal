from selenium import webdriver
from selenium.webdriver import ChromeOptions
from DomainFinderSrc.Utilities.FilePath import get_download_file_path, get_chrome_exe_path


class WebDriver:

    @staticmethod
    def get_chrome() -> webdriver.Chrome:
        options = ChromeOptions()
        download_option = {'download.default_directory': get_download_file_path(),
                           'download.directory_upgrade': 'true',
                           'download.extensions_to_open': '',
                           }
        options.add_experimental_option('prefs', download_option)
        return webdriver.Chrome(get_chrome_exe_path(), desired_capabilities=options.to_capabilities())
