## Running the Code

If you have any trouble with the following steps, please contact the repository maintainer, Tim Hargreaves, or reach out at [teaching@warwickdatascience.com](mailto:teaching@warwickdatascience.com).

### Option 1: Using Google Colab

1. Navigate to a subject example notebook (these end in .ipynb) and open it
2. Click the link at the top of the notebook to open Google Colab
3. If the notebook fails to load, click the 'raw' to open a plain text view and copy the link near the top that begins `https://colab.research` and ends `.ipynb`

### Option 2: Running the Notebooks Locally

1. Navigate to the [repository root](https://github.com/warwickdatascience/subject-examples) and select 'Code > Download ZIP'
2. Unzip the downloaded file
3. If you wish to update your local copy when changes are made to the repository, simply redownload the ZIP, or consider using version control software such as [Git](https://www.youtube.com/watch?v=uUuTYDg9XoI) which can be installed using [these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Option 2a: Using Docker (More work but guaranteed to succeed)

1. (Windows only) If you have Windows Home installed (rather than Windows Education/Pro), upgrade using the [free copy the University of Warwick provides](https://warwick.ac.uk/services/its/servicessupport/software/microsoft/windows10student)
2. Install [Docker](https://docs.docker.com/engine/install/) and run it
3. Open a terminal (Linux/OSX)/PowerShell prompt (Windows) in the `python` directory of the repositiory. On Windows, you can shift-click the `python` directory to do this
4. Run `docker build -t subject-examples-python .` to build the necessary image. You only ever have to do this once
5. Each time you want to launch the notebooks, run `docker run -it -p 8888:8888 -v <path>:/home/jovyan/notebooks se-python` replacing `<path>` with `$PWD` on Linux/OSX, `${PWD}` on Windows (PowerShell), and `%cd%` on Windows (Command Prompt)
6. An web address starting `http://127.0.0.1:8888` will appear. Copy this into your browser

#### Option 2b: Using Conda (Less work but likely to run into issues)

1. Install Conda by following [this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
2. Install any packages you need using `conda install -c conda-forge <package-name>` from the terminal/PowerShell/Command Prompt
3. Open the notebooks by running `jupyter lab` from the `python` directory and copying the supplied URL into your web browser
