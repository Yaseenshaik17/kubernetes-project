# Deployment of a Containerized Task Management Application using Kubernetes


A production-grade Task Management application built with **Spring Boot** and **MySQL**, containerized with **Docker**, and orchestrated using **Kubernetes** on **AWS EC2**.

## 🚀 Overview

This project demonstrates a modern DevOps workflow to ensure high availability, scalability, and real-time monitoring of a microservices-based application.

### Key Features
- **Containerization:** Application packaged into lightweight Docker images.
- **Orchestration:** Managed by a 3-node Kubernetes cluster (1 Master, 2 Workers) on AWS.
- **Self-Healing:** Kubernetes automatically restarts failed containers and reschedules pods on healthy nodes.
- **Scalability:** Horizontal Pod Autoscaling capable of handling traffic spikes.
- **Database Persistence:** MySQL data is secured using Persistent Volume Claims (PVC).
- **Monitoring Stack:** Full observability using Prometheus and Grafana dashboards.

## 🏗️ Architecture

- **Frontend/Backend:** Java Spring Boot (Port 8080)
- **Database:** MySQL 8.0 (Port 3306)
- **Deployment:** K8s Deployment with 3 Replicas
- **External Access:** NodePort Services
  - App: `30080`
  - Grafana: `3000`
  - Prometheus: `9090`

## 🛠️ Tech Stack
- **Cloud:** AWS (EC2)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Kubeadm)
- **Monitoring:** Prometheus, Grafana, Node Exporter
- **Build Tool:** Maven

## 📈 Monitoring
The system includes a custom Grafana dashboard that tracks:
- Application Uptime
- CPU & Memory Usage
- HTTP Request Rates

---

## 🚦 How to Run

1. **Build Docker Image:**
   ```bash
   docker build -t your-username/task-manager .
   ```

2. **Deploy to Kubernetes:**
   ```bash
   kubectl apply -f k8s/mysql.yaml
   kubectl apply -f k8s/springboot-app.yaml
   kubectl apply -f k8s/monitoring.yaml
   ```

3. **Access Services:**
   - App: `http://<Node-IP>:30080`
   - Grafana: `http://<Node-IP>:3000`
