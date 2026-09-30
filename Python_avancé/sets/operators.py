a= {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b)) # union des deux sets
print(a | b) # union des deux sets

print(a.intersection(b)) # intersection des deux sets
print(a & b) # intersection des deux sets

print(a.difference(b)) # difference des deux sets
print(a - b) # difference des deux sets
print(b - a) # difference des deux sets

print(a.symmetric_difference(b)) # difference symétrique des deux sets
print(a ^ b) # difference symétrique des deux sets