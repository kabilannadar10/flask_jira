Automated JIRA Ticket Creation from GitHub Comments: A Complete Overview
This document outlines the steps and functionalities for automating the creation of JIRA tickets from GitHub issues using a Python application hosted on an EC2 instance. The process integrates GitHub, JIRA, and AWS CloudWatch to streamline the workflow.



1. Issue Reporting and Tracking Process
Bug Reporting:

QE (Quality Engineers) or developers report bugs or issues, either minor (e.g., configuration mistakes) or genuine (requiring major fixes).
GitHub Repository:

Issues or bugs are tracked in a GitHub repository, where the development team regularly checks and categorizes them.
Manual Workflow:

Issues are checked manually, typically once or twice a week, by the development team to determine if they require major attention.
Minor or invalid issues are closed, while genuine issues are escalated for further action.



2. Manual JIRA Ticket Creation
Manual Effort:

Developers manually create JIRA tickets for valid issues. They need to send the issue description along with the reported issue.
Automation Need:

The process is manual and time-consuming, requiring automation to save time and reduce human error.



3. Solution: Automation with GitHub, JIRA, and EC2
Objective:

To automate the creation of JIRA tickets from GitHub issues using Python scripting.
GitHub and JIRA Integration:

GitHub serves as the source for issue reporting, and JIRA is used for issue management and tracking.
Python Scripting:

Python is chosen for its flexibility, dynamic nature, and extensive module support (such as requests and boto3) to interact with APIs and automate workflows.



4. Key Steps for Automation
4.1 Setting Up the Webhook
GitHub Webhook:
A webhook is created in the GitHub repository to connect to the EC2 instance.
The webhook sends issue-related information in JSON format to the EC2 instance.
4.2 EC2 Instance and Python Scripting
EC2 Instance:

The EC2 instance runs a Python Flask application to process the incoming data from GitHub.
API Calls:

The Python application makes API calls to JIRA using the received JSON data to create JIRA tickets automatically.
4.3 Flask Application
Flask Setup:
A Flask app is created with the route /jira to receive and process the data sent from GitHub.
4.4 JIRA API Integration
JIRA Setup:
Create a JIRA account, choose a Scrum template, and access the JIRA API documentation for creating tickets.
Use the preferred language (Python) for interacting with the JIRA API.
Use a secure API token for authentication.
4.5 Security Configuration
Inbound Rules:

Ensure that EC2 security groups allow traffic on port 5000 (for Flask app) via inbound rules.
Elastic IP:

Set up an Elastic IP (EIP) to ensure the EC2 instance has a stable IP address.



5. Enhancements in the Workflow
Multiple Project Integration:
A significant enhancement was made to handle multiple project issues in a single GitHub comment. This allows creating multiple JIRA tickets in different projects with a single webhook trigger.



6. CloudWatch Logging Setup
6.1 IAM Role Creation
IAM Role:
Create an IAM role named CloudWatchAgentServerRole with the necessary permissions: CloudWatchAgentServerPolicy and CloudWatchLogsFullAccess.
6.2 Log Group and Stream Setup
CloudWatch Configuration:
A CloudWatch log group and streams are created, with details stored in config.py.
Logs are imported into cloudwatch_logger.py to allow logging both locally and in CloudWatch.
6.3 CloudWatch Integration
CloudWatch Log Handler:
Logs are sent to AWS CloudWatch using watchtower's CloudWatchLogHandler for centralized log management.



7. Environment Configuration
7.1 API Token Setup
JIRA API Token:
Create an API token in JIRA and set it as an environment variable (API_TOKEN) on the EC2 instance to authenticate the Python application.
7.2 Region Configuration
AWS Region:
Set the AWS region in the EC2 instance by adding AWS_REGION to the ~/.bashrc file.



8. Summary
This automated workflow enables seamless creation of JIRA tickets from GitHub issues, reducing manual effort and streamlining the issue tracking process.
The solution is enhanced with CloudWatch for centralized logging and monitoring.
The EC2 instance, Python scripts, Flask, JIRA, GitHub, and AWS services work together to provide an efficient, automated solution for issue tracking and management.
