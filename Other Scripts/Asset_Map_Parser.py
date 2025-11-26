import xml.etree.ElementTree as ET
import json

xml_file = "assets_map.xml"

# Ask the user for the filter type
FILTER_TYPE = input("Enter the Type to extract (e.g. Texture2D, Material): ").strip()

container_map = {}
found_strings = set()

# Stream through the XML instead of loading it into memory
for event, elem in ET.iterparse(xml_file, events=("end",)):
    if elem.tag == "Asset":
        name_elem = elem.find("Name")
        container_elem = elem.find("Container")
        type_elem = elem.find("Type")

        name = name_elem.text.strip() if name_elem is not None and name_elem.text else None
        container = container_elem.text.strip() if container_elem is not None and container_elem.text else None
        asset_type = type_elem.text.strip() if type_elem is not None and type_elem.text else None

        if name and container and asset_type == FILTER_TYPE:
            container_map[container] = name
            found_strings.add(name)

        # Free memory for this <Asset> element
        elem.clear()

# Sorted list of names
sorted_files = sorted(found_strings)

# Output JSON + TXT
json_file = f"assets_map_{FILTER_TYPE}.json"
txt_file = f"assets_map_{FILTER_TYPE}.txt"

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(container_map, f, indent=2, ensure_ascii=False)

with open(txt_file, "w", encoding="utf-8") as f:
    f.write("\n".join(sorted_files))

print(f"Saved {len(container_map)} entries of type '{FILTER_TYPE}' to {json_file}")
input("\nDone! Press Enter to close...")
