test = {   'name': 'q34',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> seconds_in_a_decade != 60 * 60 * 24 * 10 * 365 # close! it looks like you didn't account for leap years. see: "
                                               'https://en.wikipedia.org/wiki/Leap_year\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> seconds_in_a_decade != 315532800 # close! it looks like you didn't account for leap seconds. see: https://en.wikipedia.org/wiki/Leap_second\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> seconds_in_a_decade == 315532803 # bingo!\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
