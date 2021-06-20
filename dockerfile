#sets the base image for subsequent instructions
FROM continuumio/miniconda3

#copy files into the container
COPY ./api /api

#set the current working directory
WORKDIR /api

#dowloads the package lists form the repositories and 'updates' them to get incormation on the newsest versions of packages and their dependancies
RUN apt-get update 

# update conda and create the environment
RUN conda update -n base conda -y && conda env update --name recommender --file environment.yml

# activate conda environment
RUN echo "source activate recommender" > ~/.bashrc
ENV PATH /opt/conda/envs/recommender/bin:$PATH

# run the gunicorn command to start the service in docker
CMD ["gunicorn", "-w", "1", "-b", ":5000", "-t", "360", "wsgi:app"]