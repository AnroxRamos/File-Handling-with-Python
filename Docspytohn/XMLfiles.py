import xml.etree.ElementTree as ET

# Reading an XML file
tree = ET.parse('data.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

# Writing to an XML file
root = ET.Element("data")
ET.SubElement(root, "item").text = "Example"
tree = ET.ElementTree(root)
tree.write("data.xml")
