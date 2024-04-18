sudo python3 -m pip install boto3
aws s3 cp "s3://scripts-ingestion-taxis-ny/Download Taxis Data.py" .
spark-submit "Download Taxis Data.py"