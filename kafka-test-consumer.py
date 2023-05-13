from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer("planto-iot-sensores-kafka", bootstrap_servers='18.214.223.254:9092', auto_offset_reset='earliest')
    print("Inicio do Consumidor Local Kafka")
    try:
        for message in consumer:
            print(message)
    except Exception as e:
        print("Error:", e)