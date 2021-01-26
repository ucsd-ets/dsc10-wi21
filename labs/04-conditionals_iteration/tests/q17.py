test = {   'name': 'q17',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> (result == 'Wow!') or (result == 'Meh.') or (result == 'Okay!')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> ten_nachos = np.array(['neither', 'cheese', 'both', 'both', 'cheese', 'salsa', 'both', 'neither', 'cheese', 'both']);\n"
                                               '>>> ten_nachos_reactions = bpd.DataFrame().assign(Nachos=ten_nachos);\n'
                                               '>>> ten_nachos_reactions = ten_nachos_reactions.assign(Reactions=ten_nachos_reactions.get("Nachos").apply(nacho_reaction));\n'
                                               ">>> both_or_neither(ten_nachos_reactions) == 'Wow!'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> seven_nachos = np.array(['neither', 'cheese', 'both', 'both', 'neither', 'both', 'neither']);\n"
                                               '>>> seven_nachos_reactions = bpd.DataFrame().assign(Nachos=seven_nachos);\n'
                                               '>>> seven_nachos_reactions = seven_nachos_reactions.assign(Reactions=seven_nachos_reactions.get("Nachos").apply(nacho_reaction));\n'
                                               ">>> both_or_neither(seven_nachos_reactions) == 'Okay!'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
