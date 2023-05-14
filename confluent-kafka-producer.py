from confluent_kafka import Producer
import socket

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

if __name__ == '__main__':
        conf = {'bootstrap.servers': "18.214.223.254:9092"}


        producer = Producer(conf)
        print("Inicio do Produtor Local Kafka - Confluent Kafka")

        producer.produce('planto-iot-sensores-kafka', key='hello', value='Teste com Confluent Kafka2', callback=acked)
        print("Enviada mensagem de teste para o Kafka")
        producer.flush()
        print("Servidor finalizado")