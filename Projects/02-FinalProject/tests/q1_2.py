test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(gfm_data, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> gfm_data.shape[1] == 9 # Make sure to overwrite columns, not to add new columns.\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> set(gfm_data.columns) == {'Category', 'Title', 'Location', 'Amount_Raised', 'Goal', 'Days_of_Fundraising', 'Number_of_Donors', 'FB_Shares', "
                                               "'Text'}# Make sure the columns are spelled correctly\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> gfm_data.shape[0] == 838\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
