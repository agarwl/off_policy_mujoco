env_names=('HalfCheetah-v1' 'Hopper-v1' 'Walker2d-v1')
seed=$1
agent="$2"
lr=${3:-1e-3}
prefix=${4:-default}
t=${5:-1e6}

for env_name in ${env_names[@]}; do
  filename="out_files/${agent}_${env_name}_${seed}_${lr}" 
  if [[ $prefix != "default" ]]; then
    filename="${filename}_${prefix}"
  fi
  stdbuf -oL python main.py --env_name $env_name --seed $seed --buffer_type "Final" --agent_name $agent --lr $lr --prefix $prefix --max_timesteps $t > "${filename}.txt" &
done
