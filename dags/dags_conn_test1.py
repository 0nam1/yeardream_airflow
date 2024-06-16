from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator

with DAG(
	dag_id="dags_bash_operator", #Dag이름 지정
	schedule="None", #크론탭 문법으로 스케쥴 지정
) as dag:
	t1 = EmptyOperator(
		task_id="empty_t1" #테스크 명 지정
	)

	t2 = EmptyOperator(
		task_id="empty_t2" #테스크 명 지정
	)

	t3 = EmptyOperator(
		task_id="empty_t3" #테스크 명 지정
	)

	t4 = EmptyOperator(
		task_id="empty_t4" #테스크 명 지정
	)

	t5 = EmptyOperator(
		task_id="empty_t5" #테스크 명 지정
	)

	t6 = EmptyOperator(
		task_id="empty_t6" #테스크 명 지정
	)

	t7 = EmptyOperator(
		task_id="empty_t7" #테스크 명 지정
	)

	t8 = EmptyOperator(
		task_id="empty_t8" #테스크 명 지정
	)

	t1 >> t2 # 테스간 실행 순서
	t1 >> t3
	t3 >> t4
	t5 >> t4
	t4 >> t6
	t7 >> t6
	t6 >> t8
