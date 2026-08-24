Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

packet = [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
print("Stage 1 Validation")
Stage 1 Validation
if packet and len(packet) >= 10:
    print("Validation passed. Processing packets")
    else:
        
SyntaxError: invalid syntax

packet = [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
print("Stage 1 Validation")
Stage 1 Validation
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet.....")
else:
    print("Validation failed: packet is empty or too short.")
print("Original packet:", packet)
SyntaxError: invalid syntax
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet.....")
else:
    print("Validation failed: packet is empty or too short.")
print("Original packet:", packet)
SyntaxError: invalid syntax

if packet and len(packet) >= 10:
    print("Validation passed. Processing packet.....")
else:
    print("Validation failed: packet is empty or too short.")

    
Validation passed. Processing packet.....
print("Original packet:", packet)
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
print("\n--- Stage 2: Middle-Out Swap ---")

--- Stage 2: Middle-Out Swap ---
midpoint = len(packet) // 2

front_half = packet[:midpoint]
back_half = packet[midpoint:]

scrambled = back_half[::-1] + front_half

print("Front half:", front_half)
Front half: [5, 12, 0, 8, 21]
print("Back half:", back_half)
Back half: [34, 7, 19, 0, 3]
print("Scrambled", scrambled)
Scrambled [3, 0, 19, 7, 34, 5, 12, 0, 8, 21]

print("Is packet same as front_half?",
      id(packet) == id(front_half))
Is packet same as front_half? False
>>> 
>>> print("\n--- Stage 3: In-Place Correction ---")

--- Stage 3: In-Place Correction ---
>>> 
>>> middle_index = len(scrambled) // 2
>>> 
>>> if type(scrambled[middle_index]) is int:
...     scrambled.insert(middle_index + 1, "SYNC-BIT")
... 
...     
>>> print("After SYNC-BIT insertion:", scrambled)
After SYNC-BIT insertion: [3, 0, 19, 7, 34, 5, 'SYNC-BIT', 12, 0, 8, 21]
>>> 
>>> while 0 in scrambled:
...     scrambled.remove(0)
... 
...     
>>> print("After removing zeors:", scrambled)
After removing zeors: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]
>>> 
>>> print("\n--- Stage 4: Memory Integrity Check ---")

--- Stage 4: Memory Integrity Check ---
>>> 
>>> first, *middle, last = scrambled
>>> 
>>> print("Original packet:", packet)
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
>>> 
>>> print("Final scrambled packet:", scrambled)
Final scrambled packet: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]
>>> 
>>> print("Header:", first)
Header: 3
>>> 
>>> print("Footer:", last)
Footer: 21
>>> 
>>> print("Body length:", len(middle))
Body length: 7
