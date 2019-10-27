library(shiny)
library(tidyverse)

source("helper_functions.R")

# Call the clean_helper function to read in and clean the data as required
data = clean_helper('data/UMD_Services_Provided_20190719.tsv.txt')

# Call the B_data_helper function to prepare data for plot B
data_b = B_data_helper(data)

# Construct the ui
ui = fluidPage(
  
  titlePanel('BIOS611 Project 2        Yen Chang'),
  
  # Define the sidebar panel 
  sidebarLayout(
    
    sidebarPanel(
      
      
      helpText('Urban Ministries of Durham (UMD) is a non-profit organization providing
              shelter, food, clothing, hygiene kits, and other services to people in needs
              in Durham. This shiny dashboard aims to provide stakeholders of UMD
              with tools to visualize the different services provided between 1999 and 2019.
              The data set used in this dashboard is supplied by UMD.'),
      
      br(),  
      
      # Plot A1: a histogram of counts of a selected service in a selected period.
      # Plot A2: a pie chart showing the percentage of visits seeking the selected service in the selected period.
      h4(helpText('A. Counts of a particular service')),
      helpText('This widget creates a histogram and a pie chart of counts of a particular type of service in a selected period. Please select the type of service and the time period of interest.'),
      
      br(),
      
      # Input A_service: types of service to select from
      radioButtons(inputId = 'A_service',
                     label = 'Type of services',
                   choices = c('Food', 'Clothing', 'Diapers', 'School Kits', 'Hygiene Kits', 'Bus Tickets')),
      
      br(), 
      
      # Input A_year: years to display
      sliderInput(inputId = 'A_year',
                  label = 'Years',
                  min = 1999,
                  max = 2019,
                  value = c(1999,2019),
                  sep = ''),
      
      helpText('Visits prior to 1999 and after 2019 likely came from key-in errors, 
               therefore only visits betwen 1999 and 2019 are included here.'), 
      
      br(), br(), br(), br(), br(), br(), br(), br(), br(),
      
      
      # Plot B: Relationship between family size and use of services
      h4(helpText('B. Family size and services')),
      
      helpText('This widget creates a scatter plot looking at the relationship between family size and selected summary statistics for a selected type of service.'),
      
      radioButtons(inputId = 'B_service',
                   label = 'Type of service',
                   choices = c('Food Provided for', 'Food in Pounds', 'Clothing', 
                               'Diapers', 'School Kits', 'Hygiene Kits', 'Bus Tickets')),
      
      radioButtons(inputId = 'B_y_axis',
                   label = 'Summary to display on the y-axis',
                   choices = c('Count of visits attributable to the selected service',
                               'Proportion of visits attributable to the selected service',
                               'Average number of portions provided in each visit for the selected service'))
    ),
    
    
    # Main panel to display outputs
    mainPanel(
      
      # Output: A1 and A2 and related text 
      plotOutput(outputId = 'A1plot'),
      
      br(),
      
      textOutput(outputId = 'Acount'),
      
      br(), br(), 
      
      plotOutput(outputId = 'A2plot'),

      br(),
      
      # Output: B
      plotOutput(outputId = 'Bplot'),
      
      br(), br(),
      
      # Output: Data source
      textOutput(outputId = 'datasource')
    )
  )
)


# Define server
server = function(input, output) {
  
  # Creates plots and text output using helper functions and links them to ui
  
  # A_data_helper function creates a list containing the a subset of data for creating 
  # plots A1 and A2, as well as counts for both plots and text output. The other helper
  # functions take the list produced by A_data_helper to create plots or text. 
  output$A1plot = renderPlot({
    service_data_list = A_data_helper(data, input$A_service, input$A_year)
    A1_plot_helper(service_data_list, input$A_service, input$A_year)
  })
  
  output$A2plot = renderPlot({
    service_data_list = A_data_helper(data, input$A_service, input$A_year)
    A2_plot_helper(service_data_list, input$A_service)
  })
  
  output$Acount = renderText({
    service_data_list = A_data_helper(data, input$A_service, input$A_year)
    paste('Total number of services in this period:', service_data_list$total_count, '.', sep = '')
  })
  
  output$Bplot = renderPlot({
    B_plot_helper(data_b, input$B_y_axis, input$B_service)
  })
  
  output$datasource = renderText({
    'Data source: Urban Ministries of Durham'
  })
}

shinyApp(ui = ui, server = server)