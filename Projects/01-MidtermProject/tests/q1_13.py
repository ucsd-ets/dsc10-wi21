test = {   'name': 'q1_13',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> 'weekend' in covid_q13.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> isinstance(covid_q13.get('weekend').loc[0], np.bool_) or isinstance(covid_q13.get('weekend').loc[0], bool) #the weekend column should containg "
                                               'True/False boolean values\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
