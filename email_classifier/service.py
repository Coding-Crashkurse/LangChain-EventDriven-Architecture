import logging
from confluent_kafka import Consumer, Producer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()}")

def classify_email(email):
    if "order cancellation" in email:
        return "Order cancellation"
    elif "review" in email:
        return "Review"
    else:
        return "Inquiry"

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'email-classifier',
    'auto.offset.reset': 'earliest'
})

p = Producer({'bootstrap.servers': 'kafka:9092'})

c.subscribe(['raw-emails'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logger.error(f"Consumer error: {msg.error()}")
        continue

    email = msg.value().decode('utf-8')
    category = classify_email(email)
    logger.info(f"Classified email: {category}")

    topic_map = {
        "Order cancellation": "order-cancellation-emails",
        "Review": "review-emails",
        "Inquiry": "inquiry-emails",
    }

    p.produce(topic_map[category], email, callback=delivery_report)
    p.flush()
