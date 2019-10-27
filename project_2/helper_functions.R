# This helper function reads in and prepares the UMD service data for analysis
clean_helper = function(data_path){
  
  # Read in dataset
  umd_df = read_tsv(data_path)
  
  # Clean data
  cleaned = umd_df %>%
    
    select(-'Client File Merge',-(Field1:Field3)) %>%          # Remove variables not used in the app
    
    rename(      'id' = 'Client File Number',                  # Rename variables
                'bus' = 'Bus Tickets (Number of)',
               'note' = 'Notes of Service',
             'food.n' = 'Food Provided for',
             'food.p' = 'Food Pounds',
            'clothes' = 'Clothing Items',
            'diapers' = 'Diapers',
             'school' = 'School Kits',
            'hygiene' = 'Hygiene Kits') %>%  
    
    mutate(date  = as.Date(Date, "%m/%d/%Y"),                   # Transform dates
           year  = as.numeric(format(date, '%Y')),
           month = as.numeric(format(date, "%m"))) %>%
    
    filter(between(year, 1999, 2019)) %>%                       # Keep only observations occuring between 1999 and 2019 
  
    mutate(food.ind = food.n > 0 | food.p > 0)                  # Create an indicator variable with 1 specifying seeking for food service
  return(cleaned)
}


# This helper function prepares data to be used in graphing A1 and A2 plots
A_data_helper = function(data,service,yr){
  service_var = switch(service,'Food' = 'food.ind', 'Clothing'='clothes', 'Diapers' = 'diapers',
                               'School Kits' = 'school', 'Hygiene Kits' = 'hygiene', 'Bus Tickets' = 'bus')
  
  # Create a text string with the years selected, to be used in the histogram title
  text = paste('(',min(yr),' to ',max(yr),')',sep='') 
  
  
  total_data = data %>%                       # Keep only the visits in the selected period
    filter(between(year,yr[1],yr[2]))
  
  total_count = dim(total_data)[1]            # Count the number of all services provided in the selected period
  
  service_data = total_data %>%               # Keep only visits seeking for the selected service
    filter(get(service_var) > 0) 
  
  service_count = dim(service_data)[1]        # Count the number of the selected service provided in the selected period
  
  return(list(text = text,                    # Return objects created in this function as a list
              total_count = total_count,
              service_data = service_data,
              service_count = service_count))
}


# This helper function creates plot A1
A1_plot_helper = function(data,service,yr){
  
  ggplot(data = data$service_data)+
    
    scale_x_continuous(breaks = seq(yr[1],yr[2],1))+
    
    labs(title = paste('A1. Counts of Visits Seeking', service, data$text),
         x = 'Year',
         y = 'Count of visits')+ 
    geom_bar(aes(year), fill = "#78517b")+
    
    theme( plot.title = element_text(size = 22),
          axis.text.x = element_text(angle = 45, hjust = 1))
  
}


# This helper function creates plot A2
A2_plot_helper = function(data,service){
  
  count.data = data.frame(
    type = c(service, 'Others'),
    n = c(data$service_count, data$total_count - data$service_count),    # The count attributable and the count not attributable to a selected service
    percent = 100 * c(data$service_count/data$total_count, 1-data$service_count/data$total_count)   # The proportion of above
  )

  count.data$type = factor(count.data$type, levels = c(service,'Others'))    # Setting factor level for the right order of variable display in the pie chart
  
  ggplot(data = count.data,aes("", percent, fill = type))+
    
    geom_bar(stat = "identity")+
    
    coord_polar("y", start = 0, direction = -1)+           # Pie Chart
    
    labs(title = paste('A2. Percentage of Visits Seeking', service),
         fill = '',
         caption = 'Some slices might not show on the pie chart due to extremely small percentages.')+
    
    scale_fill_manual(values = c("#ee6233","#3AA496"))+
    
    geom_text(aes(label = paste(round(percent, 2), '%')),position = position_stack(vjust = 0.5))+
    
    theme(   plot.title = element_text(size = 22),
           plot.caption = element_text(size = 12, hjust= 0.5),
           axis.title.x = element_blank(),
           axis.title.y = element_blank(),
             axis.ticks = element_blank(),
           panel.border = element_blank(),
             panel.grid = element_blank())
}


# This helper function perpares data for plot B
B_data_helper = function(data){
  household = data %>%
    
    arrange(id,date) %>%
    group_by(id) %>%
    
    mutate(food.n.trunc = ifelse(food.n > 50, NA, food.n),            # Food Provided for > 50 not reasonable, set to missing
           food.p.trunc = ifelse(food.p > 100, NA, food.p),           # Food in Pounds > 100 not reasonable, set to missing
                diapers = ifelse(diapers > 2000, NA, diapers)) %>%    # Diapers > 2000 not reasonable, set to missing
                
    summarize(size = max(food.n.trunc, 1, na.rm = TRUE),              # Estimate the size of a household by the maximum value of Food Provided for
              count_visit = n(),                                      # Count numbers of visits, total and by service type
              count_food.n = sum(food.n > 0 | food.p > 0, na.rm = TRUE),
              count_food.p = count_food.n,
              count_clothes = sum(clothes > 0, na.rm = TRUE),
              count_diapers = sum(diapers > 0, na.rm = TRUE),
              count_school = sum(school > 0, na.rm = TRUE),
              count_hygiene = sum(hygiene > 0, na.rm = TRUE),
              count_bus = sum(bus > 0, na.rm = TRUE),
              
              prop_food.n = count_food.n/count_visit,           # Count proportion of visits attributable to a specific type of service
              prop_food.p = prop_food.n,
              prop_clothes = count_clothes/count_visit,
              prop_diapers = count_diapers/count_visit,
              prop_school = count_school/count_visit,
              prop_hygiene = count_hygiene/count_visit,
              prop_bus = count_bus/count_visit,
              
              sum_food.n = sum(food.n.trunc, na.rm = TRUE),     # The total number of portions of a service provided to each household
              sum_food.p = sum(food.p.trunc, na.rm = TRUE),
              sum_clothes = sum(clothes, na.rm = TRUE),
              sum_diapers = sum(diapers, na.rm = TRUE),
              sum_school = sum(school, na.rm = TRUE),
              sum_hygiene = sum(hygiene, na.rm = TRUE),
              sum_bus = sum(bus, na.rm = TRUE),
              
              average_food.n = sum_food.n/count_food.n,         # The average number of portions of a service provided to each household when it came for that service
              average_food.p = sum_food.p/count_food.p,
              average_clothes = sum_clothes/count_clothes,
              average_diapers = sum_diapers/count_diapers,
              average_school = sum_school/count_school,
              average_hygiene = sum_hygiene/count_hygiene,
              average_bus = sum_bus/count_bus) 
  }

B_plot_helper = function(data, y_axis, service){
  
  y = switch(y_axis, 'Count of visits attributable to the selected service' = 'count',
                     'Proportion of visits attributable to the selected service' = 'prop',
                     'Average number of portions provided in each visit for the selected service' = 'average')
  
  service_var = switch(service,'Food Provided for' = 'food.n', 'Food in Pounds' = 'food.p', 'Clothing'='clothes', 
                               'Diapers' = 'diapers', 'School Kits' = 'school', 'Hygiene Kits' = 'hygiene', 'Bus Tickets' = 'bus')
  
  summary_var = paste(y, service_var, sep = '_')
  
  ggplot(data = data)+
    geom_count(aes(x = size, y = get(summary_var), color = ..n..))+
    
    labs(title = paste('B. Joint Distribution of Family Size and', service),
         x = 'Household size',
         y = paste(sub('the selected service','', y_axis),"\n ",service),
         #y = sub('the selected service', service, y_axis),
         caption = '1. Household size estimated by the maximum value of Food Provided for for that household. 
         \n2. Color and size of dots correspond to frequency of a value. 
         \n3. Food Provided for and Food in Pounds have the same count and proportion because both were for food.')+
   
    theme(plot.title = element_text(size = 22),
          plot.caption = element_text(size = 12, hjust = 0))+
    
    guides(color = 'legend')+
    
    scale_color_gradient(low="blue", high="red")
}