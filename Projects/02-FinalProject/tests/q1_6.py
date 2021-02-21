test = {   'name': 'q1_6',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm.shape[1] == 13 # Make sure you overwrite the Text column, not add a new column\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(gfm.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', 'Text', "
                                               "'Proportion_Raised', 'Average_Donation_Amount', 'How_Successful', 'Num_Chars'} # Make sure the columns are spelled correctly\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> isinstance(gfm.loc[0].get('Text'), str) # Make sure the values in 'Text' are strings\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
