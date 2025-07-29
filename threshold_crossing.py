import numpy as np

def count_spikes(time_series, threshold=0):
    """
    Counts the number of times a time series crosses from below to above a specified threshold.

    Args:
        time_series (list or np.array): The time series data.
        threshold (float): The value of the threshold.

    Returns:
        int: The total number of threshold crossings from below to above.
    """
    if not isinstance(time_series, (list, np.ndarray)):
        raise TypeError("time_series must be a list or a numpy array.")
    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be a number.")

    # Convert to numpy array for easier numerical operations
    time_series = np.array(time_series)

    # Calculate the difference between consecutive points and the threshold
    diff_from_threshold = time_series - threshold

    # Find where the sign changes, indicating a crossing
    # np.sign returns -1 for negative, 0 for zero, 1 for positive
    # We look for sign changes in consecutive elements
    sign_changes = np.diff(np.sign(diff_from_threshold))

    # A crossing from below to above means the sign changes from -1 to 1.
    # This results in a sign_change value of 2 (1 - (-1) = 2)
    count = np.sum(sign_changes > 0)

    return count

# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Simple time series
    data1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]
    threshold1 = 2.5

    print(f"Time Series 1: {data1}")
    print(f"Threshold 1: {threshold1}")

    crossings_above1 = count_threshold_crossings(data1, threshold1)
    print(f"Crossings (below to above): {crossings_above1}") # Expected: 2 (2.5 -> 3, 1 -> 2)

    print("-" * 30)

    # Example 2: Time series with multiple consecutive points above/below
    data2 = [10, 11, 9, 8, 12, 13, 7, 6, 15, 14]
    threshold2 = 10.0

    print(f"Time Series 2: {data2}")
    print(f"Threshold 2: {threshold2}")

    crossings_above2 = count_threshold_crossings(data2, threshold2)
    print(f"Crossings (below to above): {crossings_above2}") # Expected: 2 (8->12, 6->15)

    print("-" * 30)

    # Example 3: Edge cases (starting/ending on threshold, flat lines)
    data3 = [5, 5, 5, 6, 7, 5, 4, 5, 5]
    threshold3 = 5.0

    print(f"Time Series 3: {data3}")
    print(f"Threshold 3: {threshold3}")

    crossings_above3 = count_threshold_crossings(data3, threshold3)
    print(f"Crossings (below to above): {crossings_above3}") # Expected: 1 (5->6)

    print("-" * 30)

    # Example 4: Using numpy array directly
    data4 = np.array([0.1, 0.5, 0.9, 1.2, 0.8, 0.3, 0.7, 1.1])
    threshold4 = 1.0

    print(f"Time Series 4: {data4}")
    print(f"Threshold 4: {threshold4}")

    crossings_above4 = count_threshold_crossings(data4, threshold4)
    print(f"Crossings (below to above): {crossings_above4}") # Expected: 2 (0.9->1.2, 0.7->1.1)
