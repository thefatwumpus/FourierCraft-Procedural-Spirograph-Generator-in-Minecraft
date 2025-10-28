# FourierCraft: Procedural Spirograph Generator in Minecraft

# Reflection

While developing this project, I was inspired by Frost3ch's use of advanced Fourier transforms to visualize models inside of Minecraft.
I reached out to the creator for insights, and though I haven't gotten a reply yet, I used their work to guide the creation of my own simplified version.
This version can only create hypotrochoid patterns and cannot replicate the ideal theorem that all periodic functions can be represented by sin and cos.
The main goal of the project itself was passion inspired, a way to help me step into the world of programming by combining my love of math with visualization.

# What I Learned

Through this project, I strengthened my Python programming skills, obtained a clearer view of how the Fourier series functions, and made a creative outlet for my love of mathematics.

# Features

- Generates, animates, and removes intricate mathematical spirograph patterns inside Minecraft via Python and the RCON protocol.

- Multiple customizable designs with varied harmonic ratios, real-time pattern rendering, and dynamic cleanup for iterative exploration of mathematical art.

- Generates spirograph curves using parametric equations.

- Live Minecraft rendering.

- Experiment with varied ratios and block types.

- Removes old patterns to make room for new ones.

- Uses the classic spirograph equations:

x = (R + r) * cos(t) + p * cos(((R + r)/r) * t)
y = (R + r) * sin(t) + p * sin(((R + r)/r) * t)

# Where:
R = radius of fixed circle
r = radius of rolling circle
p = pen offset distance
t = time parameter controlling rotation

# Requirements
- Minecraft Java Edition
- RCON enabled in server.properties
- Python 3.12
- enable-rcon=true
- Set your RCON password in server.properties (e.g., rcon.password=MySecret123)
- Make sure rcon.port=25575

# Developed By
Wesley
Inspired by Frost3ch and the beauty of spirographs.
