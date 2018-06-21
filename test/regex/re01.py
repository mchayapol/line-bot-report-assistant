import re
messageList = [
    'ขอรายงานครับ',
    'เริ่มต้นการรายงานครับ',
    'ขอแจ้งข่าวครับ'
]

START_REPORT_PATTERN = 'รายงาน|แจ้งข่าว'
for message in messageList:
    m = re.search(START_REPORT_PATTERN,message)
    # print(m)
    print(m.group(0))