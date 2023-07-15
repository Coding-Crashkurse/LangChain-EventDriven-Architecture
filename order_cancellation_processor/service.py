import logging
from confluent_kafka import Consumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'order-cancellation-processor',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['order-cancellation-emails'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logger.error(f"Consumer error: {msg.error()}")
        continue

    logger.info(f"Received order cancellation email: {msg.value().decode('utf-8')}")
