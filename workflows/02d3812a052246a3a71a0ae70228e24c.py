from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2024-12-13T01:03:00', 'schedule': None, 'catchup': False, 'dag_id': '02d3812a052246a3a71a0ae70228e24c'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExampleSle_d73110e455024759ac0e75913bc03d37 = Task(
        dag,
        task_id='ExampleSle_d73110e455024759ac0e75913bc03d37',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExampleSleepPiece', 'source_image': 'ghcr.io/rajivgarg/my_custom_domino_pieces/new_repository_7f27827b:development-group0', 'repository_url': 'https://github.com/rajivgarg/my_custom_domino_pieces', 'repository_version': '0.1.2'},
        piece_input_kwargs={'sleep_time': 1}
    )()

