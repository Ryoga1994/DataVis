# libs
library(leaflet)
library(sp)
library(mapproj)
library(maps)
library(mapdata)
library(maptools)
library(htmlwidgets)
library(magrittr)
library(XML)
library(plyr)
library(rgdal)
library(WDI)
library(raster)
library(noncensus)
library(stringr)
library(tidyr)
library(tigris)
library(rgeos)
library(glyphicon)
library(ggplot2)
library(scales)

# load data
dt = read.csv("~/Documents/Study/ANLY503/TakeHomeExam/DataVis/TerrorismDATA_Real_1970_2016.csv",
              header=T, sep=",")
colnames(dt)

popup_group <- paste0("<strong>Group Name: </strong>", 
                      dt$gname, 
                      "<br><strong>Motive: </strong>", 
                      dt$motive,
                      "<br><strong>Summary: </strong>",
                      dt$summary
                      )
dt$popup = popup_group

# top 3 attack type
# table(dt$attacktype1_txt)
# rank 1: Bombing/Explosion
# rank 2: Armed Assault
# rank 3: Assassination
table(dt$attacktype2_txt)

L1_dt <- dt[dt$attacktype2_txt=="Assassination",
            c("latitude","longitude","popup")] 
L2_dt <- dt[dt$attacktype2_txt=="Bombing/Explosion",
            c("latitude","longitude","popup")]
L3_dt <- dt[dt$attacktype2_txt=="Hostage Taking (Kidnapping)",
            c("latitude","longitude","popup")]
L4_dt <- dt[dt$attacktype2_txt=="Facility/Infrastructure Attack",
            c("latitude","longitude","popup")]

# icons
icon_L1 <- awesomeIcons(
  icon = 'ios-close',
  iconColor = 'black',
  library = 'ion',
  markerColor = 'red'
)

icon_L2 <- awesomeIcons(
  icon = 'ios-close',
  iconColor = 'black',
  library = 'ion',
  markerColor = 'green'
)

icon_L3 <- awesomeIcons()

icon_L4 <- awesomeIcons(  icon = 'ios-close',
                          iconColor = 'black',
                          library = 'ion',
                          markerColor = 'white')

# iconSet = awesomeIconList(
#   L1 = makeAwesomeIcon(icon='L1', iconColor='lightgreen',library='ion'),
#   L2 = makeAwesomeIcon(icon='L2', iconColor='lightred',library='fa'),
#   L3 = makeAwesomeIcon(icon='L3', iconColor='cadetblue', library='fa'),
#   L4 = makeAwesomeIcon(icon='L4', iconColor = 'pink', library='fa')
# )
# 
# icon_L1 <- iconSet['L1']
# icon_L2 <- iconSet['L2']
# icon_L3 <- iconSet['L3']
# icon_L4 <- iconSet['L4']


gmap <- leaflet() %>%
  #addTiles() %>%
  addProviderTiles(providers$CartoDB.Positron) %>%
  # addProviderTiles(providers$MtbMap) %>%
  # addProviderTiles(providers$Stamen.TonerLines,
  #                  options = providerTileOptions(opacity = 0.35)) %>%
  # addProviderTiles(providers$Stamen.TonerLabels) %>%
  addAwesomeMarkers(data=L1_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup, 
                    group="Assassination",
                    icon=icon_L1) %>%
  addAwesomeMarkers(data=L2_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Bombing/Explosion",
                    icon=icon_L2) %>%
  addAwesomeMarkers(data=L3_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Hostage Taking (Kidnapping)",
                    icon=icon_L3) %>%
  addAwesomeMarkers(data=L4_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Facility/Infrastructure Attack",
                    icon=icon_L4) %>%
  # Layers control
  addLayersControl(
    baseGroups = c("Assassination"),
    overlayGroups = c("Bombing/Explosion",
                      "Hostage Taking (Kidnapping)",
                      "Facility/Infrastructure Attack"),
    options = layersControlOptions(collapsed = FALSE)
  )

gmap
saveWidget(gmap, '~/Documents/Study/ANLY503/TakeHomeExam/DataVis/leaflet_map_by_attacktype.html', selfcontained = TRUE)







