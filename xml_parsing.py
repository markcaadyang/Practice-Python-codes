import xml.etree.ElementTree as ET #ET is like an alias/object

#multi line string '''
data = '''<person>
    <name>Mark</name>
    <phone type="intl">
        +63 939 724 1405
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))