test = {   'name': 'q1_4',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm_success, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_campaigns.shape[1] == 11 # Make sure you made a new table, not added a new column to gfm_campaigns.\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_success.shape[1] == 12 # Make sure gfm_success has all the same data as gfm plus one new column\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(gfm_success.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', "
                                               "'Text', 'Proportion_Raised', 'Average_Donation_Amount', 'How_Successful'} # Make sure the columns are spelled correctly\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> isinstance(gfm_success.loc[0].get('How_Successful'), str)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
