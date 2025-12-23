# Generator Comprehensions
# Syntax: (expression for item in iterable if condition)
# Generators are used to create iterators in a memory-efficient way.
# They allow you to generate values on the fly, one at a time, rather than storing an entire sequence in memory. This makes them particularly useful when dealing with large datasets or infinite sequences. 
# Memory Efficiency: Generators produce values on demand, avoiding the need to store entire sequences in memory, which is crucial for large datasets.
# Lazy Evaluation: Values are generated only when requested, which can lead to performance improvements in certain scenarios.
# Infinite Sequences: Generators can represent infinite sequences, as they generate values on-the-fly without pre-computing them.

daily_sales=[5,10,15,20,25,30,35,40,45,50]
# Task : Find out total number of cups sold and find out only those > 5 using generator comprehension.

# sum is an inbuilt function that adds all the items in an iterable that is assigned to it.
total_cups_sold=sum(sale for sale in daily_sales if sale>5)

print(total_cups_sold)  # This will print the generator object. Genrator object does not store all values in memory, it generates them on-the-fly when iterated over. It is an iterable.

# op=270