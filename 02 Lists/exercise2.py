# # numbers = [10, 20, 30, 40, 50, 60, 70, 80]


# # print(numbers[:4])
# # print(numbers[-3:])
# # print(numbers[::2])
# # print(numbers[-1::-1])

# marks = [75, 82, 90, 65, 88, 75, 95]

# print(marks)
# print(f"{(sum(marks) / len(marks)):.2f}")
# print(max(marks),  min(marks))
# print(marks.count(75))
# marks.sort(reverse=True)
# print(marks)
 
# print([m for m in marks if m > 80])


numbers = [10, 20, 10, 30, 20, 40, 10, 50]
new_arr = []
for number in numbers:
    if number not in new_arr:
        new_arr.append(number)



print(new_arr)