import os
import shutil
from prometheus_client import start_http_server, Counter, multiprocess, CollectorRegistry

# ensure variable exists, and ensure defined folder is clean on start
prome_stats = os.environ["PROMETHEUS_MULTIPROC_DIR"]
if os.path.exists(prome_stats):
    shutil.rmtree(prome_stats)
os.mkdir(prome_stats)

MXSERVER_RECEIVED_EMAIL = Counter('mxserver_received_email', 'Total number of emails received.')

registry = CollectorRegistry()
multiprocess.MultiProcessCollector(registry)


def start():
    global registry
    start_http_server(9090, registry=registry)
