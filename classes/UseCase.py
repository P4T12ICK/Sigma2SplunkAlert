
import subprocess
from subprocess import DEVNULL
from .TriggeredAlert import TriggeredAlert
from .EMail import EMail
from .SummaryIndex import SummaryIndex


class UseCase:

    def __init__(self, sigma_uc, config, splunk_search):
        # mandatory values
        self.title = sigma_uc["title"]
        self.description = sigma_uc["description"]
        self.app = config["app"]
        self.cron_schedule = config["cron_schedule"]
        self.earliest_time = config["earliest_time"]
        self.latest_time = config["latest_time"]

        # splunk search
        self.splunk_search = splunk_search

        # optional values
        if 'level' in sigma_uc:
            self.level = sigma_uc['level']
        if 'status' in sigma_uc:
            self.status = sigma_uc['status']
        if 'tags' in sigma_uc:
            self.tags = sigma_uc['tags']  # array
        if 'author' in sigma_uc:
            self.author = sigma_uc['author']
        if 'falsepositives' in sigma_uc:
            self.falsepositives = sigma_uc['falsepositives']
        if 'references' in sigma_uc:
            self.references = sigma_uc['references']
        if 'allow_skew' in config:
            self.allow_skew = config["allow_skew"]
        if 'schedule_window' in config:
            self.schedule_window = config["schedule_window"]

        # default values
        self.alert_email = 0

        # alert actions
        if 'email' in config["alert_action"]:
            self.alert_email = 1
            self.email = EMail(config["alert_action"]["email"], sigma_uc)
        if 'summary_index' in config["alert_action"]:
            self.summary_index = SummaryIndex(config["alert_action"]["summary_index"])
