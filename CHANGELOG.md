# Changelog

---

## [1.0.3] - 2026-06-22

### Added
- Minecraft 26.2 support (validator and pack format range extended to 1.21–26.2).

### Changed
- Tuned overworld mineshaft spacing for mansion-tier rarity (mineshaft, mesa_mineshaft, nether_mineshaft) based on /locate grid measurements against woodland mansion spacing.

### Fixed
- Restored compatibility with Minecraft 1.21–1.21.4 by fixing item-component shape mismatches the pre-1.21.5 codec rejected:
  - `minecraft:dyed_color` in `snowy_mineshaft` loot now uses the integer form instead of `{"rgb": N}`.
  - `minecraft:written_book_content` page text in `jungle_mineshaft` special crossings is now JSON-encoded so the strict Component codec accepts it.
  - `minecraft:enchantments` in `mineshaft/intersection_8` and `_9` now uses the flat enchant-ID map instead of the post-1.21.5 `levels` wrapper.
  - Sign messages across 28 NBTs are now JSON-encoded `""` so the `FilteredText<Component>` codec accepts them.
- `pack.mcmeta` now declares `supported_formats: [48, 107]` so MC 1.21.9+ doesn't reject the pack range.
- Removed a stray evoker spawn egg left in a dispenser in `mineshaft/intersection_8`.

---

## [1.0.2] - 2026-06-19

### Changed
- Surface mineshaft entrances now spawn on flatter ground and blend cleanly into it, so no more thin shelves or slope overhangs.
- Nether mineshafts now blend into the netherrack, with only their entrance carved open.
- Tuned mineshaft spacing to keep generation frequency consistent.

### Fixed
- Fixed a bunch of small bugs.

---

## [1.0.1] - 2026-06-10

### Added
- Snowy mineshafts now generate a surface entrance building that descends into the tunnels, with its own entrance loot including dyed and enchanted leather boots for crossing the mineshaft's powdered snow.

### Changed
- Snowy mineshafts now spawn on relatively flat terrain so the surface entrance sits cleanly, and their underground pieces are buried rather than carved into the ground.

---

## [1.0.0] - 2026-06-10

First alpha release of Moog's Mineshafts Reimagined.

### Added
- Six biome-specific reimagined mineshafts: base (taiga and similar overworld biomes), desert, jungle, mesa, snowy, and nether.
- Hand-built jigsaw tunnels and rooms made from vanilla blocks and entities, with loot, mob spawners, and feature rooms.
- Themed loot variants for supply barrels, miner chests, and treasure so containers vary between rooms, plus vaults and trial spawners.

---
