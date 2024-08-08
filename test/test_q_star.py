# tests/test_q_star.py

import unittest
import numpy as np
from scripts.q_star_algorithm import QStarAlgorithm
from scripts.environment import Environment

class TestQStarAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.env = Environment('Taxi-v3')
        self.agent = QStarAlgorithm(self.env, alpha=0.1, gamma=0.99, epsilon=0.1)
    
    def test_choose_action(self):
        state = self.env.reset()
        action = self.agent.choose_action(state)
        self.assertIn(action, range(self.env.action_space.n))
    
    def test_update_q_table(self):
        state = self.env.reset()
        action = self.agent.choose_action(state)
        reward = 1
        next_state, _, _, _ = self.env.step(action)
        self.agent.update_q_table(state, action, reward, next_state)
        self.assertGreater(self.agent.q_table[state, action], 0)
    
    def tearDown(self):
        self.env.close()

if __name__ == "__main__":
    unittest.main()

