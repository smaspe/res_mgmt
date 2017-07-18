# res_mgmt
A resource management game framework

# TODOs
- [ ] Modeling
- [ ] Creating a basic model with 3-4 resources and a few technologies
- [ ] Describing the actions
- [ ] Adding an API
- [ ] Adding an administration API
- [ ] Adding a basic UI and a basic configuration as an example
- [ ] Stretch goal - adding a system to verify the balance of the resources when the game run
- [ ] Stretch goal - placing element on a map and require stuff to move from one to the next

# Modeling
- Costs are given in amounts of resources
- Time is given in units of time to be normalized (turn, s, ms, ns, ... whatever)

## Basics
- Resource
- Technology
- Worker

## Buildings

All buildings have:
- required technology
- required buildings
- construction cost
- construction time
- capabilities
- number and type of building workers
- maximum number of instances (-1 is infinite)

### Capabilities
- Storage (resources)
- Producers (resources in, resources out, production time, workers)
- Mine (resources out, production time, builders required, capacity)
- Lab (technology, required technologies, research cost, research time)
- Recruitement (worker, required technology)
- Housing (capacity)

### Upgrade
- Same content as a building 

# Example
(ITW)

```json
{
  "resources": [
    "log",
    "lumber",
    "stone"
  ],
  "technologies": [
    "lumbering"
  ],
  "workers": [
    {
      "name": "lumberjack"
    }
  ],
  "buildings": [
    {
      "name": "Town Hall",
      "technology": null,
      "cost": {
        "wood": 10
      },
      "time": 0,
      "maximum": 1,
      "workers": 0,
      "capabilities": {
        "storage": {
            "log": 10,
            "lumber": 10,
            "stone": 10
        },
        "housing": 10,
        "lab": [
          "lumber"
        ],
        "recruitment": [
          "lumberjack"
        ]
      }
    }
  ]
}
```
