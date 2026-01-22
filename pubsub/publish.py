from google.cloud import pubsub_v1

project_id = "core-pubsub-service"
topic_id = "test-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

message = "hey whatsup ".encode("utf-8")

future = publisher.publish(topic_path, message)

print("Published message ID:", future.result())
