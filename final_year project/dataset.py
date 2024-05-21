# import pandas as pd
# import numpy as np
#
#
# def generate_synthetic_data(n_samples=1000):
#     np.random.seed(42)
#
#     # Age distribution: higher probability for ages above 40, especially above 65
#     age_prob = np.array([0.05] * 10 + [0.15] * 30 + [0.8] * 20)
#     age_prob /= age_prob.sum()  # Normalize to sum to 1
#     age = np.random.choice(range(30, 90), size=n_samples, p=age_prob)
#
#     # Heart rate distribution: higher probability above 100 bpm
#     heart_rate_prob = np.array([0.1] * 40 + [0.9] * 40)
#     heart_rate_prob /= heart_rate_prob.sum()  # Normalize to sum to 1
#     heart_rate = np.random.choice(range(60, 140), size=n_samples, p=heart_rate_prob)
#
#     # Oxygen level distribution: higher probability below 90%
#     oxygen_level_prob = np.array([0.7] * 20 + [0.3] * 10)
#     oxygen_level_prob /= oxygen_level_prob.sum()  # Normalize to sum to 1
#     oxygen_level = np.random.choice(range(70, 100), size=n_samples, p=oxygen_level_prob)
#
#     # Hypertension distribution: 0 for normal, 1 for hypertension
#     hypertension = np.random.choice([0, 1], size=n_samples, p=[0.3, 0.7])
#
#     # Labels: 0 for No Sleep Apnea, 1 for Mild Sleep Apnea, 2 for Severe Sleep Apnea
#     sleep_apnea = np.where((age > 65) & (heart_rate > 100) & (oxygen_level < 90) & (hypertension == 1), 2,
#                            np.where((heart_rate > 90) | (oxygen_level < 85), 1, 0))
#
#     df = pd.DataFrame({
#         'Age': age,
#         'HeartRate': heart_rate,
#         'OxygenLevel': oxygen_level,
#         'Hypertension': hypertension,
#         'SleepApnea': sleep_apnea
#     })
#
#     return df
#
#
# # Generate and save the synthetic dataset
# df = generate_synthetic_data()
# df.to_csv('synthetic_sleep_apnea_dataset.csv', index=False)
# print("Dataset generated and saved as 'synthetic_sleep_apnea_dataset.csv'")


import pandas as pd
import numpy as np


def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)

    # Age distribution: higher probability for ages above 40, especially above 65
    age_prob = np.array([0.05] * 10 + [0.15] * 30 + [0.8] * 20)
    age_prob /= age_prob.sum()  # Normalize to sum to 1
    age = np.random.choice(range(30, 90), size=n_samples, p=age_prob)

    # Heart rate distribution: higher probability above 100 bpm
    heart_rate_prob = np.array([0.1] * 40 + [0.9] * 40)
    heart_rate_prob /= heart_rate_prob.sum()  # Normalize to sum to 1
    heart_rate = np.random.choice(range(60, 140), size=n_samples, p=heart_rate_prob)

    # Oxygen level distribution: higher probability below 90%
    oxygen_level_prob = np.array([0.7] * 20 + [0.3] * 10)
    oxygen_level_prob /= oxygen_level_prob.sum()  # Normalize to sum to 1
    oxygen_level = np.random.choice(range(70, 100), size=n_samples, p=oxygen_level_prob)

    # Hypertension distribution: 0 for normal, 1 for hypertension
    hypertension = np.random.choice([0, 1], size=n_samples, p=[0.3, 0.7])

    # Labels: 0 for No Sleep Apnea, 1 for Mild Sleep Apnea, 2 for Moderate Sleep Apnea, 3 for Severe Sleep Apnea
    severe_condition = (age > 65) & (heart_rate > 100) & (oxygen_level < 90) & (hypertension == 1)
    moderate_condition = (heart_rate > 100) | (oxygen_level < 85)
    mild_condition = (heart_rate >= 90) & (heart_rate <= 100) | (oxygen_level >= 85) & (oxygen_level < 90)

    sleep_apnea = np.where(severe_condition, 3,
                           np.where(moderate_condition, 2,
                                    np.where(mild_condition, 1, 0)))

    df = pd.DataFrame({
        'Age': age,
        'HeartRate': heart_rate,
        'OxygenLevel': oxygen_level,
        'Hypertension': hypertension,
        'SleepApnea': sleep_apnea
    })

    return df


# Generate and save the synthetic dataset
df = generate_synthetic_data()
df.to_csv('synthetic_sleep_apnea_dataset.csv', index=False)
print("Dataset generated and saved as 'synthetic_sleep_apnea_dataset.csv'")

