# AOC Day 1
# Illia Nyshpor
# Date: 30.11.23

# Calculate how many calories the elf carrying the most has
# Pt 1
elves = []

with open("./aoc2022day1.txt") as f:
  
  cc = 0

  for line in f:
    if line.strip():
      cc += int(line.strip())
    else: 
      elves.append(cc)
      cc = 0

#bc = 0

#for elf in elves:
 # if elf > bc:
  #  bc = elf
  
print(max(elves))

# Pt 2
sorted(elves)
# print(sorted(elves[-1] + sorted(elves[-2])))

#se = sorted(elves)
#tt = sorted(elves)[-3:]
#stt = sum(tt)
#print(sum(sorted(elves)[-3:]))

sorted_elves = sorted(elves)
print(sorted_elves)

top_three = sorted_elves[-3:]
print(top_three)

top_three_total = sum(top_three)
print(top_three_total)

e = 68442 + 68177 + 66575
print(e)

#print(sum(sorted(elves)[-3:]))