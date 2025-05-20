import json
import requests
import boto3
import pandas as pd
from io import StringIO
from datetime import datetime

def lambda_handler(event, context):
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    data = response.json()

    records = []
    for country in data.get("Countries", []):
        record = {
            "Country": country["Country"],
            "CountryCode": country["CountryCode"],
            "Date": country["Date"],
            "NewConfirmed": country["NewConfirmed"],
            "TotalConfirmed": country["TotalConfirmed"],
            "NewDeaths": country["NewDeaths"],
            "TotalDeaths": country["TotalDeaths"],
            "NewRecovered": country["NewRecovered"],
            "TotalRecovered": country["TotalRecovered"]
        }
        records.append(record)

    df = pd.DataFrame(records)
    df["ETL_Timestamp"] = datetime.utcnow().isoformat()

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3 = boto3.client('s3')
    bucket_name = "covid19-etl-processed"
    key = f"covid_summary_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    s3.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())

    return {
        'statusCode': 200,
        'body': json.dumps(f"ETL Success: {key} uploaded to {bucket_name}")
    }
