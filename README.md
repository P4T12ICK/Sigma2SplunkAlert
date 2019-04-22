# Sigma2SplunkAlert
Converts Sigma detection rules to a Splunk alert configuration.

# Motivation
Many Security Operations Center (SOC) are using scheduled searches for their detection rules. Sigma is the new standard for describing detection rules. Deploying multiple Sigma detection rules into Splunk was a time-consuming task. Sigma2SplunkAlert converts multiple Sigma detection rules into a Splunk savedsearches.conf configuration. Additionally, Sigma2SplunkAlerts supports Splunk alert actions such as Send email or Add to Triggered Alerts. Sigma2SplunkAlerts introduces tokens to use the interesting fields of an alert in the email body.

# How it works
Sigma2SplunkAlert combines Sigma with the power of Jinja2 templating to generate a Splunk savedsearches.conf configuration. 

![text](https://github.com/P4T12ICK/Sigma2SplunkAlert/blob/master/Sigma2SplunkAlert.jpg)

It uses the following inputs:
* folder containing Sigma detection rules
* Sigma configuration file with field names and index mapping (see [Sigma repository](https://github.com/Neo23x0/sigma) for more info)
* Sigma2SplunkAlert configuration file containing Splunk alerts configuration values

and generates a savedsearches.conf configuration. More information about the Sigma2SplunkAlert configuration can be found in the Wiki. 

# Requirements
Sigma2SplunkAlert needs Sigma for converting the Sigma detection rules into Splunk searches. Sigma needs to be installed and part of the environment variables. Furthermore, Python >= 3.5, PyYAML and Jinja2 is needed.

# Usage
````
usage: sigma2splunkalert [-h] [--config CONFIG] [--sigma-config SIGMA_CONFIG]
                         N [N ...]

Convert Sigma rules to Splunk Alerts savedsearches.conf configuration.

positional arguments:
  N                     folder or file containing the Sigma rules

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Sigma2SplunkAlert configuration file
  --sigma-config SIGMA_CONFIG, -sc SIGMA_CONFIG
                        Sigma configuration with field name and index name
                        mapping
````

# Examples
Translate a single Sigma detection rule with the standard configuration:
````
./sigma2splunkalert rules/sysmon_masquerading.yml 
````
Generates the following output:
````
# Generated with Sigma2SplunkAlert 
[Masquerading]
action.email = 1
action.email.include.results_link = 0
action.email.include.view_link = 0 
action.email.subject.alert = Splunk Alert: $name$ 
action.email.to = test@test.de
action.email.message.alert = Splunk Alert $name$ triggered \
List of interesting fields:  \
User: $result.User$ \
Image: $result.Image$ \
CommandLine: $result.CommandLine$  
action.email.useNSSubject = 1
alert.severity = 3
alert.suppress = 0
alert.track = 1
alert.expires = 24h
counttype = number of events
cron_schedule = */10 * * * *
description = Malware often uses well-known windows process names for their malicious process name to avoid detection. This technique is called masquerading.
dispatch.earliest_time = -10m
dispatch.latest_time = now
enableSched = 1
quantity = 0
relation = greater than
request.ui_dispatch_app = detection_rule_repository
request.ui_dispatch_view = search
search = (source="WinEventLog:Microsoft-Windows-Sysmon/Operational" ((EventCode="1" (Image="*\\rundll32.exe" OR Image="*\\svchost.exe" OR Image="*\\smss.exe" OR Image="*\\csrss.exe" OR Image="*\\wininit.exe" OR Image="*\\services.exe" OR Image="*\\lsass.exe" OR Image="*\\lsm.exe" OR Image="*\\winlogon.exe" OR Image="*\\explorer.exe" OR Image="*\\taskhost.exe")) NOT ((Image="*\\Windows\\System32\*" OR Image="*\\Windows\\Syswow64\*"))) NOT ((Image="C:\\Windows\\Explorer.EXE"))) | table User,Image,CommandLine
````

Translates a folder of sigma detection rules to a savedsearches.conf:
````
./sigma2splunkalert ../forks/sigma/rules/windows/sysmon/
````

Translate a folder of Sigma detection rules with a custom Sigma and Sigma2SplunkAlert configuration:
````
./sigma2splunkalert -c config/config.yml -sc sigma_config/splunk-all.yml ../forks/sigma/rules/windows/sysmon/
````

# Next Steps
* Support of recurse into subdirectories
* Improved error handling
* Further use of token

# Credits
This is a private repository developed by Patrick Bareiss (Twitter: [@bareiss_patrick](https://twitter.com/bareiss_patrick)).
