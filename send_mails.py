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

emails = [
    """
    Dear Support Team,

    I'm writing to cancel my order number #123456. After reconsideration, I realized that the product doesn't meet my needs as I initially thought. I understand your company's policy regarding order cancellations and I apologize for any inconvenience this might cause.

    I kindly ask you to confirm my cancellation request and refund the payment to my original payment method. Thank you very much for your assistance in this matter.

    Best regards,
    Customer
    """,

    """
    Hello,

    I recently purchased the Deluxe Kitchen Gadget from your online store and I'm loving it. It's been a great addition to my kitchen and has made cooking much more efficient and enjoyable. The quality of the product is impressive and it's extremely easy to use.

    I would highly recommend your product to anyone who enjoys cooking. I'm looking forward to trying out more products from your catalog. Keep up the great work!

    Best,
    Happy Customer
    """,

    """
    Hi,

    I visited your store last week and I was intrigued by your new range of products. However, I have some questions about the New Tech Gadget before I decide to purchase it.

    How long is the battery life? Does it come with a warranty? And can it be connected to my smartphone to control it remotely?

    I would appreciate it if you could provide this information. Thank you for your help.

    Regards,
    Interested Customer
    """,
]

for email in emails:
    p.produce('raw-emails', email, callback=delivery_report)

    p.flush()

    time.sleep(3)
