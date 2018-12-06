from lib import Network

netApi = Network.NetworkApi(
    '0RNK9UsKTgCCRWSQJg6sdzdYp7JlWs9J', 
    'IIOunDfkI9bMolM2cJdwUx0IPTPPehzY'
)

networkName = 'Example Network Name'

print(
    netApi.createNetwork(networkName)
)