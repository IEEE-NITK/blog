---
layout: post
title: "ESP8266 microcontrollers"
author_github: ShashankHollaS
date: 2020-04-24 23:06:00
image: '/assets/img/'
description: 'This article is about how to achieve wireless communication between two ESP8266 microcontrollers '
tags:
- ESP8266
- Microcontrollers
categories:
- Diode
github_username: 'ShashankHollaS'
---
**[WIRELESS COMMUNICATION BETWEEN TWO ESP8266
MICROCONTROLLERS]{.underline}**

**Now a days we can turn off the lights and fans in our house , sitting
in the office by just clicking a button on the phone. But how is this
possible? Answer for this is Wireless Communication. There are many
types in Wireless Communication but this article focuses only on the
communication between two NodeMCU's which gives solution for the above
problem.**

**NodeMCU** is an open
source [IoT](https://en.wikipedia.org/wiki/Internet_of_Things) platform. It
includes [firmware](https://en.wikipedia.org/wiki/Firmware) which runs
on
the [ESP8266](https://en.wikipedia.org/wiki/ESP8266) [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi) [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) (System
On Chip) from Espressif Systems, and hardware which is based on the
ESP-12 module.

**[About ESP8266:]{.underline}**

The ESP8266 WiFi Module is a self contained SOC with integrated TCP/IP
protocol stack that can give any microcontroller access to your WiFi
network. The ESP8266 is capable of either hosting an application or
offloading all Wi-Fi networking functions from another application
processor. Each ESP8266 module comes pre-programmed with an AT command
set firmware, meaning, you can simply hook this up to your Arduino
device and get about as much WiFi-ability as a WiFi Shield offers (and
that's just out of the box)! The ESP8266 module is an extremely cost
effective board with a huge, and ever growing, community.

This module has a powerful enough on-board processing and storage
capability that allows it to be integrated with the sensors and other
application specific devices through its GPIOs with minimal development
up-front and minimal loading during runtime. Its high degree of on-chip
integration allows for minimal external circuitry, including the
front-end module, is designed to occupy minimal PCB area. The ESP8266
supports APSD for VoIP applications and Bluetooth co-existance
interfaces, it contains a self-calibrated RF allowing it to work under
all operating conditions, and requires no external RF parts.

**[Scenario]{.underline}:**

There are two Microcontrollers (**NodeMCU's**). One is server and other
is client. Client sends a request and server acts based on the request
(either it can perform some task or give back some information to the
client). Here the client will send a request to turn on or off an LED

WiFi capabilities for NodeMCU comes from the **[ESP8266]{.underline}**
WiFi module present in it.

A NodeMCU can be coded in two modes, Station mode and Soft Access Point
(Soft AP) mode.

**Who is Who?**

Devices that connect to Wi-Fi networks are called **stations (STA)**.
Connection to Wi-Fi is provided by an **access point(AP**), that acts as
a hub for one or more stations. The access point on the other end is
connected to a wired network. An access point is usually integrated with
a router to provide access from a Wi-Fi network to the internet.

ESP8266 modules can operate as a station, so we can connect it to the
Wi-Fi network. It can also operate as a soft access point (soft-AP), to
establish its own Wi-Fi network. When the ESP8266 module is operating as
a soft access point, we can connect other stations to the ESP module.
ESP8266 is also able to operate as both a station and a soft access
point mode. This provides the possibility of building e.g. mesh
networks.

**[NodeMCU as an AP:]{.underline}**

:![](media/image1.jpeg){width="5.364583333333333in"
height="1.4583333333333333in"}

Set the SSID and password of your Access point. They can be anything but
[should contain at least 8 characters.]{.underline} Here we have added
password for a secured communication but it can be done without password
as well.

![](media/image2.jpeg){width="4.739583333333333in"
height="2.8854166666666665in"}

Start the access point. Here myIP is the IP address of the AP. LED is
connected to pin 13 or D7.

![](media/image3.jpeg){width="6.447916666666667in"
height="1.2708333333333333in"}

Here the first print statement prints the number of stations connected
to our access point. Then read the request sent by the client.

![](media/image4.jpeg){width="4.385416666666667in"
height="2.2291666666666665in"}

Based on the request either turn on the LED or turn it off.

**[NODEMCU as a Station:]{.underline}**

![](media/image5.jpeg){width="5.083333333333333in" height="1.65625in"}

Host contains the IP address of the AP(Access point).

Here the ssid and password should be same as the AP because we have to
connect this Station to the WiFi of the AP.(Here these names appear to
be contradicting. But it is OK as they are just identifiers.

![](media/image6.jpeg){width="3.6666666666666665in"
height="3.6666666666666665in"}

Connect the Station to the WiFi of the AP. The program won't proceed
further until the wifi is connected.

![](media/image7.jpeg){width="5.875in" height="3.2916666666666665in"}

Connect to the host and send the request. Here we follow the standard
HTTP GET request format. We are continuously sending requests with a
delay of 3 seconds.

**[OUTPUTS:]{.underline}**

. ![](media/image8.jpeg){width="2.4583333333333335in"
height="1.0416666666666667in"}

This is the output ( from the Serial monitor) of the Access Point.

![](media/image9.png){width="4.40625in" height="1.9166666666666667in"}

This is from the Serial monitor of the station.

[Further references:]{.underline}

1.  <https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html>

2.  <https://www.esp8266.com/> This is the ESP8266 community forum.

3.  <http://www.tinyosshop.com/datasheet/ESP8266%20Command%20Doc.pdf>
    This PDF contains information about AT Commands
