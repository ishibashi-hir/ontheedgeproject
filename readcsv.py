import io
import csv
import boto3


def get_s3file(bucket_name, key):
    s3 = boto3.resource('s3')
    s3obj = s3.Object(bucket_name, key).get()

    return io.TextIOWrapper(io.BytesIO(s3obj['Body'].read()))


for rec in csv.DictReader(get_s3file('hi1ro4yu8ki4webexample000', 'test.csv')):
    print(rec)