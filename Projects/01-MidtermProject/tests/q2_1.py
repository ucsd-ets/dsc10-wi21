test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(sd_covid_outbreaks, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> ('outbreak_index' in sd_covid_outbreaks.columns) and ('total_outbreaks' in sd_covid_outbreaks.columns) # check your columns' names\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> sd_covid_outbreaks.shape == (844, 7) #make sure you have the right number of rows and columns \nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import numbers ;\n'
                                               ">>> index_type = sd_covid_outbreaks.get('outbreak_index').values[0];\n"
                                               ">>> total_type = sd_covid_outbreaks.get('total_outbreaks').values[0];\n"
                                               '>>> isinstance(index_type,numbers.Integral) and isinstance(total_type,numbers.Integral) #outbreak_index and total_oubreaks should be ints\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
