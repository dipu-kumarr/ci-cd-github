ci-cd-aws-docker/
├── app/
│   ├── app.py                  # Flask application
│   ├── requirements.txt        # Application dependencies
│   ├── tests/                  # Testing folder
│   │   ├── test_app.py         # Unit tests using Pytest
├── docker/
│   ├── Dockerfile              # Dockerfile for building the app container
│   ├── docker-compose.yml      # Docker Compose for local setup
├── infrastructure/
│   ├── main.tf                 # Terraform configuration
│   ├── variables.tf            # Terraform variables
│   ├── outputs.tf              # Terraform outputs
│   ├── terraform.tfvars        # Terraform variable values
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions CI/CD pipeline
├── README.md                   # Documentation
