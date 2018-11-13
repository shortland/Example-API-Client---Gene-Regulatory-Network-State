from lib import Network
from random import randint
import random
import time

netApi = Network.NetworkApi('0RNK9UsKTgCCRWSQJg6sdzdYp7JlWs9J', 'IIOunDfkI9bMolM2cJdwUx0IPTPPehzY')

networkName = 'Beautify Network Rendering'

createNetwork = netApi.createNetwork(networkName)

try:
    createdNetworkId = createNetwork['networkId']
except:
    print("Unable to create network: '%s' \n" % createNetwork['error'])
    networkFileList = netApi.listNetworks()
    for jData in networkFileList:
        if networkName in jData['name']:
            print(netApi.deleteNetwork(jData['id'])['message'], "\n")
            createdNetworkId = netApi.createNetwork(
                networkName
            )['networkId']
            print('Recreated network with id:', createdNetworkId, '\n')

loadedNetworkCSV = netApi.csvExport('U3RhbmRhcmQlMjBOZXR3b3JrJTIwTGFiZWxlZC5jc3YuanNvbg==')

groups = list()
for nodeData in loadedNetworkCSV:
    nodeDataArr = nodeData.split(',')
    if nodeDataArr[2] not in groups:
        groups.append(nodeDataArr[2])

print(len(groups))

for group in groups:
    groupNetwork = list()
    for nodeData in loadedNetworkCSV:
        nodeDataArr = nodeData.split(',')
        if nodeDataArr[2] == group:
            groupNetwork.append("[%s]" % nodeData)

    groupNetworkChunk = ",".join(groupNetwork)
    print(netApi.modifyNetwork(
        createdNetworkId, 
        str("[%s]" % groupNetworkChunk),
        'false'
    )['message'])
    time.sleep(4)