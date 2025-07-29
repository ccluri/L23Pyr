import numpy as np

def interpolate_points(p1, p2, fraction):
    """
    Finds a point on the line defined by p1 and p2,
    interpolating or extrapolating based on the given fraction.

    Args:
        p1 (np.ndarray or list): The first 3D point (e.g., [x1, y1, z1]).
        p2 (np.ndarray or list): The second 3D point (e.g., [x2, y2, z2]).
        fraction (float): A scalar determining the position of the new point:
                          - If fraction = 0, the new point is p1.
                          - If fraction = 1, the new point is p2.
                          - If 0 < fraction < 1, the new point is between p1 and p2.
                          - If fraction > 1, the new point is beyond p2.
                          - If fraction < 0, the new point is beyond p1 (in the opposite direction).

    Returns:
        np.ndarray: The new 3D point.
    """
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)

    # Vector from p1 to p2
    v = p2 - p1

    # Calculate the new point using linear interpolation/extrapolation
    new_point = p1 + fraction * v
    return new_point #.tolist()

if __name__ == "__main__":
    # Example Usage:
    point1 = np.array([0.0, 0.0, 0.0])
    point2 = np.array([10.0, 0.0, 0.0])

    print(f"Original points: P1={point1}, P2={point2}")

    # Cases within the segment (0 <= fraction <= 1)
    fraction_0 = 0
    new_point_0 = interpolate_points(point1, point2, fraction_0)
    print(f"\nFraction = {fraction_0}: New point = {new_point_0}")
    # Expected: [0. 0. 0.] (same as P1)

    fraction_0_25 = 0.25
    new_point_0_25 = interpolate_points(point1, point2, fraction_0_25)
    print(f"Fraction = {fraction_0_25}: New point = {new_point_0_25}")
    # Expected: [2.5 0. 0.] (25% from P1 towards P2)

    fraction_0_5 = 0.5
    new_point_0_5 = interpolate_points(point1, point2, fraction_0_5)
    print(f"Fraction = {fraction_0_5}: New point = {new_point_0_5}")
    # Expected: [5. 0. 0.] (midpoint)

    fraction_0_75 = 0.75
    new_point_0_75 = interpolate_points(point1, point2, fraction_0_75)
    print(f"Fraction = {fraction_0_75}: New point = {new_point_0_75}")
    # Expected: [7.5 0. 0.] (75% from P1 towards P2)

    fraction_1 = 1
    new_point_1 = interpolate_points(point1, point2, fraction_1)
    print(f"Fraction = {fraction_1}: New point = {new_point_1}")
    # Expected: [10. 0. 0.] (same as P2)

    # Cases where fraction > 1 (extrapolating beyond P2)
    fraction_1_25 = 1.25
    new_point_1_25 = interpolate_points(point1, point2, fraction_1_25)
    print(f"\nFraction = {fraction_1_25}: New point = {new_point_1_25}")
    # Expected: [12.5 0. 0.] (25% beyond P2)

    fraction_2 = 2
    new_point_2 = interpolate_points(point1, point2, fraction_2)
    print(f"Fraction = {fraction_2}: New point = {new_point_2}")
    # Expected: [20. 0. 0.] (twice the distance from P1 as P2 is)

    # Cases where fraction < 0 (extrapolating beyond P1)
    fraction_minus_0_5 = -0.5
    new_point_minus_0_5 = interpolate_points(point1, point2, fraction_minus_0_5)
    print(f"\nFraction = {fraction_minus_0_5}: New point = {new_point_minus_0_5}")
    # Expected: [-5. 0. 0.] (50% of the distance from P1 in the opposite direction)

    fraction_minus_1 = -1
    new_point_minus_1 = interpolate_points(point1, point2, fraction_minus_1)
    print(f"Fraction = {fraction_minus_1}: New point = {new_point_minus_1}")
    # Expected: [-10. 0. 0.] (same distance as P2 from P1, but in opposite direction)

    # Example with different points and non-axial movement
    pA = np.array([1.0, 2.0, 3.0])
    pB = np.array([7.0, 8.0, 9.0])
    print(f"\nOriginal points: PA={pA}, PB={pB}")

    fraction_extrapolate = 1.5
    new_point_extrapolate = interpolate_points(pA, pB, fraction_extrapolate)
    print(f"Fraction = {fraction_extrapolate}: New point = {new_point_extrapolate}")
    # Expected: [1.0 + 1.5*(7-1), 2.0 + 1.5*(8-2), 3.0 + 1.5*(9-3)] = [1+9, 2+9, 3+9] = [10.0, 11.0, 12.0]

    fraction_backwards = -0.2
    new_point_backwards = interpolate_points(pA, pB, fraction_backwards)
    print(f"Fraction = {fraction_backwards}: New point = {new_point_backwards}")
    # Expected: [1.0 - 0.2*(7-1), 2.0 - 0.2*(8-2), 3.0 - 0.2*(9-3)] = [1-1.2, 2-1.2, 3-1.2] = [-0.2, 0.8, 1.8]
