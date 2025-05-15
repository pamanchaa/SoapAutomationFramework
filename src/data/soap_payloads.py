'''
Created on May 13, 2025

@author: Prashanth.Amancha
'''

def get_case_start_payload(proc_name, case_desc):
    return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsd="http://library.inbound.eaiwebservices.staffware.com/xsd">
    <soapenv:Header/>
    <soapenv:Body>
        <xsd:doCaseStart>
            <xsd:procName>{proc_name}</xsd:procName>
            <xsd:caseDesc>{case_desc}</xsd:caseDesc>
            <xsd:startStep></xsd:startStep>
            <xsd:packData></xsd:packData>           
            <xsd:packMemo></xsd:packMemo>
        </xsd:doCaseStart>
    </soapenv:Body>
</soapenv:Envelope>"""

def get_do_suspend_payload(proc_name, case_num):
    return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsd="http://library.inbound.eaiwebservices.staffware.com/xsd">
    <soapenv:Header/>
    <soapenv:Body>
        <xsd:doSuspend>
             <xsd:procName>{proc_name}</xsd:procName>
             <xsd:caseNum>{case_num}</xsd:caseNum>
        </xsd:doSuspend>
    </soapenv:Body>
</soapenv:Envelope>"""

def get_nodename_payload():
    return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://library.inbound.eaiwebservices.staffware.com/xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <xsd:getNodeName/>
   </soapenv:Body>
</soapenv:Envelope>"""

