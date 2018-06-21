import re
messageList = [
    'ขอรายงานครับ',
    'เริ่มต้นการรายงานครับ',
    'ขอแจ้งข่าวครับ',
    'สวัสดีจ้า'
]

START_REPORT_PATTERN = 'รายงาน|แจ้งข่าว'
for message in messageList:
    m = re.search(START_REPORT_PATTERN,message)
    # print(m)
    print(message,':', m.group(0) if m is not None else '')
    