import re

class DefaultIntent:
    pass

class StartReportIntent:
    pass

class EndReportIntent:
    pass

class ListReportIntent:
    pass

class ViewReportIntent:
    def __init__(self,id):
        self.id = id

def evaluateIntent(text):
    START_REPORT_PATTERN = 'รายงาน|แจ้งข่าว'
    END_REPORT_PATTERN = 'จบการรายงาน'
    LIST_REPORT_PATTERN = 'รายงานทั้งหมด'
    VIEW_REPORT_PATTERN = '(ดูรายงาน)( )(?P<id>\d+)'

    m = re.search(VIEW_REPORT_PATTERN,text)
    if m is not None:
        # print(m)
        # print(m.group('id'))
        id = m.group('id')
        return ViewReportIntent(id)

    m = re.search(LIST_REPORT_PATTERN,text)
    if m is not None:
        return ListReportIntent()

    m = re.search(END_REPORT_PATTERN,text)
    if m is not None:
        return EndReportIntent()

    m = re.search(START_REPORT_PATTERN,text)
    if m is not None:
        return StartReportIntent()


    return DefaultIntent()

if __name__ == '__main__':
    m = evaluateIntent('ขอดูรายงาน 2')
    print(m)