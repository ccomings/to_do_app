# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS development

EXPOSE 8080

WORKDIR app-1

COPY * /app-1/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "8080"]

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
