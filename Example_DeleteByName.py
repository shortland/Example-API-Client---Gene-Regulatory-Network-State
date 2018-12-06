from lib import Network

netApi = Network.NetworkApi(
    '0RNK9UsKTgCCRWSQJg6sdzdYp7JlWs9J', 
    'IIOunDfkI9bMolM2cJdwUx0IPTPPehzY'
)

networkFileName = 'SomeFileName'

# Gets list of all Network Files
networkFileList = netApi.listNetworks()
for networkFile in networkFileList:
    if networkFile['name'] == networkFileName + ".csv.json":
        print(
            netApi.deleteNetwork(networkFile['id'])
        )