test = {   'name': 'q732',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> num_tweets != 3.2 and num_tweets != 4 and num_tweets != 4.0 #not quite, look for a mistake\nFalse', 'hidden': False, 'locked': False},
                                   {   'code': ">>> num_tweets == 3.2 #you can't make a non-integer number of tweets, can you? now that you know what the answer should be, just type it in. we'll "
                                               'learn soon how to have python do the rounding up for you.\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numbers;\n'
                                               ">>> isinstance(num_tweets, numbers.Integral) #we're looking for an integer. try using a conversion function like you did in the last sectio.\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
