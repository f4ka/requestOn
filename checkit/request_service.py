import urllib.request
import urllib.error
import urllib.parse
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class RequestService():

    def get_code(self, url, logs):
        try:
            code = urllib.request.urlopen(url).getcode()
            logs.info(url + " --- code response:" + str(code))
            return code
        except urllib.error.HTTPError as e:
            logs.error_status_code(e.code)
            return e.code
        except urllib.error.URLError as e:
            logs.general_error(e.reason)
            return e.reason
        except ValueError as e:
            logs.general_error("".join(e.args))
            return e.args
