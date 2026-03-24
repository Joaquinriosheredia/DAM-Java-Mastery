```python
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Configuración del proveedor de métricas y trazas para exportar a OTLP
tracer_provider = TracerProvider()
otlp_span_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_span_exporter)
tracer_provider.add_span_processor(span_processor)

meter_provider = MeterProvider(
    metric_readers=[PeriodicExportingMetricReader(OTLPMetricExporter(endpoint="localhost:4317"))]
)

# Instanciación del módulo de métricas con el proveedor
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__, "0.1.2")

def create_metric(name, description):
    """Crea una nueva métrica en la aplicación"""
    return meter.create_counter(
        name=name,
        unit="unit",
        description=description
    )

def record_metrics(counter_name, value):
    """Registra un valor para una determinada métrica"""
    counter = create_metric(counter_name, "Descripción de la métrica")
    counter.add(value)
```