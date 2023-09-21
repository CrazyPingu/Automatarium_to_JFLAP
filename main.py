#!/bin/bash
import xml.etree.ElementTree as ET
import json

# Read JSON data from the file
with open("test.json", "r") as json_file:
    json_data = json.load(json_file)

# Create the XML root element
root = ET.Element("structure")
root.attrib["xmlns"] = "http://www.w3.org/1999/xhtml"
root.attrib["version"] = "1.0"

# Create and append the <type> element
type_element = ET.SubElement(root, "type")
type_element.text = "fa"

# Create and append the <automaton> element
automaton_element = ET.SubElement(root, "automaton")

# Add states to the automaton
for state in json_data["states"]:
    state_element = ET.SubElement(automaton_element, "state")
    state_element.attrib["id"] = str(state["id"])
    state_element.attrib["name"] = "q" + str(state["id"])
    x_element = ET.SubElement(state_element, "x")
    x_element.text = str(state["x"])
    y_element = ET.SubElement(state_element, "y")
    y_element.text = str(state["y"])
    if "label" in state:
        label_element = ET.SubElement(state_element, "label")
        label_element.text = state["label"]

# Add transitions to the automaton
for transition in json_data["transitions"]:
    transition_element = ET.SubElement(automaton_element, "transition")
    from_element = ET.SubElement(transition_element, "from")
    from_element.text = str(transition["from"])
    to_element = ET.SubElement(transition_element, "to")
    to_element.text = str(transition["to"])
    read_element = ET.SubElement(transition_element, "read")
    read_element.text = transition["read"]

# Create the XML tree
tree = ET.ElementTree(root)

# Write the XML to a file or print it
tree.write("output.jff", encoding="utf-8", xml_declaration=True)