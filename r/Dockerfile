FROM rocker/tidyverse
RUN apt-get update && apt-get install -y python3 \
    python3-pip \
    build-essential
RUN pip3 install jupyter
EXPOSE 8888
WORKDIR /home/rstudio
CMD jupyter notebook --no-browser --ip 0.0.0.0 --allow-root --port 8888