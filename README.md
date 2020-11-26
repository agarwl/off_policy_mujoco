# Off-Policy Deep Reinforcement Learning without Exploration (REM + TD3)

```diff
- Note this is a preliminary repository and *no effort* was spent getting REM to work well with TD3 and (as it doesn't work).
- This repository should should not be used for benchmarking and only be used a starting point for MuJoCo experiments.
```

If you use this code, please cite the [paper](https://arxiv.org/abs/1812.02900) and the [paper](https://arxiv.org/abs/1907.04543). To launch batch experiments with `RSEM` or `REM`, use the file `run_main.sh`. To generate data, use `run_expert.sh`. `RSEM` works somewhat but not well though. 

Method is tested on [MuJoCo](http://www.mujoco.org/) continuous control tasks in [OpenAI gym](https://github.com/openai/gym). 
Networks are trained using [PyTorch 0.4](https://github.com/pytorch/pytorch) and Python 2.7.
