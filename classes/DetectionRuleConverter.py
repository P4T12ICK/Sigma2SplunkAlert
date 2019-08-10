import subprocess
from subprocess import DEVNULL


class DetectionRuleConverter(object):

    @staticmethod
    def convertSigmaRule(sigma_config_path, rule_path):
        command = ['sigmac -t splunk -c ' + sigma_config_path + ' ' + rule_path]
        sigma_search = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=DEVNULL, universal_newlines=True)
        sigma_search_output = sigma_search.stdout

        if sigma_search.returncode != 0:
            print("# Failure converting the Sigma File: " + rule_path)
            return "Converter Failure"
        else:
            return sigma_search_output

    @staticmethod
    def addToSummaryIndex(search, sigma2splunkalertconfig, sigma_rule):
        if "summary_index" in sigma2splunkalertconfig["alert_action"]:
            if "tags" in sigma_rule:
                summaryindexconfig = sigma2splunkalertconfig["alert_action"]["summary_index"]
                search = search[:-1] + ' | collect index=' + \
                    summaryindexconfig["name"] + ' '
                if ("enrich_tags" in summaryindexconfig) or ("enrich_level" in summaryindexconfig):
                    search = search + 'marker="'
                    if "enrich_tags" in summaryindexconfig:
                        for tag in sigma_rule["tags"]:
                            search = search + "sigma_tag=" + tag + ","
                    if "enrich_level" in summaryindexconfig:
                        search = search + "level=" + sigma_rule["level"]
                    if search[-1:] == ",":
                        search = search[:-1]
                    search = search + '"'
        return search

    @staticmethod
    def performSearchTransformation(transformations, search, sigma_rule):
        for trans in transformations:

            # Search Transformation to add whitelist in front of table or transforming command (for better whitelisting)
            if trans == "add_whitelist_in_front":
                file_name = sigma_rule["title"] + "_whitelist.csv"
                file_name = file_name.replace(" ", "_")
                file_name = file_name.replace("/", "_")
                file_name = file_name.replace("(", "")
                file_name = file_name.replace(")", "")
                if '| table' in search:
                    tableindex = search.find('| table')
                    search = search[:tableindex] + "| search NOT [| inputlookup " + \
                        file_name + "] " + search[tableindex:]
                elif '| stats' in search:
                    statsindex = search.find('| stats')
                    search = search[:statsindex] + "| search NOT [| inputlookup " + \
                        file_name + "] " + search[statsindex:]
                else:
                    search = search[:-1] + " | search NOT [| inputlookup " + file_name + "] "

            # Search Transformation to add whitelist at the end of the search
            if trans == "add_whitelist":
                file_name = sigma_rule["title"] + "_whitelist.csv"
                file_name = file_name.replace(" ", "_")
                file_name = file_name.replace("/", "_")
                file_name = file_name.replace("(", "")
                file_name = file_name.replace(")", "")
                search = search[:-1] + " | search NOT [| inputlookup " + file_name + "] "

            # Search Transformation to add host field
            if trans == "add_host_field":
                if '| table' in search:
                    search = search[:-1] + ",host "

            # Search Transformation to add source field
            if trans == "add_source_field":
                if '| table' in search:
                    search = search[:-1] + ",source "

            # Search Transformation to add sourcetype field
            if trans == "add_sourcetype_field":
                if '| table' in search:
                    search = search[:-1] + ",sourcetype "

            # Search Transformation to add transforming_command
            if trans == "add_transforming_command":
                if not ('| table' in search):
                    search = search[:-1] + " | stats values(*) AS * by _time "

            # Add Custom Search Transformations here

        return search
