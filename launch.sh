source ./configuration.conf

cd services/data_collector/bin
bash run.sh

cd ../../data_integrator/bin
bash run.sh

cd ../../data_processor/bin
bash run.sh
