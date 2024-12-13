from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2024-12-13T00:56:00', 'schedule': None, 'catchup': False, 'dag_id': '7ca144dd6ef6494a995a2098b229e139'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    SleepPiece_f9a533ff5b104d72889b31cc3ba5a03b = Task(
        dag,
        task_id='SleepPiece_f9a533ff5b104d72889b31cc3ba5a03b',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SleepPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'sleep_time': 1}
    )()

