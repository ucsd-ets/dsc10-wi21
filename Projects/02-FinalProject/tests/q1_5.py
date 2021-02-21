test = {   'name': 'q1_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_success.shape[1] == 12 # Make sure you made a new table, not added a new column to gfm_success.\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm.shape[1] == 13 # Make sure you added a new column\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(gfm.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', 'Text', "
                                               "'Proportion_Raised', 'Average_Donation_Amount', 'How_Successful', 'Num_Chars'} # Make sure the columns are spelled correctly\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> import numbers;\n>>> isinstance(gfm.loc[0].get('Num_Chars'), numbers.Integral) # Make sure the values in 'Num_Chars' are integers\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
