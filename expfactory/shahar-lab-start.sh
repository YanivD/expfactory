port=5000;
studyid=maayan_results;
experiments=teacher_starter,teacher_practice,teacher_test;

kill $(ps aux | grep python | grep $port | awk '{print $2}'); 
EXPFACTORY_STUDY_ID=$studyid EXPFACTORY_RANDOM=false EXPFACTORY_EXPERIMENTS=$experiments /usr/bin/python3 /usr/local/bin/gunicorn expfactory.wsgi:app --bind 0.0.0.0:$port --name expfactory_experiments --workers 1 --log-level=info --log-file=/scif/logs/gunicorn.log --access-logfile=/scif/logs/gunicorn-access.log > /dev/null &
