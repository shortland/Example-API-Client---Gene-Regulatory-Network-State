from lib import Network

netApi = Network.NetworkApi(
    '0RNK9UsKTgCCRWSQJg6sdzdYp7JlWs9J', 
    'IIOunDfkI9bMolM2cJdwUx0IPTPPehzY'
)

networkId = 'QmVhdXRpZnklMjBOZXR3b3JrJTIwUmVuZGVyaW5nLmNzdi5qc29u'

print(netApi.deleteNetwork(networkId))