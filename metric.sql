-- Tabela de Métricas
CREATE TABLE device_metrics (
    time TIMESTAMPTZ NOT NULL,
    device_id VARCHAR(50) NOT NULL,
    cpu_percent DOUBLE PRECISION,
    memory_percent DOUBLE PRECISION,
    net_bytes_sent BIGINT,
    net_bytes_recv BIGINT
);

-- Transforma em Hypertable do TimescaleDB
SELECT create_hypertable('device_metrics', 'time');