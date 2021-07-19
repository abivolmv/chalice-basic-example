import asyncio
from io import BytesIO

from chalice import Chalice
from chalicelib.aws_utilities import s3_get, queue_publish
app = Chalice(app_name='basic-example')


@app.route('/')
def s3():
    return asyncio.run(main())


async def main():
    raw_data = BytesIO()
    await s3_get('s3-files-testing', 'test.txt', raw_data)
    raw_data.seek(0)
    return raw_data.read()


@app.route('/sqs')
def sqs():
    return asyncio.run(main_sqs())


async def main_sqs():
    await queue_publish('https://sqs.eu-west-1.amazonaws.com/111111111/sqs-test', "A message example")
    return
