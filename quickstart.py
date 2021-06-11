# import gym
# import gym_deepracer
# import time

# env = gym.make('deepracer-v0')   # starts as 1000x600
# env.update_random_settings({'car_rand_loc':False})
# env.resize(128,128) # resize to 128x128 for learning

# state = env.reset()

# for _ in range(200):
#     throttle = 2  # accelerate at 2 m/s^2
#     turn = 15     # turn wheels 15 degrees
#     action = (throttle, turn)
#     state, reward, done, _ = env.step(action)
#     time.sleep(1/10) # run at 10fps
# env.quit()


# import gym
# import gym_deepracer

# env = gym.make('deepracer-v0')
# env.update_random_settings({'car_rand_loc':False})

# camera_view = env.reset()
# env.play()

def reward(params):
    """
    Available option:
        all_wheels_on_track (bool)
            True if car is on track, False otherwise
        x (float)
            x coordinate in meters
        y (float)
            y coordinate in meters
        distance_from_center (float)
            distance from car center to track center in meters
        is_left_of_center (bool)
            True if car is left of track cener, False otherwise
        heading (float)
            range of [0,360), this is the angle in degrees between
            the car's direction and the x-axis
        progress (float)
            range of [0,100], this is the percentage of the track completed
        steps (int)
            number of steps taken in the environment. This resets every time
            a new episode begins, and currently the maximum episode length is 200
        speed (float)
            current speed of car in meters per second
        steering_angle (float)
            range of about [-30,30], this is the angle at which the wheels are
            turning
        track_width (float)
            the track width in meters
    """
    if params['all_wheels_on_track']:
        return 1.0
    else:
        return 0.0


from train import ModelBuilder, ModelTester

model_builder = ModelBuilder()

model_builder.set_reward(reward)
model_builder.run_builder_tool()


model_tester = ModelTester()
model_tester._env.update_reward_func(reward)
model_tester.run_test_tool()