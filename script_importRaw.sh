sudo python3 -m pip install boto3
aws s3 cp "s3://scripts-ingestion-taxis-ny/Taxi NY Import to Raw.py" .
spark-submit "Taxi NY Import to Raw.py"