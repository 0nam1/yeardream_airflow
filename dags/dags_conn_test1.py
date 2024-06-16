from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator

with DAG(
	dag_id="dags_bash_operator", #Dag이름 지정
	schedule="None", #크론탭 문법으로 스케쥴 지정
) as dag:
	t1 = EmptyOperator(
		task_id="empty_t1", #테스크 명 지정
		empty_command="echo empty1", #실제 실행되는 수행 과업
	)

	t2 = EmptyOperator(
		task_id="empty_t2", #테스크 명 지정
		empty_command="echo empty2", #실제 실행되는 수행 과업
	)

	t1 >> t2 # 테스간 실행 순서
