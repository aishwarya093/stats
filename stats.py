# -*- coding: utf-8 -*-
"""stats.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/159NlSbpkZXOWWoUcg0NB99G-y5CiSFBc
"""

#1.  Explain the different types of data (qualitative and quantitative) and provide examples of each. Discuss
# nominal, ordinal, interval, and ratio scales

# Types of Data
# Qualitative Data: Non-numeric information describing categories or qualities.

# Examples:
# Nominal: Gender (Male/Female), Colors (Red, Blue).
# Ordinal: Education Level (High School, Bachelor's, Master's).
# Quantitative Data: Numeric information used for measurements or counts.

# Examples:
# Interval: Temperature in Celsius or Fahrenheit (no true zero).
# Ratio: Height, Weight, Age (has a meaningful zero)

# 2. What are the measures of central tendency, and when should you use each? Discuss the mean, median,
# and mode with examples and situations where each is appropriate.

# Mean: Average of all values.
# Use case: When data has no outliers.
# Median: Middle value when data is ordered.
# Use case: When data has outliers.
# Mode: Most frequently occurring value.
# Use case: For categorical data or identifying frequent occurrences


Data: {1, 2, 2, 3, 4}
Mean = 2.4, Median = 2, Mode = 2.

# 3. Explain the concept of dispersion. How do variance and standard deviation measure the spread of data?

# Dispersion shows the spread of data points around a central value.

# Variance: Average squared deviation from the mean.
# Standard Deviation: Square root of variance, indicating average deviation.
# Example: Low SD = values close to the mean; High SD = values spread out.

# 4.What is a box plot, and what can it tell you about the distribution of data?

# Box plot is a graphical representation of data distribution.

# Key Components: Minimum, Q1, Median, Q3, Maximum.
# Insights:
# Detects skewness and outliers.
# Shows data spread and symmetry.

# 5. Discuss the role of random sampling in making inferences about populations.

# Random sampling ensures each member of a population has an equal chance of selection.

# Role:
# Reduces bias.
# Facilitates inferences about a population.
# Ensures representativeness.

#6. Explain the concept of skewness and its types. How does skewness affect the interpretation of data?

# Measures the asymmetry of data distribution.

# Types:
# Positive Skew: Tail on the right (mean > median).
# Negative Skew: Tail on the left (mean < median).
# Symmetric: No skew (mean = median).
# Effect: Impacts mean as a measure of central tendency.

# 8. Discuss the conditions under which the binomial distribution is used?

# Conditions:

# Fixed number of trials.
# Two outcomes (success/failure).
# Constant probability of success.
# Example: Tossing a coin 10 times.

# 9.Explain the properties of the normal distribution and the empirical rule (68-95-99.7 rule).

# Properties:

# Bell-shaped curve.
# Symmetric around the mean.
# Mean = Median = Mode.

# 11. Explain what a random variable is and differentiate between discrete and continuous random variables

# Discrete: Countable outcomes (e.g., dice roll).
# Continuous: Infinite outcomes (e.g., height, weight).

# 12. Provide an example dataset, calculate both covariance and correlation, and interpret the results

# Dataset:
# X = {2, 3, 4}, Y = {5, 6, 7}

# Covariance = 1.
# Correlation = 1.
# Interpretation: Perfect positive linear relationship.