import d4rl
import gym
from gym.envs.registration import register
from stable_baselines3.common.vec_env import DummyVecEnv

from utils.maze_utils import maze_name_to_maze_spec

env_id = "maze2d-custom-v1"
dist = True

if env_id not in gym.envs.registry.env_specs:

    assert env_id == "maze2d-custom-v1"
    max_episode_steps = 600
    maze_spec = maze_name_to_maze_spec(env_id, eval_maze_name="default")

    register(
        id=env_id,
        entry_point=(
            "d4rl.pointmaze:MazeEnvWithDist" if dist else "d4rl.pointmaze:MazeEnv"
        ),
        max_episode_steps=max_episode_steps,
        kwargs=dict(maze_spec=maze_spec, reward_type="sparse", reset_target=False),
    )


env = gym.make(env_id)
# sample random actions and print observations
env = DummyVecEnv([lambda: env])
obs = env.reset()
for _ in range(1000):
    actions = [env.action_space.sample()]
    obs, rewards, dones, info = env.step(actions)
    print(obs)
    print(obs.shape)
