import numpy as np
import scipy.stats
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

def get_samples(p, n):
    return np.random.binomial(n, p) / n

def run_ab_test(p_a, p_b, n_total=1000, bucket_ratio=0.5, alpha=0.05):
    z_low = scipy.stats.norm.ppf(alpha / 2)
    z_high = scipy.stats.norm.ppf(1 - alpha / 2)

    n_a = 0
    n_b = 0
    for _ in range(n_total):
        if np.random.random() <= bucket_ratio:
            n_a += 1
        else:
            n_b += 1

    observed_a = get_samples(p_a, n_a)
    observed_b = get_samples(p_b, n_b)

    var_a = observed_a * (1 - observed_a)
    var_b = observed_b * (1 - observed_b)

    z = (observed_b - observed_a) / np.sqrt(var_a / n_a + var_b / n_b)

    if z < z_low or z > z_high:
        return True

    return False

def run_power_simulation(p_a, changes, alpha=0.05, n_simulations=10000):
    results = []
    for change in changes:
        p_b = p_a + change
        test_result = np.array([run_ab_test(p_a, p_b) for _ in range(n_simulations)])
        results.append(test_result.mean())

    plt.title('Control Proportion: {} | alpha: {}'.format(p_a, alpha))
    sns.barplot(changes, results)
    plt.xlabel('True Difference in Proportion')
    plt.ylabel('Percentage of Statistically Significant Simulations')
    plt.show()

    return results


np.random.seed(0)

n_simulations = 1000
p_a = 0.4
changes = [-0.05, -0.03, -0.02, 0.02, 0.03, 0.05]
alpha = 0.05  # two tail

results = run_power_simulation(p_a, changes, alpha, n_simulations)
print(results)


