class EMail:

    def  __init__(self, to, subject, message, result_link, view_link, include_search, include_trigger, include_trigger_time, inline, sendcsv, sendpdf, sendresults):
        self.to = to
        self.subject = subject
        self.message = message
        self.result_link = result_link
        self.view_link = view_link
        self.include_search = include_search
        self.include_trigger = include_trigger
        self.include_trigger_time = include_trigger_time
        self.inline = inline
        self.sendcsv = sendcsv
        self.sendpdf = sendpdf
        self.sendresults = sendresults

