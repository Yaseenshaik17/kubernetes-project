#!/bin/bash
sudo pkill -f port-forward || true
tmux kill-session -t prom-pf 2>/dev/null || true
tmux kill-session -t graf-pf 2>/dev/null || true

tmux new-session -d -s prom-pf "while true; do kubectl port-forward --address 0.0.0.0 svc/prometheus-service 9090:9090; sleep 1; done"
tmux new-session -d -s graf-pf "while true; do kubectl port-forward --address 0.0.0.0 svc/grafana-service 3000:80; sleep 1; done"
