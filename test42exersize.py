"""
Methods Exercise
Create method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.
Assume Federal Tax: 10%
Assume state tax on your wish
"""
def calculateNetIncome(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross Income
    :param state: State Name
    :return: Net Income
    """
    state_tax = {'CA': 10, 'NY': 9, "NJ": 6}
    #calculate net income after federal tax
    net = gross - gross*.10
    if state in state_tax:
        net = net - (gross*state_tax[state] / 100)
        print('your net income after taxes is: ' + str(net))
        return net
    else:
        print('State not in the list')
calculateNetIncome(10000, 'CA')