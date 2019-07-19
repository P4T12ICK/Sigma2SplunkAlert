class EMail:

    def __init__(self, email_config, sigma_uc):
        # mandatory values
        self.to = email_config["to"]
        self.subject = email_config["subject"]
        self.message = email_config["message"]

        # optional values
        if "result_link" in email_config:
            self.result_link = email_config["result_link"]
        if "view_link" in email_config:
            self.view_link = email_config["view_link"]
        if "include_search" in email_config:
            self.include_search = email_config["include_search"]
        if "include_trigger" in email_config:
            self.include_trigger = email_config["include_trigger"]
        if "include_trigger_time" in email_config:
            self.include_trigger_time = email_config["include_trigger_time"]
        if "inline" in email_config:
            self.inline = email_config["inline"]
        if "sendcsv" in email_config:
            self.sendcsv = email_config["sendcsv"]
        if "sendpdf" in email_config:
            self.sendpdf = email_config["sendpdf"]
        if "sendresults" in email_config:
            self.sendresults = email_config["sendresults"]

        # Generate text block based on fields value in Sigma Use Case
        self.generateFieldsBlock(sigma_uc)

        # Generate tag block based on tags in Sigma Use Case
        self.generateMitreTagBlock(sigma_uc)

    def generateFieldsBlock(self, sigma_uc):
        if 'fields' in sigma_uc:
            field_block = ''
            for field_value in sigma_uc['fields']:
                field_block = field_block + '|' + field_value + ': $result.' + field_value + '$ '

            self.field_block = field_block

    def generateMitreTagBlock(self, sigma_uc):
        if 'tags' in sigma_uc:
            mitre_block = '|Mitre ATT&CK ID: '
            for tag_value in sigma_uc['tags']:
                if tag_value.startswith('attack.t'):
                    mitre_block = mitre_block + tag_value[7:] + ' '
            mitre_block = mitre_block + '|Mitre ATT&CK Tactic: '
            for tag_value in sigma_uc['tags']:
                if not (tag_value.startswith('attack.t') or tag_value.startswith('attack.g') or tag_value.startswith('attack.s')) and tag_value.startswith('attack.'):
                    mitre_block = mitre_block + tag_value[7:] + ' '
            mitre_block = mitre_block + '|'
            self.mitre_block = mitre_block
