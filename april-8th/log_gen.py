import random
from datetime import datetime, timedelta

# CONFIG
NUM_ENTRIES = 120000   # 1 lakh+ entries
OUTPUT_FILE = "sample.log"

# Optional: tweak these if you want patterns
SUCCESS_RATE = 0.7  # 70% success, 30% fail

def generate_log_file():
    start_time = datetime(2026, 4, 7, 13, 0, 0)

    with open(OUTPUT_FILE, "w") as f:
        for i in range(NUM_ENTRIES):
            # Random user ID
            user = f"user{random.randint(1000, 9999)}"

            # Incrementing timestamp
            timestamp = start_time + timedelta(seconds=i)

            # Random IP
            ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

            # Controlled success/failure ratio
            status = "Success" if random.random() < SUCCESS_RATE else "Failed"

            # Log line
            log_line = f"{user}|{timestamp.isoformat()}|{ip}|{status}\n"

            f.write(log_line)

    print(f"🔥 Log file generated: {OUTPUT_FILE} with {NUM_ENTRIES} entries")

if __name__ == "__main__":
    generate_log_file()
