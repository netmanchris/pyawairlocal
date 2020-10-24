

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
    Function to fetch latest sensor readings from support Awair device with Local REST
    API enabled
    :param awairclient:
    :param data:
    :return: JSON object representing sensor readings
    '''
    path = 'air-data/latest'
    response = awairclient.get(path)
    return response.json() if response else None
