import os
from typing import Tuple

# A chunk boundary can fall in the middle of a record because the file is
# read as fixed-size byte blocks rather than complete lines. A leftover
# buffer keeps the incomplete final part of each chunk and joins it with
# the next chunk before processing, so no record is incorrectly split.

def process_log_stream(
    file_path: str, chunk_size: int, /
) -> Tuple[int, float]:

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Target path '{file_path}' not found."
        )

    valid_count = 0
    running_sum = 0.0
    leftover = b""
    found_sentinel = False

    with open(file_path, "rb") as file_obj:

        for chunk in iter(
            lambda: file_obj.read(chunk_size), b""
        ):

            leftover += chunk

            complete_lines = leftover.split(b"\n")

            leftover = complete_lines[-1]

            for raw_line in complete_lines[:-1]:

                line = raw_line.decode("utf-8").strip()

                if line == "END OF LOG":
                    found_sentinel = True
                    continue

                fields = line.split(",")

                if len(fields) != 3:
                    continue

                value = fields[2].strip()

                if value == "":
                    continue

                try:
                    sensor_value = float(value)
                except ValueError:
                    continue

                valid_count += 1
                running_sum += sensor_value

    if leftover:
        line = leftover.decode("utf-8").strip()

        if line == "END OF LOG":
            found_sentinel = True

        else:
            fields = line.split(",")

            if len(fields) == 3:

                value = fields[2].strip()

                if value != "":
                    try:
                        sensor_value = float(value)
                        valid_count += 1
                        running_sum += sensor_value
                    except ValueError:
                        pass

    if not found_sentinel:
        print("Warning: file may be truncated.")

    if valid_count == 0:
        mean_value = 0.0
    else:
        mean_value = running_sum / valid_count

    return valid_count, mean_value


if __name__ == "__main__":

    sample_file = "sample_telemetry.txt"

    sample_data = """2026-01-01T00:00:01,SENSOR_A,14.5
2026-01-01T00:00:02,SENSOR_B,NaN_READING
2026-01-01T00:00:03,SENSOR_C,
2026-01-01T00:00:04,SENSOR_A,16.2
2026-01-01T00:00:05,MALFORMED_ROW_TOO_FEW_FIELDS
2026-01-01T00:00:06,SENSOR_B,15.0
END OF LOG
"""

    with open(sample_file, "w") as file_obj:
        file_obj.write(sample_data)

    result_1 = process_log_stream(sample_file, 1)
    print("Chunk size 1:", result_1)

    result_2 = process_log_stream(sample_file, 1000)
    print("Chunk size 1000:", result_2)

    assert result_1 == result_2

    assert result_1[0] == 3

    assert abs(
        result_1[1] - 15.233333333333334
    ) < 0.000001

    print("Main test passed")

    truncated_file = "truncated_telemetry.txt"

    truncated_data = """2026-01-01T00:00:01,SENSOR_A,14.5
2026-01-01T00:00:02,SENSOR_B,NaN_READING
2026-01-01T00:00:04,SENSOR_A,16.2
"""

    with open(truncated_file, "w") as file_obj:
        file_obj.write(truncated_data)

    truncated_result = process_log_stream(
        truncated_file, 1
    )

    print("Truncated file:", truncated_result)

    assert truncated_result[0] == 2

    print("Edge Case 1 passed")

    chunk_result = process_log_stream(
        sample_file, 1
    )

    assert chunk_result == (
        3,
        15.233333333333334
    )

    print("Edge Case 2 passed")

    missing_file = "file_that_does_not_exist.txt"

    try:
        process_log_stream(missing_file, 10)
    except FileNotFoundError:
        print("Edge Case 3 passed")

    empty_file = "zero_valid_records.txt"

    empty_data = """BAD
WRONG
NOT_A_NUMBER
END OF LOG
"""

    with open(empty_file, "w") as file_obj:
        file_obj.write(empty_data)

    zero_result = process_log_stream(
        empty_file, 1
    )

    print("Zero valid records:", zero_result)

    assert zero_result == (0, 0.0)

    print("Edge Case 4 passed")

    os.remove(sample_file)
    os.remove(truncated_file)
    os.remove(empty_file)

    print("All tests passed")
