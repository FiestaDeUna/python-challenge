import os
import csv

#create path 

csvpath = os.path.join("Resources", "budget_data.csv")


budget_data= []

#open reader 

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
   
    header = next(csvreader)  #separate header from data 

    #initialize value for total months

    month_count= 0
    total_sum = 0

    #calculate total months 

    for row in csvreader:
        budget_data.append(row)
        month_count += 1

        total_sum += int(row[1])


   #initialize values 

    differences_quant = month_count - 1
    single_difference= 0
    difference = 0
    greatest_decrease = 0
    greatest_increase = 0
   
    #Calculate average difference 

    for d in range(differences_quant): 
    
        single_difference = int(budget_data[d+1][1]) - int(budget_data[d][1])
        difference += single_difference
        av_difference = round(difference/differences_quant, 2)

    #calculate the greatest increase and decrease 

        if single_difference < greatest_decrease or greatest_decrease == 0 : 
            greatest_decrease = single_difference
            decrease_date = budget_data[d+1][0]
        if single_difference > greatest_increase or greatest_increase == 0 : 
            greatest_increase = single_difference 
            increase_date= budget_data[d+1][0]



#Compile and print results 

overall_analysis= (
 f"\n Budget Analysis \n\n" 
 f"-----------------------------------\n\n"
 f"Total Months: {month_count}\n\n" 
 f"Total: {total_sum}\n\n"
 f"Average change: {av_difference}\n\n"
 f"Greatest Increase in Profts: {increase_date} ({greatest_increase})\n\n"
 f"Greatest Decrease in Projets: {decrease_date} ({greatest_decrease})\n ")


print(overall_analysis)

#Write results to csv file 

analysis_path = os.path.join("Resources", "BudgetAnalysis.csv")
with open(analysis_path, 'w') as file: 
    file.write(overall_analysis)