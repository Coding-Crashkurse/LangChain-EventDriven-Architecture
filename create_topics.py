from confluent_kafka.admin import AdminClient, NewTopic

def create_topic(topic_name):
    admin = AdminClient({'bootstrap.servers': 'kafka:29092'})

    new_topic = NewTopic(topic_name, num_partitions=3, replication_factor=1)

    fs = admin.create_topics([new_topic])

    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} has been created.")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

create_topic("raw-emails")
create_topic("cancellation-emails")
create_topic("review-emails")
create_topic("inquiry-emails")
