# COVID-19-Data-ETL-Pipeline-in-AWS
ETL Pipeline for Global COVID-19 Data using AWS Lambda, S3 and Glue


# AWS COVID-19 ETL Pipeline

This project builds a serverless ETL pipeline that:
- Fetches COVID-19 data from a public API
- Transforms it using AWS Lambda
- Loads it into an S3 data lake
- Is triggered via API Gateway

# Data Source

- https://covid19api.com
- Or download CSV from Johns Hopkins CSSE GitHub

## Stack
- AWS Lambda
- Amazon S3
- API Gateway
- Python 3
- Pandas

## Architecture

See the diagram below for a high-level overview of the architecture.

![ChatGPT Image May 20, 2025, 11_34_56 AM](https://github.com/user-attachments/assets/c2ae337c-25c8-47d2-a78a-150c200b1c4c)


## How to Deploy
1. Create S3 bucket `covid19-etl-processed`
2. Create IAM Role for Lambda with `S3FullAccess` + `BasicExecution`
3. Deploy Lambda using code from `lambda_function.py`
4. Create HTTP API Gateway trigger (`GET /run-etl`)
5. Hit the endpoint to load new data to S3

## Next Steps
- Add Glue Crawler & Athena queries
- Automate daily using EventBridge
- Visualize in QuickSight


