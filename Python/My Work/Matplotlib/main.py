import matplotlib.pyplot as plt, numpy as np



# Line Graph

# over=[1,2,3,4,5,6,7,8,9,10]
# pakistan=[10,15,17,12,36,22,24,21,10,21]
# australia=[5,10,15,20,25,27,23,40,30,20]
# plt.plot(over,pakistan,label="Pak")
# plt.plot(over,australia,label="Aus")
# plt.xlabel('over')
# plt.ylabel('Runs')
# plt.title('Line Graph')
# plt.legend() # labels dikhany ke liye zaroori hy
# # Show plot
# plt.show()



# ======== Bar Graph ===========


# categories = ['Pakistan', 'Australia', 'India', 'England']
# scores = [280, 310, 295, 260]

# bars = plt.bar(categories,scores)
# plt.title("Bar Graph -- Team Total Scores") # title of the graph
# plt.xlabel("Teams") # label shown on x-axis
# plt.ylabel("Runs") # label shown on y-axis
# plt.bar_label(bars, padding=3) # uper score dikhany ke liye
# plt.show()

# multiple bars, of same data

# gender = ['Male', 'Female', 'Other']
# ratio = [10, 15, 7]
# ratio2 = [2, 5, 7]
# x = np.arange(3)
# width = 0.35
# plt.bar(x-width/2,ratio, width=width,label='ratio',color='blue')
# plt.bar(x+width/2,ratio2,width=width, label='ratio2', color='red')
# plt.xticks(x,gender)
# plt.xlabel("Gender")
# plt.ylabel('Ratios')
# plt.legend()
# plt.show()



#  =============Scatter Plot===============


# days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week or any other time frame
# expenses = [200, 300, 250, 400, 150, 350, 300]  # Expenses on each day

# plt.scatter(days,expenses)
# plt.xlabel('Days')
# plt.ylabel('Expenses')
# plt.title("Scatter Plot for Days VS Expenses")
# plt.show()



# ============== HISTOGRAM ===============


# expenses = [200, 300, 250, 400, 150, 350, 300, 220, 270, 310, 180, 400, 150, 340, 370]

# plt.hist(expenses, width=20, bins=[150,200,250,300,350,400]) # bins -> no of bars
# plt.show()

# # we can create a cumulative histogram as well, passing cumulative= True




# =========== Pie Charts ===============


# gender = ['Male', 'Female', 'Other']
# ratio = [10, 15, 7]

# plt.pie(ratio, labels=gender, explode=(0.1,0,0), colors=['skyblue','lightgreen','lightcoral'])

# plt.show()



