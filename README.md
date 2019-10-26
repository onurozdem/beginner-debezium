#  beginner-debezium

This repository includes docker-compose yaml, python script(script create sample data and insert to database) for beginner-level debezium installation. In addition, the technology topology that can be used with Nifi is shared with png.


# Installation
- ### Up Docker with Single Node Zookeeper and Kafka 

      $ docker-compose -f debezium-basic-mysql.yml up


- ### Up Docker with Multi Node Zookeeper and Kafka 

      $ docker-compose -f debezium-with-multi_zk_kafka_cluster-mysql.yml up  

# Insert Sample Data to MySql
    $ python debezium-python-data-faker-mysql.py   
