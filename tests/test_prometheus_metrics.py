"""Tests for Prometheus metrics exporter."""
import pytest
from agent_memory_guard.metrics import PrometheusMetrics


def test_prometheus_metrics_imports():
    """Verify the metrics module loads without prometheus-client installed."""
    assert PrometheusMetrics is not None