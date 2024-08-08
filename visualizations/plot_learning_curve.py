# visualizations/plot_learning_curve.py

import matplotlib.pyplot as plt

def plot_learning_curve(rewards, filename='learning_curve.png'):
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Learning Curve')
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    # Example usage
    rewards = [1, 2, 3, 4, 5]  # Replace with actual reward data
    plot_learning_curve(rewards)
