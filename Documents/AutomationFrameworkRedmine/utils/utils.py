# CONSTANTS
import inspect

URL = 'http://demo.redmine.org/'
USERNAME = 'icecream1'
PASSWORD = '1234'


def whoami():
    return inspect.stack()[1][3]
