import logging
import watchtower
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Log to EC2 (local file)
file_handler = logging.FileHandler('/var/log/myapp.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Log to AWS CloudWatch
logger.addHandler(watchtower.CloudWatchLogHandler(
    log_group="MyAppLogs",
    stream_name="MyAppStream",
    boto3_session=boto3.Session()
))

logger.info("✅ Logging system initialized!")
