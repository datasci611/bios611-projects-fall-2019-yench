data/analysis/client.csv: \
			scripts/data_wrangling.py \
			data/raw/ACSDP5Y2017.DP05_data_with_overlays_2019-11-17T201128.csv \
			data/raw/ACS_17_5YR_B21001_with_ann.csv \
			data/raw/ACS_17_5YR_S1810_with_ann.csv \
			data/raw/CLIENT_191102.tsv.txt
	docker run -it\
		--rm -v $(shell pwd):/workdir \
		-w /workdir \
		amancevice/pandas:0.25.2-slim \
			python scripts/data_wrangling.py \
			data/analysis/clients.csv

pull-pandas:
	docker pull amancevice/pandas:0.25.2-slim && touch $@


build-tidyr: Dockerfile
	docker build -t yench/tidyr . -f Dockerfile && touch $@

	
results/Project3_Report.html: \
			results/Project3_Report.Rmd \
			data/analysis/client.csv \
			data/analysis/summary_sex.csv \
			data/analysis/summary_age.csv \
			data/analysis/summary_race.csv \
			data/analysis/summary_ethnicity.csv \
			data/analysis/summary_veteran.csv \
			data/analysis/durham_disability.csv 
	docker run -it --rm \
	-v $(shell pwd):/workdir \
	-w /workdir yench/tidyr \
	Rscript -e "library(rmarkdown); rmarkdown::render('results/Project3_Report.Rmd','html_document')"
 
 
