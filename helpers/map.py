def get_all_maps():
    result = [
        Map(1, 'Arcade Map'),
        Map(1, 'Crystal Ore Map'),
        Map(1, 'Desert Map'),
        Map(1, 'Jungle Valley Map'),
        Map(2, 'Beach Map'),
        Map(2, 'Factory Map'),
        Map(2, 'Ghetto Map'),
        Map(2, 'Oasis Map'),
        Map(3, 'Arid Lake Map'),
        Map(3, 'Cavern Map'),
        Map(3, 'Channel Map'),
        Map(3, 'Grotto Map'),
        Map(3, 'Marshes Map'),
        Map(3, 'Sewer Map'),
        Map(3, 'Vaal Pyramid Map'),
        Map(4, 'Academy Map'),
        Map(4, 'Acid Lakes Map'),
        Map(4, 'Dungeon Map'),
        Map(4, 'Graveyard Map'),
        Map(4, 'Phantasmagoria Map'),
        Map(4, 'Villa Map'),
        Map(4, 'Waste Pool Map'),
        Map(5, 'Burial Chambers Map'),
        Map(5, 'Dunes Map'),
        Map(5, 'Mesa Map'),
        Map(5, 'Peninsula Map'),
        Map(5, 'Pit Map'),
        Map(5, 'Primordial Pool Map'),
        Map(5, 'Spider Lair Map'),
        Map(5, 'Tower Map'),
        Map(6, 'Canyon Map'),
        Map(6, 'Quarry Map'),
        Map(6, 'Racecourse Map'),
        Map(6, 'Ramparts Map'),
        Map(6, 'Spider Forest Map'),
        Map(6, 'Strand Map'),
        Map(6, 'Thicket Map'),
        Map(6, 'Vaal City Map'),
        Map(6, 'Wharf Map'),
        Map(7, 'Arachnid Tomb Map'),
        Map(7, 'Armoury Map'),
        Map(7, 'Ashen Wood Map'),
        Map(7, 'Castle Ruins Map'),
        Map(7, 'Catacombs Map'),
        Map(7, 'Cells Map'),
        Map(7, 'Mud Geyser Map'),
        Map(8, 'Arachnid Nest Map'),
        Map(8, 'Arena Map'),
        Map(8, 'Atoll Map'),
        Map(8, 'Barrows Map'),
        Map(8, 'Bog Map'),
        Map(8, 'Cemetery Map'),
        Map(8, 'Pier Map'),
        Map(8, 'Shore Map'),
        Map(8, 'Tropical Island Map'),
        Map(9, 'Coves Map'),
        Map(9, 'Crypt Map'),
        Map(9, 'Museum Map'),
        Map(9, 'Orchard Map'),
        Map(9, 'Overgrown Shrine Map'),
        Map(9, 'Promenade Map'),
        Map(9, 'Reef Map'),
        Map(9, 'Temple Map'),
        Map(10, 'Arsenal Map'),
        Map(10, 'Colonnade Map'),
        Map(10, 'Courtyard Map'),
        Map(10, 'Malformation Map'),
        Map(10, 'Quay Map'),
        Map(10, 'Terrace Map'),
        Map(10, 'Underground River Map'),
        Map(11, 'Bazaar Map'),
        Map(11, 'Chateau Map'),
        Map(11, 'Excavation Map'),
        Map(11, 'Precinct Map'),
        Map(11, 'Torture Chamber Map'),
        Map(11, 'Underground Sea Map'),
        Map(11, 'Wasteland Map'),
        Map(12, 'Crematorium Map'),
        Map(12, 'Estuary Map'),
        Map(12, 'Ivory Temple Map'),
        Map(12, 'Necropolis Map'),
        Map(12, 'Plateau Map'),
        Map(12, 'Residence Map'),
        Map(12, 'Shipyard Map'),
        Map(12, 'Vault Map'),
        Map(13, 'Beacon Map'),
        Map(13, 'Gorge Map'),
        Map(13, 'High Gardens Map'),
        Map(13, 'Lair Map'),
        Map(13, 'Plaza Map'),
        Map(13, 'Scriptorium Map'),
        Map(13, 'Sulphur Wastes Map'),
        Map(13, 'Waterways Map'),
        Map(14, 'Maze Map'),
        Map(14, 'Mineral Pools Map'),
        Map(14, 'Palace Map'),
        Map(14, 'Shrine Map'),
        Map(14, 'Springs Map'),
        Map(14, 'Volcano Map'),
        Map(15, 'Abyss Map'),
        Map(15, 'Colosseum Map'),
        Map(15, 'Core Map'),
        Map(15, 'Dark Forest Map'),
        Map(15, 'Overgrown Ruin Map'),
        Map(16, 'Forge of the Phoenix Map'),
        Map(16, 'Lair of the Hydra Map'),
        Map(16, 'Maze of the Minotaur Map'),
        Map(16, 'Pit of the Chimera Map'),
        Map(16, 'Vaal Temple Map'),
    ]
    for _map in result:
        if _map.tier <= 10:
            result.append(Map(_map.tier + 5, 'Shaped {0}'.format(_map.name)))

    return sorted(result, key=lambda _map: _map.tier)


def get_maps_by_tier():
    result = {}
    for _map in get_all_maps():
        if _map.tier not in result:
            result[_map.tier] = []
        result[_map.tier].append(_map)
    return result


class Map(object):
    tier = 0
    name = ''

    def __init__(self, tier, name):
        self.tier = tier
        self.name = name

    @property
    def drop_level(self):
        return self.tier + 67
