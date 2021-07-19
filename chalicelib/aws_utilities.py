#!/usr/bin/python
# -*- coding: utf-8 -*-

import aioboto3

aio_session = aioboto3.Session()


async def s3_get(bucket, key, filelike):
    async with aio_session.client('s3') as s3:
        return await s3.download_fileobj(bucket, key, filelike)


async def queue_publish(queue_url: str, message_body: str):
    async with aio_session.client('sqs') as sqs_client:
        return await sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )