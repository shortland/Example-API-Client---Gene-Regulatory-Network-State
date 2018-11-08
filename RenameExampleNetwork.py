from Network import NetworksApi

netApi = NetworksApi()

# Authenticate process
netApi.setCredentials(
    'tZoPskK2JTQgtyRYByZnbLpNrI4lzTyg', 
    'j35dP7vQMKxaBCiDsWKipYENjT5KruaI'
)
netApi.authorize()
netApi.acquireToken()

networkId = 'R2VuZXJhdGlvbmFsJTIwQ29sb3IlMjBDb2RpbmclMjAyLmNzdi5qc29u'
newNetworkName = 'New Network Naming'

print(netApi.renameNetwork(networkId, newNetworkName))