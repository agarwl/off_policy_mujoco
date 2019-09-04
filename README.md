# Off-Policy Deep Reinforcement Learning without Exploration (REM + TD3)

If you use this code, please cite the [paper](https://arxiv.org/abs/1812.02900) and the [paper](https://arxiv.org/abs/1907.04543). To launch batch experiments with `RSEM` or `REM`, use the file `run_main.sh`. To generate data, use `run_expert.sh`. The `DDPG_REM` agent doesn't work, while `RSEM` works really well. 

Method is tested on [MuJoCo](http://www.mujoco.org/) continuous control tasks in [OpenAI gym](https://github.com/openai/gym). 
Networks are trained using [PyTorch 0.4](https://github.com/pytorch/pytorch) and Python 2.7. 

### Overview

Main algorithm, Batch-Constrained Q-learning (BCQ), can be found at BCQ.py.

If you are interested in reproducing some of the results from the paper, an expert policy (DDPG) needs to be trained by running train_expert.py. This will save the expert model. A new buffer can then be collected by running generate_buffer.py and adjusting the settings in the code or using the default settings. 
