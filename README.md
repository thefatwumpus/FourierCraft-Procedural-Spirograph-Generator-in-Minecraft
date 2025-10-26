# FourierCraft: Procedural Spirograph Generator in Minecraft

A Python program that uses Fourier-based spirograph equations to generate, animate, and remove intricate mathematical patterns inside Minecraft via the RCON protocol.  

Features multiple customizable designs with varied harmonic ratios, real-time pattern rendering, and dynamic cleanup for iterative exploration of mathematical art.

## Features
- Generates spirograph curves using parametric equations  
- Live Minecraft rendering  
- Experiment with varied ratios and block types  
- Removes old patterns to make room for new ones  
- Uses the classic spirograph equations:
x = (R + r) * cos(t) + p * cos(((R + r)/r) * t)
y = (R + r) * sin(t) + p * sin(((R + r)/r) * t)

Where:  
- **R** = radius of fixed circle  
- **r** = radius of rolling circle  
- **p** = pen offset distance  
- **t** = time parameter controlling rotation

## Requirements
- Minecraft Java Edition  
- RCON enabled in `server.properties`  
- Python 3.12
- enable-rcon=true
- Set your RCON password in server.properties (e.g., rcon.password=MySecret123)
- Make sure rcon.port=25575

## Developed By
**Wesley**  
Inspired by **Frost3ch** and the beauty of spirographs.


