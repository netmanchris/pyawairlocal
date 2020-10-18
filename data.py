

def get_dev_config(awairclient, data=None):
    """

    :param awairclient:
    :return:
    """
    path = 'settings/config/data'
    response = awairclient.get(path)
    return response.json() if response else None

def get_dev_data(awairclient, data=None):
    '''

    :param awairclient:
    :param data:
    :return:
    '''
    path = 'air-data/latest'
    response = awairclient.get(path)
    return response.json() if response else None
