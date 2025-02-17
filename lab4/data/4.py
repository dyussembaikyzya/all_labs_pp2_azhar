from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

yesterday_timestamp = yesterday.timestamp()
tomorrow_timestamp = tomorrow.timestamp()

print(tomorrow_timestamp - yesterday_timestamp)
