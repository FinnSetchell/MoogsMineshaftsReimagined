# Changelog

---

## [1.1.0] - 2026-10-01

### Added
- Three new mineshafts: the dark oak mineshaft, the mushroom mineshaft and the deep dark mineshaft
- Villagers now have a mix of jobs, including unemployed villagers, nitwits and children, and new trades every time
- Armour stands in the regular mineshaft now wear random armour
- Structure preview links in Moog's Structure Lib's config screen
- Mineshafts now sometimes generate entirely underground, with no entrance on the surface
- The mesa mineshaft now sometimes has a surface entrance, with a trial room, a trapped chest and armour stands in gold armour
- An option in Moog's Structure Lib's config screen that replaces vanilla mineshafts with Moog's, about as common as vanilla ones were
  - With it on, some chests hold vanilla mineshaft loot, so loot added by other mods shows up there too
- Advancements for discovering each kind of mineshaft, and a challenge for finding them all

### Changed
- Horses, donkeys, parrots and villagers look different every time a mineshaft generates
- Mineshafts have fewer mobs standing around in them
- Spawners in the regular mineshaft now spawn skeletons
- Every structure has been rebuilt for each Minecraft version it supports, fixing a range of small visual and loading problems
- Mineshaft tunnels no longer adapt the surface terrain. This fixes the large flat areas by mineshaft entrances
- Underground tunnels are now wrapped in stone instead of breaking into caves
- The regular underground mineshaft can now appear in most overworld biomes
- Mineshafts now spread out about as far as vanilla mineshafts, with more tunnels and branches
- Special rooms turn up much more often, but never more than once or twice in the same mineshaft. This includes the warden prison and sculk pit in the deep dark mineshaft, the big rooms in the regular mineshaft, the special crossings in the desert, jungle and Nether mineshafts, the dog room in the snowy mineshaft and the large dead ends in the mushroom mineshaft
- Mineshafts no longer generate on top of vanilla mineshafts
- The regular and mesa mineshafts have fewer tunnel junctions, so they're less of a maze

### Fixed
- Parrots are back in the desert mineshaft room
- Item frames and paintings now appear correctly on every version
- Two rooms in the Nether mineshaft had empty spawners; they now spawn piglin brutes, wither skeletons and blazes
- The jungle, mesa, Nether and regular mineshafts now generate on Forge 1.20.1
- The minecart chest in the jungle mineshaft now has treasure in it
- Cacti, carts and gold piles now appear beside the desert mineshaft's paths
- The suspicious sand in the desert mineshaft now has loot
- The Nether mineshaft's mess hall can now generate
- A few jungle and Nether tunnels that could never generate now do, including the jungle drop shaft

![dark oak mineshaft](https://i.moogsmods.com/images/6f4c3584293d4be886fee57b70f4385f.png)
![deep dark mineshaft](https://i.moogsmods.com/images/9607415efe5c46c0ac3ee565ffc56a20.png)
![mushroom mineshaft](https://i.moogsmods.com/images/33d6390f8e3c476d94ce8835d9175b6c.png)
![underground view of 3 mineshafts](https://i.moogsmods.com/images/92bdc2bed6884456b0d2de4321215ac0.png)
![configuration settings for mmr](https://i.moogsmods.com/images/842f6eb882e9486ea5292d52b66d3cc0.png)

---

## [1.0.2] - 2026-06-22

First port of MMR to Minecraft 1.20–1.20.6.

### Added
- Custom `#mmr:` biome tags so structure biome lists resolve identically across Fabric 1.20.x (where Convention Tags v2 names differ from 1.20.5+) and Forge 1.20.x (which uses the `forge:` namespace).
- Explicit 1.20.5 and 1.20.6 version mappings so MSL picks the right template per MC, with entity item format adjusted for the 1.20.6 component overhaul.

### Changed
- Ported to 1.20–1.20.6. Substituted 1.21-only blocks and entities (tuff variants → stone variants, copper bulbs → shroomlights, crafter → dropper, bogged → stray, decorated pot palette adjusted). Reshaped sign and item NBTs for the 1.20 codec. Renamed `structure/` and `loot_table/` paths to the plural form 1.20 expects.
- Vault rooms now use chest loot (no 1.20.x equivalent for vaults / trial spawners).
- Replaced the 1.21 guster banner pattern with a 1.20-safe alternative.
- Tuned overworld mineshaft spacing for mansion-tier rarity (ported from 1.21-datapack).

### Removed
- Ominous loot tables and trial-spawner pieces (no 1.20.x equivalent).
- 1.21-only processors and `1_21_9/` NBT version-forks (not needed on 1.20.x).

---

## [1.0.0] - 2026-06-10

First alpha release of Moog's Mineshafts Reimagined (1.21-datapack line). See the [1.21-datapack branch](../../tree/1.21-datapack/CHANGELOG.md) for the 1.21 release history; this branch's history starts with 1.0.2 as the first 1.20 port.

---
