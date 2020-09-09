def powerset(array):
    Set = [[]]
    for element in array:
        for subsetidx in range(len(Set)):
            current = Set[subsetidx]
            Set.append(current + [element])
    return Set

