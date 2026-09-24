# Changelog

---

## [1.0.3] - 2026-06-24

### Added
- Villagers now have a mix of jobs, including unemployed villagers, nitwits and children, and new trades every time
- Armour stands in the regular mineshaft now wear random armour
- Structure preview links in Moog's Structure Lib's config screen

### Changed
- Horses, donkeys, parrots and villagers look different every time a mineshaft generates
- Mineshafts have fewer mobs standing around in them
- The regular mineshaft's bogged spawners are now skeleton spawners
- Every structure has been rebuilt for each Minecraft version it supports, fixing a range of small visual and loading problems

### Fixed
- Parrots are back in the desert mineshaft room
- Item frames and paintings now appear correctly on every version
- The jungle, mesa, Nether and regular mineshafts now generate on Forge 1.20.1

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
