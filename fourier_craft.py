import socket
import struct
import math
import time

class MinecraftRCON:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(('localhost', 25575))
        packet = struct.pack('<ii', 1, 3) + b'python\x00\x00'
        self.sock.send(struct.pack('<i', len(packet)) + packet)
        self.sock.recv(4096)
    
    def command(self, cmd):
        packet = struct.pack('<ii', 1, 2) + cmd.encode() + b'\x00\x00'
        self.sock.send(struct.pack('<i', len(packet)) + packet)
        return self.sock.recv(4096)
    
    def draw_line(self, x1, y1, z1, x2, y2, z2, block_type):
        """Draw a solid line between two points"""
        dx = x2 - x1
        dz = z2 - z1
        distance = max(abs(dx), abs(dz))
        
        if distance == 0:
            return
            
        for i in range(int(distance) + 1):
            t = i / distance
            x = int(x1 + dx * t)
            z = int(z1 + dz * t)
            self.command(f"setblock {x} {y1} {z} {block_type}")
    
    def remove_pattern(self, pattern_points, center_x, center_y, center_z):
        """Remove a pattern by replacing all its blocks with AIR"""
        print("   Removing pattern...")
        points_removed = 0
        for block_x, block_z in pattern_points:
            self.command(f"setblock {block_x} {center_y} {block_z} air")
            points_removed += 1
            if points_removed % 100 == 0:
                time.sleep(0.1)
        print(f"    Removed {points_removed} blocks")

mc = MinecraftRCON()

print(" VARIED Fourier Patterns - User Choice for Final Pattern")
print()

# Use world spawn coordinates
center_x, center_y, center_z = 0, 70, 0

print(f"Drawing at: X={center_x}, Y={center_y}, Z={center_z}")
print("Each pattern has DIFFERENT mathematical parameters")
print("You choose whether to keep the final pattern")
print()

# VARIED patterns with different mathematical properties
patterns = [
    # (R, r, p, points, block_type, description, speed_divisor)
    (25, 15, 12, 800, "sea_lantern", "Flower Pattern (5/3 ratio)", 25),      # 25/15 = 5/3
    (28, 16, 8, 900, "glowstone", "Star Pattern (7/4 ratio)", 20),           # 28/16 = 7/4
    (30, 20, 15, 1200, "ochre_froglight", "Large Loops (3/2 ratio)", 30),    # 30/20 = 3/2
    (24, 18, 10, 1000, "pearlescent_froglight", "Dense Pattern (4/3 ratio)", 15)  # 24/18 = 4/3
]

previous_pattern_points = None

for pattern_idx, (R, r, p, points, block_type, description, speed_divisor) in enumerate(patterns):
    print()
    print(f" PATTERN {pattern_idx + 1}: {description}")
    print(f"   Math: R={R}, r={r}, p={p} (Ratio: {R}/{r} = {R/r})")
    print(f"   Block: {block_type}")
    
    # REMOVE previous pattern by replacing its blocks with AIR
    if previous_pattern_points is not None:
        print("   Removing previous pattern...")
        mc.remove_pattern(previous_pattern_points, center_x, center_y, center_z)
        time.sleep(1)
        print("    Previous pattern removed!")
    
    # Mark center
    mc.command(f"setblock {center_x} {center_y} {center_z} diamond_block")
    mc.command(f"say  Drawing: {description}")
    
    print(f"   Drawing {points} points...")
    
    previous_point = None
    current_pattern_points = set()
    
    for i in range(points):
        t = 2 * math.pi * i / speed_divisor  # Different speed for each pattern
        
        # Spirograph equations
        x = (R + r) * math.cos(t) + p * math.cos(((R + r) / r) * t)
        z = (R + r) * math.sin(t) + p * math.sin(((R + r) / r) * t)
        
        block_x = int(center_x + x)
        block_z = int(center_z + z)
        
        # Store this point for later removal
        current_pattern_points.add((block_x, block_z))
        
        # Place the point
        mc.command(f"setblock {block_x} {center_y} {block_z} {block_type}")
        
        # Connect to previous point with consistent lines
        if previous_point is not None:
            prev_x, prev_z = previous_point
            # Draw line and store all line points
            line_dx = block_x - prev_x
            line_dz = block_z - prev_z
            line_distance = max(abs(line_dx), abs(line_dz))
            
            for j in range(int(line_distance) + 1):
                t_line = j / line_distance
                line_x = int(prev_x + line_dx * t_line)
                line_z = int(prev_z + line_dz * t_line)
                current_pattern_points.add((line_x, line_z))
                mc.command(f"setblock {line_x} {center_y} {line_z} {block_type}")
        
        previous_point = (block_x, block_z)
        
        if i % 150 == 0:
            print(f"     Progress: {i}/{points} points")
            time.sleep(0.1)
    
    print(f"    Pattern {pattern_idx + 1} complete!")
    previous_pattern_points = current_pattern_points  # Store for next removal
    
    # Wait for user before replacing with next pattern (except for final pattern)
    if pattern_idx < len(patterns) - 1:
        print()
        input("   Press Enter to REMOVE this pattern and draw next one...")
    else:
        print()
        print("    FINAL PATTERN COMPLETE")
        print("   You now have a choice:")
        print("   1. Keep this pattern (it will remain visible)")
        print("   2. Remove this pattern (clean up everything)")
        print()
        
        while True:
            choice = input("   Enter 'keep' or 'remove': ").lower().strip()
            if choice in ['keep', 'remove']:
                break
            print("   Please enter 'keep' or 'remove'")
        
        if choice == 'remove':
            print("   Removing final pattern...")
            mc.remove_pattern(previous_pattern_points, center_x, center_y, center_z)
            mc.command("setblock 0 70 0 air")  # Remove center marker too
            mc.command("say  All patterns cleaned up!")
            print("    Final pattern removed!")
        else:
            mc.command("say  Fourier art complete! Pattern saved!")
            print("    Final pattern kept! Enjoy your Fourier art! ")

print()
print(" PROGRAM COMPLETE!")
if choice == 'keep':
    print(" Your Fourier art remains at (0, 70, 0)")
else:
    print(" Everything has been cleaned up")
