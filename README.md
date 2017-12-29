### Monitorization and control system of the production of Salicornia in the Ria de Aveiro

> Technological evolution has always been present in the life of humanity from its beginnings to the present, in a relationship that has grown and continues to grow at an amazing rate. The paradigm, transversal to any economic activity, consists in resource optimization with the objective to maximize production through the technological evolution. In agricultural production this is not exception, and for this reason, the monitoring mechanisms of the parameters that influence the quantity and quality of production are becoming indispensable and preponderant in the success of the business. Thus, in the cultivation of Salicornia, a plant that grows in the Ria de Aveiro, is also essential create a system that allows monitor and help to control the optimal conditions of cultivation of the specie.

> The main goal of this thesis was the project and the implementation of an information system for the control and monitoring of the Salicornia production in collaboration with a company of the region of Aveiro and the Department of Biology of the University of Aveiro. The developed system is a low-cost and effective solution for data acquisition, processing and storage. In addition, this system is structured to be applied in other contexts beyond the Salicornia cultivation.

#### Hardware simulation 

#### All repositories

* [sali-report](https://github.com/ruipoliveira/sali-report)
* [sali-dashboard](https://github.com/ruipoliveira/sali-dashboard)
* [sali-deploy](https://github.com/ruipoliveira/sali-deploy)
* [sali-hardware](https://github.com/ruipoliveira/sali-hardware)
* [sali-surveillance](https://github.com/ruipoliveira/sali-surveillance)

#### Overview 



![alt text](https://github.com/ruipoliveira/sali-sensor/blob/master/resources/comm.png)


##### Arduino Nano 

* arduino code to receive data from sensors; interaction with bluetooth module

![alt text](https://github.com/ruipoliveira/sali-sensor/blob/master/resources/arduino.png)

* legend: Arduino Nano (A), Módulo Bluetooth HC-06 (B), LED (C), Sensor de temperatura TTC 104 NTC (D), Sensor de luminosidade GL5528 (foto-resistência) (E), Sensor para nível de água (F)


##### Raspberry Pi 3

* python script for bluetooth 4.0 communication with Bluetooth module HC-06; send data to API. 


#### Author
* Rui Oliveira (ruipedrooliveira@ua.pt)

University of Aveiro, 2017
