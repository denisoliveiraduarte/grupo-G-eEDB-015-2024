# Importação de dados de Taxis para Source

## Importação de bibliotecas

import boto3
s3 = boto3.resource('s3')

## Definição de Funções

def TransferData(bucketSourceName, bucketTargetName, folderSourcePrefix, folderTargetName):
    for obj in bucketSource.objects.filter(Prefix=folderSourcePrefix):
        source_filename = (obj.key).split('/')[-1]
        copy_source = {
        'Bucket': bucketSourceName,
        'Key': obj.key
        }
        target_filename = "{}/{}".format(folderTargetName, source_filename)
        if source_filename != '':
            if not list(bucketTarget.objects.filter(Prefix=target_filename).limit(1)):
                s3.meta.client.copy(copy_source, bucketTargetName, target_filename)

## Seleção de buckets source e target

bucketSourceName = 'nyc-tlc'
bucketTargetName = 'taxis-ny-source'
bucketSource = s3.Bucket(bucketSourceName)
bucketTarget = s3.Bucket(bucketTargetName)

## Seleção de pastas source e target de dados viagens de taxi

folderSourcePrefix = 'trip data'
folderTargetName = 'trip data'

## Transferência de dados de viagens da origem para source
TransferData(bucketSourceName, bucketTargetName, folderSourcePrefix, folderTargetName)