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


for j in range(1, 30, 1):
    flower = list()

    for i in range(1, 40, 1):
        data = "[%s,%s,%s]" % (int(str(j) + str(i)), int(str(j) + str(j)), j)
        flower.append(data);

    print(
        netApi.modifyNetwork(
            createdNetworkId,
            str("[%s]" % ",".join(flower)),
            'false'
        )['message']
    )
    
    time.sleep(1)