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
