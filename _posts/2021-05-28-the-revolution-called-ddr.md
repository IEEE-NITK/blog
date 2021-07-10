---
layout: post
title: "The Revolution called DDR"
date: 2021-05-28 00:00:00
image: '/assets/img/'
description: "If you have ever done some decent amount of research before buying any phone, laptop, graphics card, prebuilt PC, or even built your PC you would have come across terms such as LPDDR, DDR, or GDDR when the product's RAM or VRAM is concerned. All of these terms have DDR in common them, but what is DDR?"
tags:
- IEEE NITK
- Diode
- DDR
- RAM
- Digital Systems
categories:
- Diode
github_username: 'krutideepanpanda'
---

## DDR

### DDR SDRAM

![img1](/blog/assets/img/revolution-called-ddr/Fig-2-Figure-Clocking-1-300x89.jpg)

DDR memory stands for **Double Data Rate memory**, this is actually called DDR SDRAM but since it has become so widespread we just say DDR. To understand how this works and why is this so important lets go back to simple memory components such as latches. Latches and Flip -Flops store data at either the rising or falling edge of the clock cycle, and this was the case with the initial **SDRAM (Synchronous Dynamic Random Access Memory)**. 

What makes DDR SDRAM so different is that it does the same functions as SDRAM but at both rising and falling edges of the clock cycle. Doing so effectively doubled the transfer rate (measured in transfers per second). The first generation of DDR memory had transfer rates between **266-400 MT/s (Mega Transfers per Second)**. All these RAMs have some prefetch buffer associated with them which acts as a cache for the RAM. DDR had a 2bit prefetch buffer, which is double that of SDRAM. We usually see DDR memory as DDR4 in laptops and desktops. This is the 4th generation of DDR memory. 

### DDR2

The second-generation DDR2 memory could operate the external bus at twice the speeds of its previous generation while maintaining the same internal clock. It had a prefetch buffer of 4bits.

### DDR3

A major drawback of DDR2 was that it consumed a lot of power than DDR1 causing it to heat up frequently. This was dealt with DDR3, it consumed 40% less power than DDR2 and added 2 extra functions of **ASR (Automatic Self-Refresh)** and **SRT (Self-Refresh Temperature)** which allowed for the memory to control its refresh rate according to temperature variations. DDR3 has a prefetch buffer of 8bits.

### DDR4

DDR4 is the current generation of DDR memory and has even lower operating voltages and higher transfer rates. DDR4 has something called **Bank Groups**, it has 4 bank groups allowing to process 4 data in a clock cycle. DDR4 also offers better signal integrity due to functions such as DBI (Data Bus Inversion), CRC (Cyclic Redundancy Check), and CA parity.

### Bank groups

Previous generational improvements were brought about by increasing but having too high of a pre-fetch is also not ideal. As per the figure below, if the trends were to continue then DDR4 would have had a 16N prefetch. This isn't ideal so what we do is divide it into 2 8N groups, each such group is considered to be a bank group.

![img2](/blog/assets/img/revolution-called-ddr/prev.jpg)

![img3](/blog/assets/img/revolution-called-ddr/present.jpg)

A comparison of all the generations of DDR memory is shown in the table below. We can see that through various generations DDR becomes faster and more power-efficient.

![img4](/blog/assets/img/revolution-called-ddr/ddr-table.png)

## LPDDR

In layman's terms, LPDDR can be considered as DDR but for mobile devices where power consumption is a major factor. Unlike PCs, mobile devices don't have the liberty to draw as much power as they need. They are restricted to manage with whatever the battery can provide while also ensuring that they don't gulp it all at once, instead they have to sip it slowly to maintain good battery life for the device.

LPDDR4 is the mobile equivalent of DDR4 memory, with a few key differences. LPDDR4 has dual 16-bit channels resulting in a 32-bit total bus per DIMM (DIMM or Dual In-line Memory module could be just considered as RAM ). In comparison, DDR4 has 64-bit channels per DIMM. At the same time, LPDDR4 has a wider prefetch than DDR4. This means that **to consume low power LPDDR4 sacrifices some of the bandwidth**, this results in battery life of anywhere between 8-10 hours. However, the real-world battery life depends on how it is implemented and varies from device to device. LPDDR4 is in no way slower than DDR4 and data rates of 3200 MT/s aren't hard to come by.

## GDDR

GDDR stands for Graphics Double Data Rate and can be seen in VRAMs of graphics cards, with the standards such as GDDR6, GDDR6X, and GDDR5 being pretty common in modern cards. In design, it similar to DDR but has several differences that make GDDR have much better performance. 

**Differences between GDDR and DDR -**

- GDDR has a wider memory bus as compared to DDR and thus has a higher bandwidth
- GDDR can request as well as receive in the same clock cycle unlike DDR
- GDDR is much more power-efficient and gives off less heat. This allows for keeping higher performance modules with just a simple cooling solution

The latest standard of GDDR is GDDR6X and is significantly faster than previous generations. Usually, when we send or receive data we do so in two power levels 1 or 0, but GDDR6X uses four power levels which are 00, 01, 10, and 11. This doubles the amount of data present in each cycle. Each 8Gb (1GB) chip of GDDR6X memory has the bandwidth to transfer 84GB/s. 

## Resources

- [What is DDR (Double Data Rate) Memory and SDRAM memory?](https://www.microcontrollertips.com/understanding-ddr-sdram-faq/)
- [What is the difference between SDRAM, DDR1, DDR2, DDR3 and DDR4?](https://www.transcend-info.com/Support/FAQ-296)
- [What is GDDR?](https://www.computerhope.com/jargon/g/gddr.htm)
- [What is the Difference Between DirectX 11 and DirectX 12?](https://www.hardwaretimes.com/what-is-the-difference-between-ddr4-and-lpddr4-lpddr4x/)
- [What is DIMM?](https://www.enterprisestorageforum.com/storage-hardware/what-is-dimm.html)
- [What is GDDR6X?](https://www.technipages.com/what-is-gddr6x)
- [DDR4 Bank Groups](https://www.synopsys.com/designware-ip/technical-bulletin/ddr4-bank-groups.html)
