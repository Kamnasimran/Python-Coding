def parse_payload(raw_packet: list, delimiter: str, /, *, correction_offset: int = 0) -> tuple:
    status_tokens = raw_packet[2].split(delimiter)
    corrected_sensors = [
        value if "ERROR" in status_tokens else value + correction_offset
        for value in raw_packet[1][:]
    ]
    return raw_packet[0], corrected_sensors


raw_packet = [501, [12.5, 13.0, 11.8], "NOMINAL|CALIBRATED"]

result = parse_payload(raw_packet, "|", correction_offset=2)

print("Test 1 ->", result[0], result[1])

assert raw_packet[1] == [12.5, 13.0, 11.8]
assert id(raw_packet[1]) != id(result[1])

print("Test 1 side-effect assertions passed.")


raw_packet = [502, [9.0, 8.5], "ERROR|SENSOR_FAULT"]

result = parse_payload(raw_packet, "|", correction_offset=5)

print("Test 2 ->", result[0], result[1])

assert raw_packet[1] == [9.0, 8.5]
assert id(raw_packet[1]) != id(result[1])

print("Test 2 side-effect assertions passed.")


raw_packet = [503, [1.0, 2.0], "NOMINAL"]

result = parse_payload(raw_packet, "|")

print("Test 3 (default offset) ->", result[0], result[1])


try:
    parse_payload(raw_packet=raw_packet, delimiter="|")
except TypeError as e:
    print("Test 4 passed. TypeError raised as expected:", e)


try:
    parse_payload(raw_packet, "|", 2)
except TypeError as e:
    print("Test 5 passed. TypeError raised as expected:", e)


raw_packet = [504, [10.0, 20.0], "NOMINAL|CALIBRATED|LOW POWER"]

result = parse_payload(raw_packet, "|", correction_offset=5)

print("Edge Case 1 ->", result)


raw_packet = [504, [], "NOMINAL"]

result = parse_payload(raw_packet, "|", correction_offset=5)

print("Edge Case 2 ->", result)


raw_packet = [505, [4.0, 6.0], "NOMINAL"]

result1 = parse_payload(raw_packet, "|", correction_offset=0)
result2 = parse_payload(raw_packet, "|")

print("Edge Case 3:", result1)
print("Edge Case 3:", result2)

assert result1 == result2
