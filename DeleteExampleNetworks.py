from Network import NetworksApi

netApi = NetworksApi()

# Authenticate process
netApi.setCredentials(
    'tZoPskK2JTQgtyRYByZnbLpNrI4lzTyg', 
    'j35dP7vQMKxaBCiDsWKipYENjT5KruaI'
)
netApi.authorize()
netApi.acquireToken()

# Get a list of all network file ids that match the name pattern 'Example Network File Name'
networkFileList = netApi.listNetworks()
for jData in networkFileList:
    if 'Generational Color Coding' in jData['name']:
        print(netApi.deleteNetwork(jData['id']))

