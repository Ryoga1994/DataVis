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
table(dt$weaptype2_txt)

L1_dt <- dt[dt$weaptype2_txt=="Explosives/Bombs/Dynamite",
            c("latitude","longitude","popup")] 
L2_dt <- dt[dt$weaptype2_txt=="Incendiary",
            c("latitude","longitude","popup")]
L3_dt <- dt[dt$weaptype2_txt=="Melee",
            c("latitude","longitude","popup")]
L4_dt <- dt[dt$weaptype2_txt=="Firearms",
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

gmap <- leaflet() %>%
  #addTiles() %>%
  addProviderTiles(providers$CartoDB.Positron) %>%
  # addProviderTiles(providers$MtbMap) %>%
  # addProviderTiles(providers$Stamen.TonerLines,
  #                  options = providerTileOptions(opacity = 0.35)) %>%
  # addProviderTiles(providers$Stamen.TonerLabels) %>%
  addAwesomeMarkers(data=L1_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup, 
                    group="Explosives/Bombs/Dynamite",
                    icon=icon_L1) %>%
  addAwesomeMarkers(data=L2_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Incendiary",
                    icon=icon_L2) %>%
  addAwesomeMarkers(data=L3_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Melee",
                    icon=icon_L3) %>%
  addAwesomeMarkers(data=L4_dt, lat=~latitude, lng=~longitude, 
                    popup=~popup,
                    group="Firearms",
                    icon=icon_L4) %>%
  # Layers control
  addLayersControl(
    baseGroups = c("Explosives/Bombs/Dynamite"),
    overlayGroups = c("Incendiary",
                      "Melee",
                      "Firearms"),
    options = layersControlOptions(collapsed = FALSE)
  )

gmap
saveWidget(gmap, '~/Documents/Study/ANLY503/TakeHomeExam/DataVis/leaflet_map_by_weaptype.html', selfcontained = TRUE)







