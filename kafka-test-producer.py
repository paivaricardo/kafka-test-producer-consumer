from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='18.214.223.254:9092')
    print("Inicio do Produtor Local Kafka")
    producer.send("planto-iot-sensores-kafka", "Teste do Produtor Local".encode('utf-8'))
    print("Envia mensagem de teste para o Kafka")
