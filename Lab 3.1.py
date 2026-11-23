Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"]

]

shutdown_triggered = False

for batch_id in range(len(telemetry_stream)):
    batch = telemetry_stream[batch_id]

    
range(4)
range(0, 4)

    print("--- Auditing Batch", batch_id, ":", batch, "---")
    
SyntaxError: unexpected indent
    print("--- Auditing Batch", batch_id, ":", batch, "---")
    
SyntaxError: unexpected indent
telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"]

]

shutdown_triggered = False

for batch_id in range(len(telemetry_stream)):
    batch = telemetry_stream[batch_id]
    
SyntaxError: multiple statements found while compiling a single statement

telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"]
]

shutdown_triggered = False

for batch_id in range(len(telemetry_stream)):
    batch = telemetry_stream[batch_id]

    
print("--- Auditing Batch", batch_id, ":", batch, "---")
--- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
for reading in batch:
    if reading == "STOP":
        print("Emergency Shutdown at Batch", batch_id)
        shutdown_triggered = True
        break
    if reading == "ERR":
        print("Noise ignored at Batch", batch_id, ("ERR)")
        continue
    
SyntaxError: '(' was never closed
telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"]
... ]
... 
... shutdown_triggered = False
... 
... for batch_id in range(len(telemetry_stream)):
...     batch = telemetry_stream[batch_id]
... 
...     
... print("--- Auditing Batch", batch_id, ":", batch, "---")
... --- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
... for reading in batch:
...     if reading == "STOP":
...         print("Emergency Shutdown at Batch", batch_id)
...         shutdown_triggered = True
...         break
...     if reading == "ERR":
...         print("Noise ignored at Batch", batch_id, ("ERR")")
...         continue
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> for reading in batch:
...     if reading == "STOP":
...         print("Emergency Shutdown at Batch", batch_id)
...         shutdown_triggered = True
...         break
...     if reading == "ERR":
...         print("Noise ignored at Batch", batch_id, ("ERR"))
...         continue
...     if isinstance(reading, (int, float)) and reading > 35.0:
...         print("Anomaly Detected at Batch", batch_id, ":", reading)
... 
...         
Emergency Shutdown at Batch 3
>>> if shutdown_triggered:
...     break
SyntaxError: 'break' outside loop
>>> 
=========================================== RESTART: C:/Users/skamn/Downloads/Coding for AI Assignment 3.1.py ===========================================
--- Auditing Batch 0 : [22.5, 23.0, 22.8] ---
--- Auditing Batch 1 : [25.1, 'ERR', 24.9] ---
Noise ignored at Batch 1 (ERR)
--- Auditing Batch 2 : [30.2, 35.5, 40.1] ---
Spike Detected at Batch 2 : 5.300000000000001
Anomaly Detected at Batch 2 : 35.5
Anomaly Detected at Batch 2 : 40.1
--- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
Emergency Shutdown at Batch 3

=========================================== RESTART: C:/Users/skamn/Downloads/Coding for AI Assignment 3.1.py ===========================================
--- Auditing Batch 0 : [22.5, 23.0, 22.8] ---
Aduit Complete: No system-wide failures
--- Auditing Batch 1 : [25.1, 'ERR', 24.9] ---
Noise ignored at Batch 1 (ERR)
Aduit Complete: No system-wide failures
--- Auditing Batch 2 : [30.2, 35.5, 40.1] ---
Spike Detected at Batch 2 : 5.300000000000001
Anomaly Detected at Batch 2 : 35.5
Anomaly Detected at Batch 2 : 40.1
Aduit Complete: No system-wide failures
--- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
Emergency Shutdown at Batch 3

=========================================== RESTART: C:/Users/skamn/Downloads/Coding for AI Assignment 3.1.py ===========================================
--- Auditing Batch 0 : [22.5, 23.0, 22.8] ---
Aduit Complete: No system-wide failures
--- Auditing Batch 1 : [25.1, 'ERR', 24.9] ---
Noise ignored at Batch 1 (ERR)
Aduit Complete: No system-wide failures
--- Auditing Batch 2 : [30.2, 35.5, 40.1] ---
Spike Detected at Batch 2 : 5.300000000000001
Anomaly Detected at Batch 2 : 35.5
Anomaly Detected at Batch 2 : 40.1
Aduit Complete: No system-wide failures
--- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
Emergency Shutdown at Batch 3

=========================================== RESTART: C:/Users/skamn/Downloads/Coding for AI Assignment 3.1.py ===========================================
--- Auditing Batch 0 : [22.5, 23.0, 22.8] ---
--- Auditing Batch 1 : [25.1, 'ERR', 24.9] ---
Noise ignored at Batch 1 (ERR)
--- Auditing Batch 2 : [30.2, 35.5, 40.1] ---
Spike Detected at Batch 2 : 5.3
Anomaly Detected at Batch 2 : 35.5
Anomaly Detected at Batch 2 : 40.1
--- Auditing Batch 3 : [22.0, 22.1, 'STOP'] ---
Emergency Shutdown at Batch 3
