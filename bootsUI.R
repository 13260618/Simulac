 
library(shiny)
library(plotly)
library(ggplot2)
library(htmlwidgets)
library(stats)
library(graphics)
 
# layout
library(shinyWidgets)
#library(shinydashoboard)
library(shinythemes)

# 
# if(!require(leaflet)) {install.packages("leaflet", repos = "http://cran.us.r-project.org")}
# 
# 
# if(!require(lubridate)) {install.packages("lubridate")}
# if(!require(shinyTime)) {install.packages("shinyTime")}
# if(!require(shinycssloaders)) {install.packages("shinycssloaders")}
# if(!require(plotly)) {install.packages("plotly")}
# if(!require(dplyr)) {install.packages("dplyr")}
# if(!require(shinydashboard)) {install.packages("shinydashboard")}

setwd("C://Users//LANREF//Documents//ss_imr//simulac")
 
library(leaflet)
library(readxl)


library(tippy) #
library(lubridate) # horas
library(shinyTime)
library(plotly)
library(dplyr)
library(shinycssloaders)
library(shinydashboard)

clima =  read_xlsx("clima.xlsx")  
datos = read.csv("historicos.csv")
dates = as.Date(clima$Fecha)
horas = clima$Hora
date0 = as.Date(datos$Fecha_inst)
date1 = as.Date(datos$Fecha_Rev)
temperatura = clima$`°C`
hora = (clima$Hora)
HR = clima$`HR(%)`



bootstrapPage( 
  
  tags$head(includeHTML("gtag.html")),
   
   navbarPage(theme = shinytheme("flatly"), collapsible = TRUE,
              HTML('<a style="text-decoration:none;cursor:default;color:#FFFFFF;" class="active" href="#">Simulac-2022</a>'), id="nav",
              windowTitle = "SIMULAC",
              
              tabPanel("Ciclo de Vida", 
                       div(class="outer",
                           tags$head(includeCSS("styles.css")),
                           leafletOutput("mymap", width="100%", height="100%")),
                
                       box(width =12, 
                           title = HTML("<b>Proceso del ciclo de vida de <i>Ceratitis capitata </i></b>"), 
                           #solidHeader = T, status = "primary",
                           
                           tabBox(title = HTML("<b style=color:#045a8d>1) Ovipostura</b>"), width = 2,tags$img(src="ovi.png",height = 250,width = 250)),
                           tabBox(title = HTML("<b style=color:#045a8d>2) Colonización</b>"), width = 2, tags$img(src="colo.png",height = 250,width = 250)),
                           tabBox(title = HTML("<b style=color:#045a8d>3) Dentro de fruto</b>"), width = 2,  tags$img(src="dentros.jpg",height = 250,width = 250)),
                           tabBox(width = 2, tags$img(src="emerg.png",height = 250,width = 250)),
                           tabBox(title = HTML("<b style=color:#045a8d>4) Ovipostura Oi</b>"),width = 2, tags$img(src="ovip.png",height = 250,width = 250)),
                           tabBox(width = 2,  tags$img(src="muere.png",height = 250,width = 250)),
                           fluidRow(
                             column(1,hr()),
                             column(1, 
                                    dateInput("fecha0", (HTML("<b style=color:#045a8d>Tiempo de inicio (ti)</b>")), value = as.character("2017/05/01"), min = min(date0), max = max(date0), format = "dd/mm/yyyy")
                             ),
                             column(3, " " ),
                             column(1,
                                    numericInput('intervalo', HTML("<b style=color:#045a8d>Intervalo de tiempo (it)</b>"), 1, min = 0,max = 5)
                             ),
                             
                             column(3, " " ),
                             
                             column(1,
                                    dateInput('dateff',  (HTML("<b style=color:#045a8d>Tiempo Máximo (tf)</b>")),value = as.character("2017/10/30"),min = min(date1), max = max(date1), format = "dd/mm/yyyy")
                             ),
                             column(1,hr())
                             
                           )
                           
                           
                           
                           ),
                       box(width = 12,status = "danger",
                           column(3,
                                  numericInput('Pi',"Periodo de Incubación (Pi)",3, min = 2, max = 3)
                           ),
                           column(3,
                                  numericInput('PI',"Periodo de Infestación (PI)",18, min = 18, max = 24)
                           ),
                           column(3,
                                  numericInput('Pc',"Periodo de Copulación (Pc)",25, min = 0, max = 30)
                           ),
                           column(3,
                                  numericInput('NO',"Número de Oviposturas ",1, min = 1, max = 6)
                           )
                       )
                       
                       
                       
                       
                       ),
            
              tabPanel("Simulador",
                       
                       fluidRow(
                         
                         
                         box(width = 6, title = HTML("Parámetros de Inicialización"),#status = "primary",solidHeader = T,
                             tabBox(id=NULL, width =  12, #side =  "right", 
                                    tabPanel(p(HTML("<b style=color:#2876BC> INFESTACIÓN </b>"), icon("bugs")),
                                             fluidRow(
                                               column(3, 
                                                      p(HTML("<b>N.Brote/Municipio</b>"),span(shiny::icon("info-circle"), id = "info_brote"),numericInput('brote', NULL, value=18, min = 1,max = 20,step = 2),
                                                        tippy::tippy_this(elementId = "info_brote",tooltip = "El número de brotes determina el valor inicial del proceso de simulación",placement = "right"))
                                               ),
                                               column(3, 
                                                      p(HTML("<b>No. Adultos/Trampa</b>"), span(shiny::icon("info-circle"), id = "info_trampa"),numericInput('trampa', NULL,value=5,min =0,max=50,step=5),
                                                        tippy::tippy_this(elementId = "info_trampa",tooltip = "Número promedio de adultos/trampa a Y0", placement = "right")
                                                      )
                                               ),
                                               column(3,p(HTML("<b>No. Huevos/Ovipostura</b>"),span(shiny::icon("info-circle"), id = "info_egg"), selectInput('huevos', NULL,c(1,5,10,20,30),selected = 5),
                                                          
                                                          tippy::tippy_this(elementId = "info_egg", tooltip = "Ovipostura por lesión estimado por experimento <br> Se considera que un fruto de café puede tener un máximo de 3 larvas",placement = "right")
                                               )),
                                               
                                               column(3,
                                                      p(HTML("<b>Proporción H/M</b>"),span(shiny::icon("info-circle"), id = "hm"),numericInput('HM', NULL, value=0.51, min = 0,max = 1,step = 0.01),
                                                        tippy::tippy_this(elementId = "hm",tooltip =  "Este valor corresponde a la proporción de Hembras sobre machos en el cultivo." ,placement = "right"))
                                                      
                                               )
                                               
                                             )),
                                    tabPanel(p(HTML("<b style=color:#2876BC> MANEJO </b>"),icon("vial-virus")),
                                             fluidRow(
                                               column(3,p(HTML("<b> Tipo de producto</b>"), selectInput('product',NULL , choices  = c("Biológico 1","Biológico 2","Ninguno"), selected = "Ninguno", selectize =  T)),
                                               ),
                                               
                                               
                                               column(3,
                                                      dateInput('date1',label = ("Fecha 1.a aplicación de producto"),value = as.character("2017/05/01") ,format = "dd/mm/yyyy"), 
                                                      numericInput('porce1', "% Efectividad producto", 80, min = 0.0, max = 100.0, step = 0.1), 
                                                      
                                               ),
                                               
                                               column(3, dateInput('date2',label = "Fecha 2.a aplicación de producto",value = as.character(" "),format = "dd/mm/yyyy" ),
                                                      numericInput('periPQ',"Período de efectividad",30) 
                                               ),
                                               column(3, dateInput('date3',label = "Fecha 3.a aplicación de producto",value = as.character(" "),format = "dd/mm/yyyy")
                                                      
                                               )
                                               
                                               
                                             )
                                             
                                    ),
                                    tabPanel(p(HTML("<b style=color:#2876BC> COSECHA </b>"), icon("sun-plant-wilt")),
                                             fluidRow(
                                               column(3, dateInput('date4',label = "Inicio de cosecha",value = as.character(" "),format = "dd/mm/yyyy" )),
                                               column(3, dateInput('date5',label = "Fin  de Cosecha° ",value = as.character(" "),format = "dd/mm/yyyy" )),# date [dd/mm/aaaa]
                                               column(3, numericInput('porce2', "% finalización cosecha", 80, min = 0.0, max = 100.0, step = 0.1)) # date [dd/mm/aaaa] #value = as.character("30/10/2019")
                                               
                                             )
                                    ),
                                    tabPanel(p(HTML("<b style=color:#2876BC> CLIMA </b>"),icon("cloud")),
                                             fluidRow(
                                               column(3,
                                                      dateInput('perdesd', label="Período (Desde) ", value =as.character("2017/05/01"),  format = "dd/mm/yyyy"),
                                                      dateInput('perdhast', label="Hasta: ", value = as.character("2017/10/30"), format = "dd/mm/yyyy")
                                                      
                                               ),
                                               column(3, 
                                                      timeInput('hordesd', label="Horas:", value = strptime("8:00:00", "%T"),   minute.steps = 30),
                                                      timeInput('hordhast', label="Hasta:",  value =  strptime("18:00:00", "%T"), minute.steps = 30)
                                               ),
                                               
                                               column(3,
                                                      numericInput('tempdesd', "Temperaturas (°C)", value = "10",min = min(temperatura), max = max(temperatura)),
                                                      numericInput('tempdhast', "Hasta: ", value = "25")
                                               ),
                                               
                                               column(3,
                                                      numericInput('hrdesd', "HR (%)",value = "80", min =min(HR),max = max(HR)),
                                                      numericInput('hrdhast',"Hasta: ",value = "100")
                                                      
                                                      
                                               )
                                               
                                               
                                               
                                             )
                                    )
                                    
                             )),
                         box(title = "Parámetros Estimados", width = 6, #solidHeader = T,  status = "primary",
                             fluidRow( 
                               column(4,dateInput('dateperiod',label = HTML("<<<<b style=color:#2876BC>  Especifique tiempo </b>>>> "),value = as.Date("2017/07/12"), min = min(dates), max = max(dates), format = "dd/mm/yyyy" ))
                             ),
                             
                             fluidRow(
                               column(4, 
                                      numericInput('Abs', "No. Frutos Infestados (Absoluto)", value = 676 ), 
                                      numericInput('Abs1', "No. Brotes (Absoluto)", value = 89 )
                               ),
                               
                               
                               column(4, # br(),br(),br(), 
                                      numericInput('Acum1', "No. Frutos Infestados (Acumulados)", value =3378),
                                      numericInput('Acum2', "No. Brotes (Acumulados)", value = 2027 )
                                      
                               ) ,
                               column(4,
                                      numericInput('hrf', "Horas favorables (hrf)", value = 822 ),
                                      numericInput('hrf', "Índice de hrf", value = "0.53")
                               )
                               
                             )
                             
                             
                             
                         )
                         
                         
                       ),
                       
                       
                       hr( ),
                       
                       fluidRow( 
                         tabBox(title = HTML("<b>Modelo de estimación de frutos infestados</b>"), width = 6,
                                id = "tabset1",
                                tabPanel("Fig. (a)", plotlyOutput("sim1") %>% withSpinner(type = 5)),
                                tabPanel("Pruebas",  textOutput('proof')  %>% withSpinner(type = 5) ),
                                tabPanel("Click", verbatimTextOutput("click"))
                                
                         ),
                         
                         tabBox(title = HTML("<b>Modelo de estimación de brotes infestados</b>"), width = 6,
                                id = "tabset2",
                                tabPanel("Fig. (b)", plotlyOutput("rrp_plot") %>% withSpinner(type = 5)), #,#,
                                tabPanel("Modelos de distribución", plotlyOutput("r1") ),
                                tabPanel("Modelación gráfica", plotlyOutput("myPlot"))
                         )
                       )
                       
                       
                       
                       
                       ),
              tabPanel("Datos",
                       tabsetPanel(
                       tabPanel("Clima",tableOutput('clima')),
                       tabPanel("Históricos",tableOutput('histo'))))
              
              
              
              ),
   
   
  )
