import gym
import numpy as np
import torch
import argparse
import os

import utils
import DDPG
import BCQ
import TD3
import REM


# Runs policy for X episodes and returns average reward
def evaluate_policy(policy, eval_episodes=10):
	avg_reward = 0.
	for _ in xrange(eval_episodes):
		obs = env.reset()
		done = False
		while not done:
			action = policy.select_action(np.array(obs))
			obs, reward, done, _ = env.step(action)
			avg_reward += reward

	avg_reward /= eval_episodes

	print "---------------------------------------"
	print "Evaluation over %d episodes: %f" % (eval_episodes, avg_reward)
	print "---------------------------------------"
	return avg_reward


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--env_name", default="Hopper-v1")				# OpenAI gym environment name
	parser.add_argument("--seed", default=0, type=int)					# Sets Gym, PyTorch and Numpy seeds
	parser.add_argument("--buffer_type", default="Robust")				# Prepends name to filename.
	parser.add_argument("--eval_freq", default=5e3, type=float)			# How often (time steps) we evaluate
	parser.add_argument("--max_timesteps", default=1e6, type=float)		# Max time steps to run environment for
	parser.add_argument("--agent_name", default="BCQ")
	parser.add_argument("--lr", default=1e-3, type=float)
	args = parser.parse_args()

	file_name = "%s_%s_%s_%s" % (args.agent_name, args.env_name, str(args.seed), str(args.lr))
	buffer_name = "%s_%s_%s" % (args.buffer_type, args.env_name, str(args.seed))
	print "---------------------------------------"
	print "Settings: " + file_name
	print "---------------------------------------"

	results_dir = "./results_%s" % (args.agent_name)
	if not os.path.exists(results_dir):
	  os.makedirs(results_dir)

	env = gym.make(args.env_name)

	env.seed(args.seed)
	torch.manual_seed(args.seed)
	np.random.seed(args.seed)
	
	state_dim = env.observation_space.shape[0]
	action_dim = env.action_space.shape[0] 
	max_action = float(env.action_space.high[0])

	# Initialize policy
	if args.agent_name == 'BCQ':
	  policy_agent = BCQ.BCQ
	elif args.agent_name == 'TD3':
	  policy_agent = TD3.TD3
	elif args.agent_name == 'REM':
	  policy_agent = REM.REM
	policy = policy_agent(state_dim, action_dim, max_action, lr=args.lr)

	# Load buffer
	replay_buffer = utils.ReplayBuffer()
	replay_buffer.load(buffer_name)
	
	evaluations = []

	episode_num = 0
	done = True 

	training_iters = 0
	while training_iters < args.max_timesteps: 
		pol_vals = policy.train(replay_buffer, iterations=int(args.eval_freq))

		evaluations.append(evaluate_policy(policy))
		np.save(results_dir + "/" + file_name, evaluations)

		training_iters += args.eval_freq
		print "Training iterations: " + str(training_iters)
