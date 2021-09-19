# Cat or Dog

This is a tiny Machine Learning project with using AWS Lambda Container.
In the past, AWS Lambda was not the right approach because [Tensorflow](https://www.tensorflow.org/) is too big and even with zipping and sizing, the space on AWS Lambda was not sufficient.

Since [Lambda with Container](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html), we are able to use libraries with up to 10 GB.

This project compares an image with an already defined model.

## Prerequisite

* Docker
* [AWS Sam](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Usage

Run `sam build` and `sam local invoke --debug --event events.json` for testing.

Run `sam deploy` for deploying.

That's it.

## Example

You could use a client such as Postman and run a post-request after deploying:

```bash
curl -XPOST "https://<aws-hash>.execute-api.<aws-region>.amazonaws.com/Prod/predict" -d '{"image_path": "https://www.rover.com/blog/wp-content/uploads/2018/12/dog-sneeze-1-1024x945.jpg"}'
```

## Development

You need at least Python3.9:

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```
