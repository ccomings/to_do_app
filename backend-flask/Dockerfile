# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS development

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR app

COPY * /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM development as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
