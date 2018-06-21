import re

class DefaultIntent:
    pass

class StartReportIntent:
    pass

class EndReportIntent:
    pass

def evaluateIntent(text):
    START_REPORT_PATTERN = 'รายงาน|แจ้งข่าว'
    END_REPORT_PATTERN = 'จบการรายงาน'
    
    m = re.search(END_REPORT_PATTERN,text)
    if m is not None:
        return EndReportIntent()

    m = re.search(START_REPORT_PATTERN,text)
    if m is not None:
        return StartReportIntent()


    return DefaultIntent()
