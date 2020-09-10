FROM jupyter/scipy-notebook
RUN conda install -c conda-forge rdkit & \
	mkdir notebooks
WORKDIR notebooks
CMD jupyter lab --no-browser
