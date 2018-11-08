from Network import NetworksApi
from random import randint
import random
import sys

networkName = 'Generational Color Coding 2'

netApi = NetworksApi()

netApi.setCredentials(
    'tZoPskK2JTQgtyRYByZnbLpNrI4lzTyg', 
    'j35dP7vQMKxaBCiDsWKipYENjT5KruaI'
)
netApi.authorize()
netApi.acquireToken()

createNetworkRes = netApi.createNetwork(
    networkName
)
try:
    createdNetworkId = createNetworkRes['networkId']
except:
    print("Unable to create network: '%s' \n" % createNetworkRes['error'])
    networkFileList = netApi.listNetworks()
    for jData in networkFileList:
        if networkName in jData['name']:
            print(netApi.deleteNetwork(jData['id']))
            createdNetworkId = netApi.createNetwork(
                networkName
            )['networkId']

ids = list()
for i in range(500):
    newId = randint(0, 10000000)
    ids.append(newId)
    parentId = random.choice(ids)
    groupId = parentId
    dummyData = "[[%s,%s,%s]]" % (newId, parentId, groupId)
    netApi.modifyNetwork(
        createdNetworkId, 
        dummyData
    )
