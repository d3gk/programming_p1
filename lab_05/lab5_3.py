
# defining indexes
absolute_index = 1
index = 0x41

# outputting data for A-Z range
while index < 0x5B:
    print(f"{absolute_index:02})\t{chr(index)}\t{index:03}\t{hex(index)}")
    absolute_index += 1
    index += 1

index = 0x30

# outputting data for 0-9 range
while index < 0x3A:
    print(f"{absolute_index:02})\t{chr(index)}\t{index:03}\t{hex(index)}")
    absolute_index += 1
    index += 1


