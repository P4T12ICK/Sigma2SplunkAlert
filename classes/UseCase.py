
from .TriggeredAlert import TriggeredAlert
from .EMail import EMail

class UseCase:

    def __init__(self, sigma_uc, config):
	# add checks for missing values with try 
        self.title = sigma_uc["title"]
        self.description = sigma_uc["description"]
	
	# add checks for missing values
	self.scheduled_search = config["scheduled_search"]
	self.app = config["config"]
        self.cron_schedule = config["cron_schedule"]
	self.earliest_time = config["earliest_time"]
	self.latest_time = config["latest_time"]
	self.schedule_window = config["schedule_window"]

    
    def addSigmaUCValues(self, sigma_uc):
	# add checks for missing values with try 
        self.title = sigma_uc["title"]
        self.description = sigma_uc["description"]
	
	if 'level' in sigma_uc:
            self.level = sigma_uc['level']
	if 'status' in sigma_uc:
            self.status = sigma_uc['status']
        if 'tags' in sigma_uc:
            self.tags = sigma_uc['tags'] #array
        if 'author' in sigma_uc:
            self.author = sigma_uc['author']
        if 'falsepositives' in sigma_uc:
            self.falsepositives = sigma_uc['falsepositives']
	
    def addConfigValues(self, sigma_uc, config):
        # add checks for missing values
        self.scheduled_search = config["scheduled_search"]
        self.app = config["config"]
        self.cron_schedule = config["cron_schedule"]
        self.earliest_time = config["earliest_time"]
        self.latest_time = config["latest_time"]
        self.schedule_window = config["schedule_window"]
      
        if 'email' in converter_config["alert_action"]: 
            self.email = EMail(converter_config["alert_action"]["email"], sigma_uc)

        # to do

    def  __init__(self, title, description, search, cron_schedule, earliest_time, latest_time, app):
        self.title = title
        self.description = description
        self.search = search
        self.cron_schedule = cron_schedule
        self.earliest_time = earliest_time
        self.latest_time = latest_time
        self.app = app
        self.alert_TriggeredAlert = 0
        self.alert_EMail = 0

    def addStatusValue(self, status):
        self.status = status

    def addReferencesValue(self, reference_array):
        self.references = ''
        for reference in reference_array:
            self.references = self.references + reference + ' '

    def addTagsValue(self, tags_array):
        self.tags = ''
        for tag in tags_array:
            self.tags = self.tags + tag + ' '

    def addAuthorValue(self, author):
        self.author = author

    def addDateValue(self, date):
        self.date = date

    def addFalsepositivesValue(self, falsepositives_array):
        self.falsepositives = ''
        if isinstance(falsepositives_array,list):
            for falsepositive in falsepositives_array:
                self.falsepositives = self.falsepositives + falsepositive + ' '
        else:
            self.falsepositives = falsepositives_array

    def addLevelValue(self, level):
        self.level = level

    def addTriggeredAlert(self, alert):
        self.alert_TriggeredAlert = 1
        self.alert = TriggeredAlert(alert)

    def addEmailAlert(self, to, subject, message, result_link, view_link, include_search, include_trigger, include_trigger_time, inline, sendcsv, sendpdf, sendresults):
        self.alert_EMail = 1
        self.email = EMail(to, subject, message, result_link, view_link, include_search, include_trigger, include_trigger_time, inline, sendcsv, sendpdf, sendresults)

    def addFieldsBlock(self, string):
        self.fieldBlock = string

    def addMitreBlock(self, string):
        self.mitreBlock = string

    def addSummaryIndex(self, attack_ID, index_name):
        self.attack_ID = attack_ID
        self.index_name = index_name



