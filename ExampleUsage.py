from Network import NetworksApi
from random import randint
import sys
import time

netApi = NetworksApi()

###
# Set clientId and clientSecret in the NetworksApi object
###

print(
    netApi.setCredentials(
        'tZoPskK2JTQgtyRYByZnbLpNrI4lzTyg', 
        'j35dP7vQMKxaBCiDsWKipYENjT5KruaI'
    )
)

###
# Retrieve a new temporary Authorization Code
###

print(
    "Retrieved Authorization Code: %s \n" % netApi.authorize()
)

###
# Retrieve a new Access Token for the API
###

print(
    "Retrieved Access Token: %s \n" % netApi.acquireToken()
)

###
# Create new Network file
###

newNetworkFileName = "Example Network File Name %s" % randint(20, 10000)

print("Creating a Network file with the name: '%s'\n" % newNetworkFileName)

createNetworkRes = netApi.createNetwork(
    newNetworkFileName
)

try:
    createdNetworkId = createNetworkRes['networkId']
except:
    print("Unable to create network: '%s' \n" % createNetworkRes['error'])
    sys.exit()

print(
    "Created New Network with Id: %s \n" % createdNetworkId
)

###
# View list of all Network files
###

print("Network File List:")
networkFileList = netApi.listNetworks()
for jData in networkFileList:
    print("\tFile name: ", jData['name'])
    print("\tFile id: ", jData['id'])
    print("\t")

###
# Append new data to the Network that was just created
###

groupInt = randint(0, 9)
destInt = randint(2000, 6000)
idInt = destInt
dummyData = "[[%d,%d,%d],[%d,%d,%d],[%d,%d,%d]]" % (idInt, destInt, groupInt, idInt + 1, destInt, groupInt, idInt + 2, destInt, groupInt)
print(
    "Modify recently createed Network: %s \n" % netApi.modifyNetwork(
        createdNetworkId, 
        dummyData
    )
)

###
# List changes that have been made to a Network file.
# Given a Timestamp; only changes made to the network after the timestamp will be listed.
###

print(
    "Network changes within last 10 seconds: \n%s \n" % netApi.networkChanges(
        createdNetworkId, 
        int(time.time()) - 10
    )
)

###
# Delete the dummy Network file that was just created
###

print(
    "Delete existing Network: \n%s \n" % netApi.deleteNetwork(
        createdNetworkId
    )
)