test = {   'name': 'q1_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm_campaigns, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_data.shape[1] == 9 # Make sure not to change gfm_data, just create a new table called gfm_campaigns.\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_campaigns.shape[1] == 11 # Make sure you added 2 new columns.\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(gfm_campaigns.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', "
                                               "'Text', 'Proportion_Raised', 'Average_Donation_Amount'} # Make sure the columns are spelled correctly\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numbers;\n'
                                               ">>> (isinstance(gfm_campaigns.loc[0].get('Proportion_Raised'), numbers.Real)) and (isinstance(gfm_campaigns.loc[0].get('Average_Donation_Amount'), "
                                               'numbers.Real)) # Make sure the values in the new columns are decimals \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
