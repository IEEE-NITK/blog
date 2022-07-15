---
layout: post
title: "Cosmic Bit Flip"
author_github: harishA3
date: 2022-07-15 00:00:00
description: 'A bit flip is a change in a bit of the computer memory  from 0 to 1 or vice versa. Bit Flips can be caused by many factors,one of them bein Cosmic rays.This blog talks about Cosmic Bit Flips and why it is essential in the design of Avionic Systems.'
tags:
- IEEE NITK
- Blog
- Cosmic Bit Flip
categories:
- Piston
github_username: 'harishA3'
---

# Cosmic Bit Flip

## Abstract

Has your laptop or PC ever crashed into a blue screen,just like the one shown below.

![image](/blog/assets/img/cosmic-bit-flip/image-1.png)

Have you ever wondered what the reason behind the system crash could be. Computers are employed everywhere today, and in some critical areas, such as a spacecraft, having the system crash could have quite unpleasant consequences.
A likely reason for the system crash can be Cosmic Bit Flip. Spacecraft must be protected from Bit Flips to operate safely.

## What is Cosmic Bit Flip?

Digital data is stored as a sequence of 0s and 1s. Each 0 or 1 is called a bit. A bit-flip is an _inadvertent change_ of state of a bit that is different from its initial state.Cosmic ray is a highly energetic atomic nucleus or other particle travelling through space at a speed approaching that of light. Cosmic radiation from exploding stars outside our solar system can cause electronics to malfunction by flipping bits in a computer's memory,causing glitches.

![image](/blog/assets/img/cosmic-bit-flip/image-2.png)

Cosmic Bit Flips, on rare occasions, cause a single bit of information to “flip”(single bit flip). This can be enough to force a computer to reboot, knock a passenger jet out of its autopilot mode

## Single-Evnet Upset(SEU)

A single event upset (SEU) is a bit flip in a memory element of a semiconductor device.The result of upsets is data corruption. Many systems can tolerate some level of soft errors(A temporary error that is not caused by a persistent hardware fault, typically being remedied by rebooting the system).
  
In 2013, a speedrunner of the Super Mario 64 video game using the Nintendo 64 console experienced a glitch which teleported Mario higher up in the "Tick Tock Clock" stage. This has been hypothesized to have been caused by an SEU, flipping the least significant bit of Mario’s height's most significant byte. Click [here](https://www.youtube.com/watch?v=bhBf5crp0i8) to watch the video for the same.

## SEU in Aircraft Electronics

Over the last ten years,the occurrence of single-event upset (SEU) in aircraft electronics has evolved from a series of interesting anecdotal incidents to accepted fact. Once avionics SEU was shown to be an actual effect, it had to be dealt with in avionics designs. The major concern is in random access memories (RAMs), both static (SRAMs) and dynamic (DRAMs), because these microelectronic devices contain the largest number of bits, but other parts, such as microprocessors, are also potentially susceptible to upset.The most common way of dealing with SEU in RAM’s is by means of error detection and correction (EDAC). 

Today, a number of commercially available computer systems for upgrading military aircraft to incorporate EDAC in their designs are available. This trend of building EDAC directly into the design is likely to continue as larger quantities of memory (from megabits to gigabits) are incorporated into avionic(electronic equipment fitted in an aircraft) systems.  

## Fatal Crashes of the Boeing 737 MAX 

October 29, 2018: Lion Air Flight 610, a 737 MAX 8, on a flight from Jakarta, Indonesia to Pangkal Pinang, Indonesia, crashed into the sea 13 minutes after takeoff, with 189 people on board the aircraft: 181 passengers (178 adults and three children), as well as six cabin crew and two pilots. All on board died.

![image](/blog/assets/img/cosmic-bit-flip/lionairflightcrash.png)

March 10, 2019: Ethiopian Airlines Flight 302, a 737 MAX 8, on a flight from Addis Ababa, Ethiopia to Nairobi, Kenya, crashed six-minutes after takeoff; all 157 people aboard (149 passengers and 8 crew members) died. The plane was only four months old at the time of the accident.

![image](/blog/assets/img/cosmic-bit-flip/EthiopianAirlinesFlight302Crash.png)

After two deadly crashes of Boeing’s 737 MAX and the ensuing heavy criticism of the FAA for its limited oversight of the jet’s original certification, the agency has been reevaluating and recertifying Boeing’s updated flight-control systems.

## Boeing 737 MAX Redesign

Boeing announced on June 26,2019 that a new potential flaw had been discovered on the MAX — this time in a microprocessor in the jet’s flight-control computer. the specific fault that showed up has “never happened in 200 million flight hours on this same flight-control computer in [older model] 737 NGs.”

In sessions in a Boeing flight simulator in Seattle, two FAA engineering test pilots, typically ex-military test pilots, and a pilot from the FAA’s Flight Standards Aircraft Evaluation Group (AEG), typically an ex-airline pilot, set up a session to test 33 different scenarios that might be sparked by a rare, random microprocessor fault in the jet’s flight-control computer. This was standard testing that’s typically done in certifying an airplane, but this time it was deliberately set up to produce specific effects similar to what happened on the Lion Air and Ethiopian flights.

The fault occurs when bits inside the microprocessor are randomly flipped from 0 to 1 or vice versa(Bit Flip). This is a known phenomenon that can happen due to cosmic rays striking the circuitry. Electronics inside aircraft are particularly vulnerable to such radiation because they fly at high altitudes and high geographic latitudes where the rays are more intense.

for example, a value of 1 on a single bit might indicate that the jet’s wing flaps are up, while a 0 would mean they are down. A value of 1 on a different bit might tell the computer that the MAX’s problematic flight-control system called MCAS(Maneuvering Characteristics Augmentation System) is engaged, while a 0 would indicate it is not. FAA regulations require that Bit Flips be accounted for in the design of all critical electronics on board aircraft.

During the tests, 33 different scenarios were artificially induced by deliberately flipping five bits on the microprocessor, an error rate determined appropriate by prior analysis. For these simulations, the five bits flipped were chosen in light of the two deadly crashes to create the worst possible combinations of failures to test if the pilots could cope.

In one scenario, the bits chosen first told the computer that MCAS was engaged when it wasn’t. This had the effect of disabling the cut-off switches inside the pilot-control column, which normally stop any uncommanded movement of the horizontal tail if the pilot pulls in the opposite direction.

A second bit was chosen to make the horizontal tail, also known as the stabilizer, swivel upward uncommanded by the pilot, which has the effect of pitching the plane’s nose down. Other bits were flipped to add three more complications.
Even though the MCAS system that pushed the nose down on the two crash flights had not been activated, these changes in essence gave the FAA test pilots in the simulator an emergency situation similar to what transpired on those flights.

Boeing could have just rewritten the software governing what functions are monitored within the flight-control computer to eliminate this failure scenario. Instead, it’s decided to make a much more radical software redesign, one that will not only fix this problem but make the MAX’s entire flight-control system — including MCAS — more reliable, according to three sources. This change means the flight-control system will take input from both of the airplane’s flight computers and compare their outputs. This goes beyond what Boeing had previously decided to do, which is to adjust the MCAS software so that it took input from two angle of attack sensors instead of one.

## Conclusion

Cosmic Bit Flips need to be considered during the desinging of Avionic Systems. The aircraft softwares need to be built in way such that the probable number of bit flips that can occur in the aircraft software should not affect it's flight.
  
EDAC Systems need to be incorported into avionics to prevent SEUs(Single event upsets)in the RAM or the microprocessor installed in the airplane. There is a need for Stringent testing of airplanes to prevent crashes.

## Recourses

- [What are bit flips and how are spacecraft protected from them](https://www.scienceabc.com/innovation/what-are-bit-flips-and-how-are-spacecraft-protected-from-them.html#:~:text=Cosmic%20Bit%2DFlip&text=Again%2C%20as%20the%20name%20suggests,been%20stripped%20of%20their%20electrons)
- [software redesign of Boeing’s 737 MAX flight controls](https://www.seattletimes.com/business/boeing-aerospace/newly-stringent-faa-tests-spur-a-fundamental-software-redesign-of-737-max-flight-controls/)
- [List of accidents and incidents involving the Boeing 737](https://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_the_Boeing_737)