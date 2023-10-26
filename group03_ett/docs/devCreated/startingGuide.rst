Notes on how to set up this project
===================================

Setting up git
--------------

**Downloading the repository**

One can download (clone) the git project by using the ``git clone`` command.

``git clone``

This will create a new folder ``group03_ett`` in which the git project will reside. Similarly it will create the needed structure for git to be able to create commits later on.

**Create a local git config**

After downloading the repository and entering it, execute following commands to create local settings for this project.

- ``git config --local user.name "first_Name last_Name"``
- ``git config --local user.email "first_Name.last_Name@email.de"``
- ``git config --local user.signinkey [KEYID]``
- ``git config --local commit.gpgsign true``

**Important Git Commands**

- Pull Changes.
    - To get new changes from the git repository, pull them from there by using ``git pull``

- Use a new branch to develop new features independently from the master branch.
    - Create branch ``git checkout -b new_branch``
    - (Optionally) push branch ``git push origin new_branch``

- Merge new_branch into master when the feature is done.
    - Switch to master ``git checkout master``.
    - Make sure master is up to date ``git pull``.
    - Merge with new_branch ``git merge new_branch``.
    - Push to master ``git push origin master``.
    - If done with branch, delete locally ``git branch -d new_branch``
    - If done with branch, delete remote ``git push -d origin new_branch``

- Merge from master into stable at the end of sprint.
    - Make sure master is up to date ``git pull``.
    - Switch to stable ``git checkout stable``.
    - Merge with master ``git merge master``.
    - Push to stable ``git push origin stable``.

Install Software
----------------

**Python on Windows 10**

- Download Python_.
- Install it and add Python to the PATH Env.
- (Optionally) Remove the PATH length limit.

.. _Python: https://www.python.org/downloads/

**Python on a GNU Distro**

- Download Python from your Repository or follow the same Link as Windwos.

    - e.g. Ubuntu ``sudo apt install python``

**make on Windows 10**

Make is used to install the dependencies for the python project. This tool is a standard tool under most GNU OSs, so Linux and MacOS include it by default. For Windows we need to install MinGW (Minimalist GNU for Windows), which allows us to use make there.

- Download MinGW_.
- Install MinGW. We only need mingw32-base for our project. To really install the choosen packages, click on ``Installation`` -> ``Apply Changes`` -> ``Apply``
- Add MinGW to the PATH Env.: ``set PATH=%PATH%;C:\MinGW\bin`` (Assuming one leaves the default paths).
- (Optionally) Add MingGW to the PATH Env. permanently: ``setx /M PATH "%PATH%;C:\MinGW\bin"``
- Use MinGW: ``mingw32-make``.

.. _MinGW: https://sourceforge.net/projects/mingw/files/

**Docker**

To achive a development enviroment that is the same across all platforms we use docker at the very beginning of the project to ensure that all developer have the same working enviroment. Docker makes sure that the project will run platform independent and allows us to work on any machine that we want.`

- Download Docker_.
- Install Docker.

    - Under Linux, one might need to add the current user to the ``docker`` Group with ``# usermod -aG docker USERNAME``. Furthermore, one may need to start and enable the systemprocess ``# systemctl enable docker.service && systemctl start docker.service``.

- Now, Docker will be able to download and install the necessary files to create a container.
- To make life easier, one can start Docker over the make file (first ``make build`` then ``make run``), or type in the command into the terminal by itself.

.. _Docker: https://www.docker.com/get-started/

Set up your Development Enviroment
----------------------------------

There is the paradoxon of choice, which states that too many choices will ultimately only confuse and deter people to choose anything. Working with Python is possible with pretty much anything as long as one has a Terminal and an Editor.

However, to make things as easy as possible to troubleshoot and to create a uniform working enviroment, I set up additional files to use with `Visual Studio Code`_. It is compatible with every major OS.

To use the prepared settings file, open a new workspace by way of opening the included ``vscode_group03_ett.code-workspace`` file. This will set the necessary Paths and Settings.

The included Terminal will then be able to automatically use the right path and enviroment, allowing for much easier troubleshooting etc. in the future.

Other choices are obviously also possible and allowed. :) Just beware that one has to enter the virtual python enviroment (denoted by ``(.venv)`` in the terminal) to install additional libraries etc.

.. _`Visual Studio Code`: https://code.visualstudio.com/

