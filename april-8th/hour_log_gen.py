import random
import os
from datetime import datetime, timedelta

# CONFIG
LINES_PER_FILE = 110000
HOURS_TO_GENERATE = 5   # change this (e.g., 24 for full day)
OUTPUT_DIR = "logs"
SUCCESS_RATE = 0.7

def generate_hourly_logs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_time = datetime(2026, 4, 7, 0, 0, 0)

    for hour in range(HOURS_TO_GENERATE):
        current_hour = base_time + timedelta(hours=hour)

        # File name: app_YYYY-MM-DD_HH.log
        file_name = current_hour.strftime("app_%Y-%m-%d_%H.log")
        file_path = os.path.join(OUTPUT_DIR, file_name)

        with open(file_path, "w") as f:
            for i in range(LINES_PER_FILE):
                # Random user
                user = f"user{random.randint(1000, 9999)}"

                # Spread timestamps within the hour
                seconds_offset = random.randint(0, 3599)
                timestamp = current_hour + timedelta(seconds=seconds_offset)

                # Random IP
                ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

                # Status
                status = "Success" if random.random() < SUCCESS_RATE else "Failed"

                log_line = f"{user}|{timestamp.isoformat()}|{ip}|{status}\n"
                f.write(log_line)

        print(f"✅ Generated: {file_path} ({LINES_PER_FILE} lines)")

if __name__ == "__main__":
    generate_hourly_logs()
