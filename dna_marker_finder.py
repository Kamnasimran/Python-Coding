def search4letters(phrase, letters="ATCG"):
    return set(letters).intersection(set(phrase))


def analyze_sequence(sequence_list, marker):
    print("Inside Function (Start) - ID:", id(sequence_list), "| Data:", sequence_list)

    sequence_list.append(marker)

    print("Inside Function (End) - ID:", id(sequence_list), "| Data:", sequence_list)


print("Task 1")

print(search4letters("TGGACC", "GC"))
print(search4letters(letters="CG", phrase="TGGACC"))
print(search4letters("TGGACC"))

print("Task 2")

dna_database = ["AATCCG", "TGGCTA"]

print("Global Scope (Before) - ID:", id(dna_database), "| Data:", dna_database)

analyze_sequence(dna_database, "CGAT")

print("Global Scope (After) - ID:", id(dna_database), "| Data:", dna_database)

print("Slice Experiment")

dna_database = ["AATCCG", "TGGCTA"]

print("Global Scope (Before) - ID:", id(dna_database), "| Data:", dna_database)

analyze_sequence(dna_database[:], "CGAT")

print("Global Scope (After) - ID:", id(dna_database), "| Data:", dna_database)

print("Edge Case 1")

print(search4letters(""))

print("Edge Case 2")

print(search4letters("TGGACC", letters="GC"))

print("Edge Case 3")

dna_database = ["AATCCG", "TGGCTA"]

analyze_sequence(dna_database[:], "CGAT")
analyze_sequence(dna_database[:], "TTAA")

print("Original List:", dna_database)
