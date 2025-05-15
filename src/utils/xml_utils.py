'''
Created on May 13, 2025

@author: Prashanth.Amancha
'''
import xml.etree.ElementTree as ET

def get_value_from_tag(xml_string, tag):
    root = ET.fromstring(xml_string)
    return root.find('.//{http://library.inbound.eaiwebservices.staffware.com/xsd}' + tag).text
