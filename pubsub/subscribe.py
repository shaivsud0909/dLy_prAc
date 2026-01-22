from google.cloud import pubsub_v1

project_id = "core-pubsub-service"
subscription_id = "test-sub"

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(project_id, subscription_id)


def callback(message):
    print("Received:", message.data.decode())
    message.ack()


print("Listening for messages...")

subscriber.subscribe(sub_path, callback=callback)

while True:
    pass
