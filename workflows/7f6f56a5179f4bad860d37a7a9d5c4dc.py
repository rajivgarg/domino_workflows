from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2024-12-12T02:16:00', 'schedule': None, 'catchup': False, 'dag_id': '7f6f56a5179f4bad860d37a7a9d5c4dc'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExampleSle_6dd031d139924d8e8140679ad97cfc92 = Task(
        dag,
        task_id='ExampleSle_6dd031d139924d8e8140679ad97cfc92',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExampleSleepPiece', 'source_image': 'ghcr.io/rajivgarg/my_custom_domino_pieces/new_repository_7f27827b:0.1.0-group0', 'repository_url': 'https://github.com/rajivgarg/my_custom_domino_pieces', 'repository_version': '0.1.1'},
        piece_input_kwargs={'sleep_time': 5}
    )()

