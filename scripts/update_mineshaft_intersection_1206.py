"""
Convert entity HandItems from old item format (Count: Byte) to new format (count: Int)
for mineshaft/intersection_8 and mineshaft/intersection_9.
Writes updated copies as intersection_8_1206.nbt and intersection_9_1206.nbt.
Required for MC 1.20.5+ which expects the new item component format.
"""
import shutil
import nbtlib
from pathlib import Path

STRUCTURES = Path(__file__).parent.parent / "src/main/resources/data/mmr/structures/mineshaft"

def convert_item(item: nbtlib.Compound) -> nbtlib.Compound:
    if "Count" in item and isinstance(item["Count"], nbtlib.Byte):
        count_val = int(item["Count"])
        new_item = nbtlib.Compound({k: v for k, v in item.items() if k != "Count"})
        new_item["count"] = nbtlib.Int(count_val)
        return new_item
    return item

def update_nbt(src: Path, dst: Path) -> int:
    nbt = nbtlib.load(src)
    changed = 0
    for entity in nbt.get("entities", []):
        hand_items = entity.get("nbt", {}).get("HandItems", [])
        for i, item in enumerate(hand_items):
            if item and "Count" in item:
                hand_items[i] = convert_item(item)
                changed += 1
    nbt.save(dst)
    return changed

for name in ["intersection_8", "intersection_9"]:
    src = STRUCTURES / f"{name}.nbt"
    dst = STRUCTURES / f"{name}_1206.nbt"
    n = update_nbt(src, dst)
    print(f"  {dst.name}: {n} item(s) converted")

print("Done.")
