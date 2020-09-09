FROM jupyter/scipy-notebook
RUN conda create -c conda-forge -n rdkit-env rdkit ipykernel -y && \
    conda run -n rdkit-env python -m ipykernel install --user --name=rdkit-env
EXPOSE 8888
CMD jupyter lab --no-browser
