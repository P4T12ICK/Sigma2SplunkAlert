class SummaryIndex:

    def __init__(self, summary_index_config):
        self.name = summary_index_config["name"]
        if 'enrich_tags' in summary_index_config:
            self.enrich_tags = summary_index_config["enrich_tags"]
        if 'enrich_level' in summary_index_config:
            self.enrich_level = summary_index_config["enrich_level"]
