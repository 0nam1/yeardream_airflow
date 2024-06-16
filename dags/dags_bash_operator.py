
from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
	dag_id="dags_bash_operator", #Dag이름 지정
	schedule="0 0 * * *", #크론탭 문법으로 스케쥴 지정
	start_date=pendulum.datetime(2024, 6, 14, tz="Asia/Seoul"), #Dag 시작 날짜
	catchup=True # 누락된 스케쥴을 따라잡을것인지 여부
) as dag:
	bash_t1 = BashOperator(
		task_id="bash_t1", #테스크 명 지정
		bash_command="echo whoami", #실제 실행되는 수행 과업
	)

	bash_t2 = BashOperator(
		task_id="bash_t2",
		bash_command="echo $HOSTNAME",
	)

	bash_t1 >> bash_t2 # 테스간 실행 순서