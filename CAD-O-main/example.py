import xml.etree.ElementTree as ET

# Create an XML document with a root element
root = ET.Element("root")

# Create a subelement within the root element
subelement1 = ET.SubElement(root, "subelement1")
subelement1.text = "This is the text of subelement1"

# Create another subelement within the root element
subelement2 = ET.SubElement(root, "subelement2")
subelement2.text = "This is the text of subelement2"

# Create an XML tree from the root element
tree = ET.ElementTree(root)

# Save the XML tree to a file
tree.write("example.xml")
