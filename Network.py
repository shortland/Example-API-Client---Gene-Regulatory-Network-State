import requests

class NetworksApi:
    def __init__(self):
        self.baseUrl = 'http://138.197.50.244/network2/api'
        self.clientId = ''
        self.clientSecret = ''
        self.clientCode = ''
        self.clientToken = ''

    def setCredentials(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret
        return 'Credentials set\n'

    def getCredentials(self):
        return {
            'clientId': self.clientId,
            'clientSecret': self.clientSecret,
            'authorizationCode': self.clientCode,
            'acccessToken': self.clientToken
        }
    
    def apiCall(self, endpoint, parameters, type):
        if type is 'get':
            response = requests.get(
                url = self.baseUrl + endpoint,
                params = parameters
            )
        elif type is 'post':
            response = requests.post(
                url = self.baseUrl + endpoint,
                data = parameters
            )
        data = response.json()
        return data

    def authorize(self):
        endpoint = '/authorize'
        parameters = {
            'response_type': 'code',
            'client_id': self.clientId
        }
        data = self.apiCall(endpoint, parameters, 'get')
        code = data['message']['code']
        self.clientCode = code
        return code
    
    def acquireToken(self):
        endpoint = '/token'
        parameters = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': self.clientCode
        }
        data = self.apiCall(endpoint, parameters, 'post')
        token = data['message']['token']
        self.clientToken = token
        self.clientCode = ''
        return token

    def listNetworks(self):
        endpoint = '/list_networks'
        parameters = {}
        data = self.apiCall(endpoint, parameters, 'get')
        fileList = data['network_list']
        return fileList
    
    def networkChanges(self, networkId, epoch):
        endpoint = '/get_network_changes'
        parameters = {
            'networkId': networkId,
            'epoch': epoch
        }
        data = self.apiCall(endpoint, parameters, 'get')
        return data

    def modifyNetwork(self, networkId, edgeList):
        endpoint = '/modify_network'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId,
            'edgeList': str(edgeList)
        }
        data = self.apiCall(endpoint, parameters, 'post')
        return data

    def deleteNetwork(self, networkId):
        endpoint = '/delete_network'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId
        }
        data = self.apiCall(endpoint, parameters, 'post')
        return data

    def createNetwork(self, networkName):
        endpoint = '/create_network'
        parameters = {
            'token': self.clientToken,
            'networkName': networkName
        }
        data = self.apiCall(endpoint, parameters, 'post')
        return data

    def renameNetwork(self, networkId, networkNewName):
        endpoint = '/rename_network'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId,
            'networkNewName': networkNewName
        }
        data = self.apiCall(endpoint, parameters, 'post')
        return data