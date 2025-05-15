'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
import xml.dom.minidom as minidom

def beautify_xml(xml_file):
    final_xml = minidom.parseString(xml_file).toprettyxml()
    return final_xml
    