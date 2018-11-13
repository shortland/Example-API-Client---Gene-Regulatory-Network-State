import requests

class NetworkApi:
    def __init__(self, clientId, clientSecret):
        self.baseUrl = 'http://138.197.50.244/network2/api'
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.clientCode = self.authorize()
        self.clientToken = self.acquireToken()

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
        #print(response.text)
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
        return code
    
    def acquireToken(self):
        print("tokenize again")
        endpoint = '/token'
        parameters = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': self.clientCode
        }
        data = self.apiCall(endpoint, parameters, 'post')
        token = data['message']['token']
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

    def modifyNetwork(self, networkId, edgeList, save = 'false'):
        endpoint = '/modify_network'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId,
            'edgeList': str(edgeList),
            'save': save
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

    def csvExport(self, networkId):
        endpoint = '/export_csv'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId
        }
        data = self.apiCall(endpoint, parameters, 'get')
        return data

    def jsonExport(self, networkId):
        endpoint = '/export_json'
        parameters = {
            'token': self.clientToken,
            'networkId': networkId
        }
        data = self.apiCall(endpoint, parameters, 'get')
        return data
    
    def networkDiffs(self, oldNetworkId, newNetworkId):
        endpoint = 'network_diffs'
        parameters = {
            'token': self.clientToken,
            'oldNetworkId': oldNetworkId,
            'newNetworkId': newNetworkId
        }
        data = self.apiCall(endpoint, parameters, 'get')
        return data