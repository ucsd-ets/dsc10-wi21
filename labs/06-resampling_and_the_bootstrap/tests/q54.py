test = {   'name': 'q54',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # from numpy import std;\n>>> stdv = np.std(new_bootstrap_estimates);\n>>> 5 < stdv < 20\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 < new_right_end - new_left_end < 75\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> stdv = np.std(new_bootstrap_estimates);\n>>> abs(((new_right_end - new_left_end) / stdv) - 3.9) < .20\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
