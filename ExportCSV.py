from Network import NetworksApi

netApi = NetworksApi()

# Authenticate process
netApi.setCredentials(
    'tZoPskK2JTQgtyRYByZnbLpNrI4lzTyg', 
    'j35dP7vQMKxaBCiDsWKipYENjT5KruaI'
)
netApi.authorize()
netApi.acquireToken()

networkId = 'YXR0cmFjdG9yMi5jc3YuanNvbg=='

print(netApi.csvExport(networkId))

print(netApi.jsonExport(networkId))