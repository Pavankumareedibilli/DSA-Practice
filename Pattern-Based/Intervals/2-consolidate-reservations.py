def consolidateReservations(reservations:list,newReservation:list):
    all_reservations = reservations + [newReservation]

    all_reservations.sort(key = lambda x : x[0])

    merged = []

    for start,end in all_reservations:
        if not merged or start>merged[-1][1]:
            merged.append([start,end])
        else:
            merged[-1][1] = max(merged[-1][1],end)

    return merged


# You are building a reservation system for a cloud provider.

# Each reservation occupies a compute resource during an inclusive time range:

# [start, end]

# For example:

# [10, 20]

# means the resource is occupied from time 10 through time 20.

# The system maintains existing reservations for one resource.

# Reservations may overlap because they came from an older system that did not enforce conflict checking.

# A new reservation request arrives.

# The system must return the consolidated occupied time ranges after adding the new reservation.

# Additional requirements
# The existing reservations are not sorted.
# Some existing reservations may already overlap.

# The output must contain:

# all occupied time ranges
# merged wherever ranges overlap or touch
# sorted by start time
# Example 1

# Input:

# reservations = [[8,10], [1,3], [2,6], [12,15]]
# new = [5,13]

# Expected output:

# [[1,15]]
# Example 2

# Input:

# reservations = [[10,12], [1,3], [5,7]]
# new = [3,5]

# Expected output:

# [[1,7], [10,12]]
# Example 3

# Input:

# reservations = []
# new = [4,8]

# Expected:

# [[4,8]]
# Constraints
# 1 <= number of reservations <= 100,000
# 0 <= start <= end <= 10^9

# Your algorithm should be efficient enough for 100,000 reservations.