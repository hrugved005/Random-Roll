from die import Die
import pygal

#Initialize two D6 dies.
die_1=Die()
die_2=Die()

#Generate rolls, store values in a list. 
results=[]
for roll_num in range(100):
    result=die_1.roll()+die_2.roll()
    results.append(result)
print(results)

#Analyze the results.
frequency=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(1, max_result+1):
    frequencies=results.count(value)
    frequency.append(frequencies)
print(frequency)

#Generate a histogram; visualize results.
hist=pygal.Bar()
hist.title="Result of rolling two D6 dice 1000 times."
hist.x_labels=['2','3','4','5','6', '7', '8', '9', '10', '11', '12']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('D6 + D6', frequency)
hist.render_to_file("die_vis.svg")