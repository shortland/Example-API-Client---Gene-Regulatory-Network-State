# GRNSS API Wrapper

## Starting off

```python
from lib import Network

netApi = Network.NetworkApi(
    'client_id',
    'client_secret'
)
```

## Example Scripts

- [Deleting Network Files](#network-deletion)
- [Creating Network Files](#network-creation)

### Sample Data Generation

Data output via [Example_FlowerNetwork.py](https://github.com/shortland/GRNSS-API-Wrapper/blob/master/Example_FlowerNetwork.py)

![FlowerNetwork.py Image Generation](https://ilankleiman.com/network2/images/FlowerNetwork.png)

### Network Deletion

```python
.deleteNetwork(networkId)
```

- By Network ID: [Example_DeleteByID.py](https://github.com/shortland/GRNSS-API-Wrapper/blob/master/Example_DeleteByID.py)
- By Network Name: [Example_DeleteByName.py](https://github.com/shortland/GRNSS-API-Wrapper/blob/master/Example_DeleteByName.py)
- All Networks: [Example_DeleteAll.py](https://github.com/shortland/GRNSS-API-Wrapper/blob/master/Example_DeleteAll.py)

### Network Creation

```python
.createNetwork(networkName)
```

- With Name: [Example_CreateByName.py](https://github.com/shortland/GRNSS-API-Wrapper/blob/master/Example_CreateByName.py)