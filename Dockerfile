FROM public.ecr.aws/bitnami/python:3.9.7
FROM public.ecr.aws/lambda/python:3.9

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD [ "handler.what_animal" ] 