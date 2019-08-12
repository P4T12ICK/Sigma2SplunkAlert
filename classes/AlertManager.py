class AlertManager:
    
    def __init__(self, alertmanager_config, sigma_uc):
        # mandatory values
        if 'auto_previous_resolve' in alertmanager_config:
            self.auto_previous_resolve = alertmanager_config['auto_previous_resolve']
        else:
            self.auto_previous_resolve = 0
        if 'auto_subsequent_resolve' in alertmanager_config:
            self.auto_subsequent_resolve = alertmanager_config['auto_subsequent_resolve']
        else:
            self.auto_subsequent_resolve = 0
        if 'auto_suppress_resolve' in alertmanager_config:
            self.auto_suppress_resolve = alertmanager_config['auto_suppress_resolve']
        else:
            self.auto_suppress_resolve = 0
        if 'auto_ttl_resove' in alertmanager_config:
            self.auto_ttl_resove = alertmanager_config['auto_ttl_resove']
        else:
            self.auto_ttl_resove = 0
        
        # optional values
        if 'title' in alertmanager_config:
            self.title = alertmanager_config['title']
        if "display_fields" in alertmanager_config:
            self.display_fields = alertmanager_config["display_fields"]
        if "tags" in alertmanager_config:
            self.tags = alertmanager_config["tags"]
        if "auto_assign_owner" in alertmanager_config:
            self.auto_assign_owner = alertmanager_config["auto_assign_owner"]
        if "append_incident" in alertmanager_config:
            self.append_incident = alertmanager_config["append_incident"]
        if "urgency" in alertmanager_config:
            self.urgency = alertmanager_config["urgency"]
        if "impact" in alertmanager_config:
            self.impact = alertmanager_config["impact"]
        if "category" in alertmanager_config:
            self.category = alertmanager_config["category"]
        if "subcategory" in alertmanager_config:
            self.subcategory = alertmanager_config["subcategory"]
        if "notification_scheme" in alertmanager_config:
            self.notification_scheme = alertmanager_config["notification_scheme"]
            