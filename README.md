# Sigma2SplunkAlert
Converts Sigma detection rules to a Splunk alert configuration.

# Motivation
Many Security Operations Center (SOC) are using scheduled searches for their detection rules. Sigma is the new standard for describing detection rules. Deploying multiple Sigma detection rules into Splunk was a time-consuming task. Sigma2SplunkAlert converts multiple Sigma detection rules into a Splunk savedsearches.conf configuration. Additionally, Sigma2SplunkAlerts supports Splunk alert actions such as Send Email and Summary Index. Sigma2SplunkAlert introduces tokens to use the interesting fields of an alert in the email body. Furthermore, Splunk Search transformations are used to adapt the Splunk Search with customizations such as adding an whitelist or another custom Splunk command.

# How it works
Sigma2SplunkAlert combines Sigma with the power of Jinja2 templating to generate a Splunk savedsearches.conf configuration.

![text](https://github.com/P4T12ICK/Sigma2SplunkAlert/blob/master/images/Sigma2SplunkAlert.jpg)

It uses the following inputs:
* folder containing Sigma detection rules
* Sigma configuration file with field names and index mapping (see [Sigma repository](https://github.com/Neo23x0/sigma) for more info)
* Sigma2SplunkAlert configuration file containing Splunk alerts configuration values

and generates a savedsearches.conf configuration. More information about the Sigma2SplunkAlert configuration can be found in the Wiki.

# Requirements
Sigma2SplunkAlert needs Sigma for converting the Sigma detection rules into Splunk searches. Sigma needs to be installed and part of the environment variables. Furthermore, Python >= 3.5, PyYAML and Jinja2 is needed.
The Sigma2SplunkAlert was tested with Splunk version 7.2.5. If you find some incompatibility to previous Splunk versions, open an issue and I will try to add the support as soon as possible.

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
./sigma2splunkalert rules/sysmon_mimikatz_detection_lsass.yml
````
Generates the following output:
````
# Generated with Sigma2SplunkAlert
[Mimikatz Detection LSASS Access]
action.email = 1
action.email.subject.alert = Splunk Alert: $name$
action.email.to = test@test.de
action.email.message.alert = Splunk Alert $name$ triggered  \
List of interesting fields:  \
EventCode: $result.EventCode$ \
TargetImage: $result.TargetImage$ \
GrantedAccess: $result.GrantedAccess$ \
ComputerName: $result.ComputerName$  \
title: Mimikatz Detection LSASS Access status: experimental \
description: Detects process access to LSASS which is typical for Mimikatz (0x1000 PROCESS_QUERY_ LIMITED_INFORMATION, 0x0400 PROCESS_QUERY_ INFORMATION, 0x0010 PROCESS_VM_READ) \
references: ['https://onedrive.live.com/view.aspx?resid=D026B4699190F1E6!2843&ithint=file%2cpptx&app=PowerPoint&authkey=!AMvCRTKB_V1J5ow'] \
tags: ['attack.t1003', 'attack.s0002', 'attack.credential_access'] \
author:  \
date:  \
falsepositives: ['unknown'] \
level: high
action.email.useNSSubject = 1
alert.severity = 1
alert.suppress = 0
alert.track = 1
alert.expires = 24h
counttype = number of events
cron_schedule = */10 * * * *
description = Detects process access to LSASS which is typical for Mimikatz (0x1000 PROCESS_QUERY_ LIMITED_INFORMATION, 0x0400 PROCESS_QUERY_ INFORMATION, 0x0010 PROCESS_VM_READ)
dispatch.earliest_time = -10m
dispatch.latest_time = now
enableSched = 1
quantity = 0
relation = greater than
request.ui_dispatch_app = sigma_hunting_app
request.ui_dispatch_view = search
search = (source="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode="10" TargetImage="C:\\windows\\system32\\lsass.exe" GrantedAccess="0x1410") | table EventCode,TargetImage,GrantedAccess,ComputerName,host | search NOT [| inputlookup Mimikatz_Detection_LSASS_Access_whitelist.csv] | collect index=threat-hunting marker="sigma_tag=attack.t1003,sigma_tag=attack.s0002,sigma_tag=attack.credential_access,level=high"
````

Translates a folder of sigma detection rules to a savedsearches.conf:
````
./sigma2splunkalert ../sigma/rules/windows/sysmon/
````

Translate a folder of Sigma detection rules with a custom Sigma and Sigma2SplunkAlert configuration:
````
./sigma2splunkalert -c config/config.yml -sc sigma_config/splunk-all.yml ../forks/sigma/rules/windows/sysmon/
````

# Next Steps
* Improved error handling

# Credits
This is a private repository developed by Patrick Bareiss (Twitter: [@bareiss_patrick](https://twitter.com/bareiss_patrick)).
