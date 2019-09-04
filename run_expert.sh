seed=$1
env_name=$2
start_timesteps=1000

if [[ $env_name == "HalfCheetah-v1" ]]; then
  start_timesteps=10000
fi

stdbuf -oL python train_expert.py --env_name $env_name --seed $seed --expl_noise 0.5 --start_timesteps $start_timesteps > "out_files/${env_name}_${seed}.txt" &
