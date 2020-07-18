#!/bin/bash

# Steps to configure and install Cassandra

echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y cassandra

sudo systemctl stop cassandra

# To enable Thrift RPC (needed by cassandra_ros)
sudo sed -i 's/start_rpc: false/start_rpc: true/g' /etc/cassandra/cassandra.yaml

# To change partitioner to ByteOrdered (needed by cassandra_ros)
sudo mkdir -p /var/lib/cassandra2
sudo chown -R cassandra:cassandra /var/lib/cassandra2

sudo sed -i 's/lib\/cassandra/lib\/cassandra2/g' /etc/cassandra/cassandra.yaml
sudo sed -i 's/partitioner: org.apache.cassandra.dht.Murmur3Partitioner/partitioner: org.apache.cassandra.dht.ByteOrderedPartitioner/g' /etc/cassandra/cassandra.yaml

sudo systemctl start cassandra
