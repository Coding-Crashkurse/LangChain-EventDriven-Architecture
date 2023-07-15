import logging
from confluent_kafka import Producer
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()}")

p = Producer({'bootstrap.servers': 'localhost:9092'})

email_types = ["order cancellation", "review", "inquiry"]

for i in range(10):
    email = f"This is a {email_types[i % 3]} email {i}"

    logger.info(f"Sending email: {email}")

    p.produce('raw-emails', email, callback=delivery_report)

    p.flush()

    time.sleep(3)
