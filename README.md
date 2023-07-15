# Email Classification and Processing Service

This project provides a service for categorizing and processing different types of emails, leveraging the power of Confluent Kafka and OpenAI's language model.

## Services

1. **send_mails.py**: A Python script that sends out emails. These are categorized into three types: order cancellations, reviews, and inquiries. These messages are sent to the 'raw-emails' Kafka topic.

2. **email_classifier**: This service consumes the 'raw-emails' Kafka topic and uses OpenAI's language model to classify the type of each email. It then sends the emails to their corresponding Kafka topics based on their classifications.

3. **order_cancellation_processor, review_processor, inquiry_processor**: These are services that consume from their respective Kafka topics ('order-cancellation-emails', 'review-emails', 'inquiry-emails') and perform specific processing tasks on the incoming emails of that type.

The system is deployed and orchestrated using Docker, as specified by the `docker-compose.yaml` file. All necessary environment variables are stored in the `.env` file.

## Usage

To run the system, make sure Docker is installed and use the following command:

```bash
docker-compose up
```

To send out emails, run the `send_mails.py` script.

U need an OpenAI API-key to run this. Rename the `.env.example` to `.env` and provide your API Key
