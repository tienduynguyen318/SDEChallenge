# PaytmLabs SDE Challenge

Interface: IMovingAverage defines the data structure for calculating moving average of last n element elements added<br />
Implementation: MovingAverageImpl: provide implementation of the interface IMovingAverage<br />

## Coding Question

Write an interface for a data structure that can provide the moving average of the last N elements added, add elements to the structure and get access to the elements. Provide an efficient implementation of the interface for the data structure

## Design Question

Desgin a Google Analytic like Backend System. We need to provide Google Analytic like services to our customers. Please provide a high level solution design for the backend system. Feel free to choose any open source tools as you want

### What is Google Analytic

Google analytic is a web analytic service that track and report website traffic.

### Requirement and goal of the system

We will focus on the following set of requirement while designing Google Analytic:

#### Functional requirement

1. Site visitor's metadata stored.
2. User should be able view the web traffic and other metrics generated by visitor.

#### Non-functional requirement

1. Handle large write volume: Billions of write events per day.
2. Handle large read/query volumn: Millions of merchants wish to gain insight into their business. Read/Query patterns are time-series related metrics.
3. Provide metrics to customers with at most one hour delay.
4. Run with minimum down time.
5. Have the ability to reprocess historical data in case of bugs in processing logic.

#### Extended requirement

Have the ability to auto scale when traffic increase suddenly

#### Out of scopes

User register for accounts<br />
User authenticate their accounts<br />
Implement UI for user<br />

### Capacity estimation and constraints

#### Traffic estimates

Write: Billions of write event per day -> approximately 1 billion / (24 hours* 3600 seconds) = 12000 write event per second<br />
Read: Assume that an user need to check their website traffic three times a day -> approximately 3 million / (24 hours* 3600 seconds) = 35 read event per second<br />

#### Storage estimates

Assume that 1 KB perwrite event -> approximately 1 KB * 1 billion = 1 Terabyte per day

### High level system design
![alt tag](https://github.com/tienduynguyen318/SDE-Challenge/blob/master/Google%20Analytics.jpg)

### General architecture

#### Backend analytic system use microservice architecture

#### Cluster management: Kubernetes

Kubernetes support cluster management with minimum downtime as it has node auto-repairing<br />
Kubernetes also support auto scaling to met sudden increase in traffic<br />

#### API Gateway/Load Balancer/Service registry: Apache Zookeeper

Zookeeper is our API gateway that also serve as load balancer, service registry and healthcheck<br />

#### Data streaming: Apache Kafka, Apache Spark

Kafka cluster while serve as queue/message bus system with no risk of loss in data with its multiple partitions<br />
Spark streaming use for consumer in speed layer, provide analytic and ETL capabilities for time series data<br />
Kafka streaming for consumer in batch layer<br />

#### Database: Cassandra for writing event, PostgreSQL to store report

Cassandra scale very well with large amount of read and write, support the need to handle billions of write request and millions of read request per day<br />
Cassandra is based on a masterless cluster which support our needs of minimum downtime<br />
PostgreSQL is used to store report<br />

### Component design

Use case: Site visitor visit the website/application
	The snippet in the website create a write event to the API Gateway using Zookeeper<br />
	The API Gateway forward the write event to Write Service<br />
	The Write Service push write event to Queue (Kafka Stream) and return<br />
	Queue will slit the message to be consume by Spark Stream and Kafka Stream<br />
	Spark will process the data and store in PostgreSQL for quick update<br />
	Kafka will process the data in batch that run once a day to update all the data into PostgreSQL<br />
Use case: Merchant view the web traffic and other metrics generate by site visitor<br />
