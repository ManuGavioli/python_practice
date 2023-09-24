#Average time courses duration
other_courses_min = 2.5
other_courses_max = 7
other_courses_avg = 4
dalto_course = 1.5

#Raw Durations
average_raw = 5
dalto_raw = 3.5

#Duration differences
diff_min = 100 - dalto_course / other_courses_min * 100
diff_max = 100 - dalto_course * 1000 // other_courses_max / 10
diff_avg = 100 - dalto_course / other_courses_avg * 100

#Calculating percent of empty time removed

empty_time_average = 100 - other_courses_avg * 1000 // average_raw / 10
empty_time_dalto = 100 - dalto_course * 1000 // dalto_raw / 10

#Showing the duration differences
print("--------------------------------------------")
print('Daltos course duration is:')
print(f'- {diff_min}% less than the fastest course')
print(f'- {diff_max}% less than the slowest course')
print(f'- {diff_avg}% less than the averange of the courses')
print("--------------------------------------------")

#Showing empty time removed
print(f'An average course deletes a {empty_time_average}% of empty time')
print(f'This course deletes a {empty_time_dalto}% of empty time')
print("--------------------------------------------")

#Showing differences if the courses lasted 10 hours
print(f'Watch 10 hours of Daltos course equals to {other_courses_avg * 100 // dalto_course / 10} hours of the rest of them')
print(f'Watch 10 hours of other courses equals to {dalto_course * 100 // other_courses_avg / 10} hours of the Daltos ones')
print("--------------------------------------------")