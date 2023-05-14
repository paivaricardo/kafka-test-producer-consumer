from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='18.214.223.254:9092')
    print("Inicio do Produtor Local Kafka")
    producer.send("planto-iot-sensores-kafka", str("Teste do Produtor Local - kafka-python").encode('utf-8'), key=str("hello").encode('utf-8'))
    print("Envia mensagem de teste para o Kafka")
    producer.flush()
