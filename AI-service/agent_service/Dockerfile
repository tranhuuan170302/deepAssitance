FROM python:3.12-slim

RUN apt update && apt install -y ca-certificates
RUN update-ca-certificates

WORKDIR /app
COPY ./services/agent_service/requirements.txt
RUN pip install -r requirements.txt

COPY ./services/agent_service ./agent_service
COPY ./.env .

CMD ["uvicorn", "services.agent_service.app:app", "--host", "0.0.0.0", "--port", "8001"]