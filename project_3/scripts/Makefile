data/analysis/client.csv: \
			scripts/data_wrangling.py \
			data/raw/ACSDP5Y2017.DP02_data_with_overlays_2019-11-18T123256.csv \
  			data/raw/ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv \
			data/raw/CLIENT_191102.tsv.txt
	docker run -it\
		--rm -v $(shell pwd):/workdir \
		-w /workdir \
		amancevice/pandas:0.25.2-slim \
			python scripts/data_wrangling.py \
			data/analysis/clients.csv
	
results/report.html: \
			report.RmD \
			client.csv \
			durham_sex.csv \
			durham_age.csv \
			durham_race.csv \
			durham_ethnicity.csv \
			durham_veteran.csv \
			durham_disability.csv 
	docker run -it --rm \
	-v $(shell pwd):/workdir \
	-w /workdir rocker/tidyverse \
	Rscript -e "library(rmarkdown); rmarkdown::render('results/report.Rmd','html_document')
 
 
