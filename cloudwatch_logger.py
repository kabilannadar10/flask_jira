import logging
import watchtower
import boto3
import os

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
boto3.setup_default_session(region_name=AWS_REGION)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Log to EC2 (local file)
file_handler = logging.FileHandler('/home/ubuntu/flask_jira/logs/app.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Log to AWS CloudWatch
logger.addHandler(watchtower.CloudWatchLogHandler(
    log_group="JiraLogs",
    stream_name="JiraStream",
))

logger.info("Logging system initialized!")
