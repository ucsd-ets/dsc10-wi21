test = {   'name': 'q4_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm_impactful, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> gfm_impactful.shape[1] == 14 # Make sure you make a dataframe (gfm_impactful) with all the data from gfm plus a new column\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> set(gfm_impactful.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', "
                                               "'Text', 'Proportion_Raised', 'Average_Donation_Amount', 'How_Successful', 'Num_Chars', 'Has_Impactful'}\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
