# res_mgmt
A resource management game framework

# TODOs
- [ ] Modeling
- [ ] Create a basic model with 3-4 resources and a few technologies
- [ ] Describing the actions
- [ ] Adding an API
- [ ] Adding an administration API
- [ ] Adding a basic UI and a basic configuration as an example
- [ ] Stretch goal - add a system to verify the balance of the resources when the game run
- [ ] Stretch goal - place element on a map and require stuff to move from one to the next

# Modeling
- Costs are given in amounts of resources
- Time is given in units of time to be normalized (turn, s, ms, ns, ... whatever)

## Basics
- Resource (storable vs non-storable - e.g. water vs electricity)
- Technology (pre-requisites, research cost, research time)
- Worker (required technology, buildings)

## Buildings
All buildings have:
- required technology
- required buildings (?)
- construction cost
- construction time
- workers
- capabilities

### Capabilities
- Storage (resources)
- Producers (resources in, resources out, production time, workers)
- Mine (resources out, production time, builders required, capacity)
- Lab (technologies)
- Recrutement (workers)
- Housing (capacity)

### Upgrade
- Same content as a building
