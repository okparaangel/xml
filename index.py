# design a simple python program that is able to read an write to an xml file

import xml.etree.ElementTree as ET

def create_xml_file(file_path):
    root = ET.Element("note")
    to = ET.SubElement(root, "to")
    sender = ET.SubElement(root, "from")
    heading = ET.SubElement(root, "heading")
    body = ET.SubElement(root, "body")
    
    to.text = "anestin@gmail.com"
    sender.text = "angel@gmail.com"
    heading.text = "New user"
    body.text = "Thank you for registration"


    tree = ET.ElementTree(root)
    tree.write(file_path)

def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for user in root.findall("user"):
        user_id = user.find("id").text
        user_name = user.find("name").text
        print(f"User ID: {user_id}, Name: {user_name}")

def main():
    file_path = "smtp.xml"
    create_xml_file(file_path)
    print("XML file created successfully!")

    print("Reading from XML file:")
    read_xml_file(file_path)

if __name__ == "__main__":
    main()


import xml.etree.ElementTree as ET

def create_xml_file(file_path):
    root = ET.Element("data")

    item1 = ET.SubElement(root, "item")
    item1.text = "cyberSecurity"

    item2 = ET.SubElement(root, "item")
    item2.text = "SocialEnginerring"

    tree = ET.ElementTree(root)

    tree.write(file_path)

def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for item in root.findall("item"):
        print(item.text)

if __name__ == "__main__":
    file_path = "data.xml"

    create_xml_file(file_path)
    read_xml_file(file_path)
