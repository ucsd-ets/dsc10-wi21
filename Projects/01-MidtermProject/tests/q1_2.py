test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> covid.shape == (4692, 14)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(covid.columns) == set(['date', 'state', 'death', 'deathIncrease', 'hospitalized',\n"
                                               "...        'hospitalizedIncrease', 'negative', 'negativeIncrease', 'positive',\n"
                                               "...        'positiveIncrease', 'totalTestResults', 'totalTestResultsIncrease',\n"
                                               "...        'month', 'day'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numbers;\n'
                                               ">>> isinstance(covid.get('month').iloc[0], numbers.Integral) and isinstance(covid.get('day').iloc[0], numbers.Integral) #make sure the month and day "
                                               'columns contain integers, not strings\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
