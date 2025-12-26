### Telco Churn – End-to-End ML Project
#### Purpose
Build and ship a full machine-learning solution for predicting customer churn in a telecom setting—from data prep and modeling to an API + web UI deployed on AWS.

#### Problem solved & benefits
* Faster decisions: Predicts which customers are likely to churn so teams can act before they leave.
* Operationalized ML: Model is accessible via a REST API and a simple UI; anyone can test it without notebooks.
* Repeatable delivery: CI/CD + containers mean every change can be rebuilt, tested, and redeployed in a consistent way.
* Traceable experiments: MLflow tracks runs, metrics, and artifacts for reproducibility and auditing.
#### What I built
Data & Modeling: Feature engineering + XGBoost classifier; experiments logged to MLflow.
Model tracking: Runs, metrics, and the serialized model logged under a named MLflow experiment.
Inference service: FastAPI app exposing /predict (POST) and a root health check /.
Web UI: Gradio interface mounted at /ui for quick, shareable manual testing.
Containerization: Docker image with uvicorn entrypoint (src.app.main:app) listening on port 8000.
CI/CD: GitHub Actions builds the image and pushes to Docker Hub; optionally triggers an ECS service update.
Orchestration: AWS ECS Fargate runs the container (serverless).
Networking: Application Load Balancer (ALB) on HTTP:80 forwarding to a Target Group (IP targets on HTTP:8000).
Security: Security groups scoped to allow ALB inbound 80 from the internet, and task inbound 8000 from the ALB SG.
Observability: CloudWatch Logs for container stdout/stderr and ECS service events.
#### Deployment flow (high-level)
Push to main → GitHub Actions builds the Docker image and pushes it to Docker Hub.
ECS service is updated (manually or via the workflow) to force a new deployment.
ALB health checks hit / on port 8000; once healthy, traffic is routed to the new task.
