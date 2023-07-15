import logging
from confluent_kafka import Consumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'inquiry-processor',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['inquiry-emails'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logger.error(f"Consumer error: {msg.error()}")
        continue

    logger.info(f"Received inquiry email: {msg.value().decode('utf-8')}")
