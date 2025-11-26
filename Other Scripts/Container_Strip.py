import xml.etree.ElementTree as ET

xml_file = "assets_map.xml"
txt_file = "Containers.txt"

containers = set()

# Iteratively parse the XML
for event, elem in ET.iterparse(xml_file, events=("end",)):
    if elem.tag == "Asset":
        container_elem = elem.find("Container")
        if container_elem is not None and container_elem.text:
            containers.add(container_elem.text.strip())

        # Clear element from memory
        elem.clear()

# Sort and save
unique_containers = sorted(containers)

with open(txt_file, "w", encoding="utf-8") as f:
    f.write("\n".join(unique_containers))

print(f"Saved {len(unique_containers)} unique container IDs to {txt_file}")
input("\nDone! Press Enter to close...")
